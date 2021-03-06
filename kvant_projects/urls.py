"""kvant_projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Homeвфыв
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from kvant_projects.apps.kvant_proj.views import index, kvantums, kvantum, kvant_project


urlpatterns = [
    # re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('kvantums', kvantums, name='kvantums'),
    re_path(r'^kvantum/(?P<kvantum_id>\d+)$', kvantum, name='kvantum'),
    re_path(r'^project/(?P<project_id>\d+)$', kvant_project, name='project'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)



