"""
URL configuration for MaeStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import archive.views
urlpatterns = [
    path('admin/', admin.site.urls),
    # TODO: make archive URLS their own namespace and file
    path('read/<int:snowflake_id>', archive.views.read, name='read'),
    path('index/', archive.views.index, name='index'),
    path('upload/', archive.views.upload, name='upload'),
    path('search/', include('haystack.urls'))

]
