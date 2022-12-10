from django.shortcuts import render
from django.views import View
from life.models import NewLifeManagementMember


class HomePageView(View):
    http_method_names = ["get"]

    def get(self,request):
        context = {}
        context["management_members"] = NewLifeManagementMember.objects.all()
        return render(request=request,template_name="pages/homepage.html",context=context)
