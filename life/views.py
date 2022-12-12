from urllib.parse import urlparse

from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.views import View

from life.models import Comment, Molecule, NewLifeManagementMember


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
        return render(
            request=request, template_name="pages/homepage.html", context=context
        )


class MoleculeView(View):
    http_method_names = ["get"]

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {}
        context["molecules"] = Molecule.objects.all()
        return render(
            request=request, template_name="pages/models_page.html", context=context
        )
