from django.contrib import admin
from django.urls import include, path
from django.views.decorators.cache import cache_page
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from velosafe.maps.views import PreferencesFormView, UserRouteView

schema_view = get_schema_view(
    openapi.Info(
        title="velosafe API",
        default_version="v1",
        contact=openapi.Contact(email="mail@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/doc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(
        "api/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger",
    ),
    path("preferences-form/", PreferencesFormView.as_view()),
    path("user-route/", UserRouteView.as_view()),
    path("__debug__/", include("debug_toolbar.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    path("", include("velosafe.maps.urls")),
]
