#! /usr/bin/env python2.7
"""projectname URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from projectname.home.views import HomeView
from autocomplete import views

#from autocomplete import views
#import projectname.autocomplete

#admin.autodiscover()
print("hoge******************")
urlpatterns = [
    # Homepage
    #url(r'^autocomplete/$', 'autocomplete.views.index'),
    url(r'^autocomplete/$', 'projectname.autocomplete.views.index'),
    url(r'^autocomplete/([0-9a-zA-Z]+)/$', 'projectname.autocomplete.views.suggest'),
    #url(r'^autocomplete/([0-9a-zA-Z]+)/$', 'views.suggest'),
    url(r'^$', HomeView.as_view(), name='home'),
    #url(r'^admin/', include(admin.site.urls))
    #url(r'^autocomplete/(?P<input>[0-9a-zA-Z]d+)/$', 'autocomplete.suggest')
]
