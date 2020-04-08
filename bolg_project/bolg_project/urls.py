"""bolg_project URL Configuration

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
from django.urls import path
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.autologin),
    path('login/',views.login),
    path('index/',views.index),
    path('regist/',views.regist),
    path('inf/',views.inf),
    path('updateinf/',views.updateinf),
    path('article/',views.article),
    path('addarticle/',views.addarticle),
    path('articledetail/',views.articledetail),
    path('updatearticle/',views.updatearticle),
    path('delarticle/',views.delarticle),
]
