from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from django.views import defaults as default_views
from life.views import DashboardView, HomePageView, MoleculeView, set_language, MoleculeDetailView, BlogDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path(_("molekuller"), MoleculeView.as_view(), name="molecule"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("users/", include("newlife.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path(_("molekuller/<slug:slug>"),MoleculeDetailView.as_view(),name="molecule-detail"),
    path(_("blog/<slug:slug>"),BlogDetailView.as_view(),name="blog-detail")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>", set_language, name="set-language"),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
