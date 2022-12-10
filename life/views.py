from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from life.models import Comment, NewLifeManagementMember


class HomePageView(View):
    http_method_names = ["get"]

    def get(self, request) -> HttpResponse:
        context = {}
        context["management_members"] = NewLifeManagementMember.objects.all()
        context["user_comments"] = Comment.objects.filter(is_active=True)
        return render(
            request=request, template_name="pages/homepage.html", context=context
        )
