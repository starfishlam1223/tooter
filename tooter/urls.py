"""tooter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from toots.views import (
    toot_detail_view,
    toot_list_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", toot_list_view),
    path("<int:toot_id>/", toot_detail_view),
    path("react/", TemplateView.as_view(template_name="react.html")),
    path("api/toots/", include("toots.api.urls")),
    path("api/profiles/", include("profiles.api.urls")),
    re_path(r"accounts?/", include("accounts.urls")),
    re_path(r"profiles?/", include("profiles.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
