"""TestProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from TestApp.views import index
from TestApp.views import *
from TestProject import settings
from django.contrib.staticfiles import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index),
    url(r'^add/$',add, name='add' ),
    url(r'^add/(\d+)/(\d+)/$', add2, name='add2'),
    url(r'^home/$', home),
    url(r'^home/add/$', home_add),
            
    url(r'^static/(?P<path>.*)$', views.serve),

]

