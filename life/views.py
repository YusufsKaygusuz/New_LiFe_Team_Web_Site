from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.views import View
from django.views.generic import DetailView, FormView, UpdateView

from life.forms import UserDashboardForm
from life.models import Card, Comment, Molecule, NewLifeManagementMember, Blog, FavoriteBlog, FavoriteMolecule
from newlife.users.models import User


def set_language(request: HttpRequest, language: str) -> HttpResponse:
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response


class HomePageView(View):
    http_method_names = ["get"]

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {}
        context["management_members"] = NewLifeManagementMember.objects.all()
        context["user_comments"] = Comment.objects.filter(is_active=True)
        context["blogs"] = Blog.objects.all()
        return render(
            request=request, template_name="pages/homepage.html", context=context
        )


class DashboardView(LoginRequiredMixin,UpdateView):
    template_name = "pages/dashboard.html"
    form_class = UserDashboardForm
    success_url = "/dashboard/"

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id)



class MoleculeView(View):
    http_method_names = ["get"]

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {}
        molecules = Molecule.objects.all()
        context["cards"] = Card.objects.order_by('?')[:5]
        if self.request.GET.get("search"):
            molecules = molecules.filter(
                title__icontains=self.request.GET.get("search")
            )
        context["molecules"] = molecules
        return render(
            request=request, template_name="pages/models_page.html", context=context
        )


class MoleculeDetailView(DetailView):
    context_object_name = "molecule"
    template_name = "pages/molecule_detail.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Molecule,slug=self.kwargs.get('slug'))


class BlogDetailView(DetailView):
    context_object_name = "blog"
    template_name = "pages/blog.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Blog,slug=self.kwargs.get("slug"))


class AddToFavoriteBlog(View):
    http_method_names = ["post"]

    def post(self,request):
        obj = FavoriteBlog.objects.filter(user=self.request.user,blog__slug=request.POST.get("blog"))
        if obj.exists():
            obj.delete()
        else:
            FavoriteBlog.objects.create(user=self.request.user,blog=Blog.objects.get(slug=request.POST.get("blog")))
        return redirect("blog-detail",slug=Blog.objects.get(slug=request.POST.get("blog")).slug)


class AddToFavoriteMolecule(View):
    http_method_names = ["post"]

    def post(self,request):
        obj = FavoriteMolecule.objects.filter(user=self.request.user,molecule__slug=request.POST.get("molecule"))
        if obj.exists():
            obj.delete()
        else:
            FavoriteMolecule.objects.create(user=self.request.user,molecule=Molecule.objects.get(slug=request.POST.get("molecule")))
        return redirect("molecule-detail",slug=Molecule.objects.get(slug=request.POST.get("molecule")).slug)
