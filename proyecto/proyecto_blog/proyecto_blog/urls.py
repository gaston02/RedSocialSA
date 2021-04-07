"""proyecto_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
from app_blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('registro', views.registro, name="registro"),
    path('crear_autor', views.crear_autor, name="crear_autor"),
    path('login', views.login, name="login")
]

"""if(settings.DEBUG):
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root':settings.MEDIA_ROOT, 
        }),
    ]"""

"""if(settings.DEBUG):
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_URL)"""