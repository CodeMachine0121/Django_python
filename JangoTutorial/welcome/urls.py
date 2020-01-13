"""JangoTutorial URL Configuration

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

from . import views
urlpatterns = [
    path("",views.index,name="index"),

    #只能傳遞int 型態給year
    #預設是str 
    #slug 有包含ASCII的str
    path("articles/<int:year>",views.year_archive),

    path("articles/<slug:month>/<slug:year>",views.month_archive),
    #http://localhost:8000/welcome/articles/12/2012
]
