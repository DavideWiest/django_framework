"""PROJECT_NAME URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.views.decorators.http import require_GET
from django.http import HttpResponse


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Allow: /",
        "Sitemap: https://davidewiest.com/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


@require_GET
def sitemap_txt(request):
    lines = [
        "https://davidewiest.com/"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('_api.urls')),
    path('legal/', include('legal.urls')),
    path('', include('_site.urls')),
    path("robots.txt", robots_txt),
    path("sitemap.txt", sitemap_txt)
]
