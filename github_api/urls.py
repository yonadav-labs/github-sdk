"""github_api URL Configuration

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

from gauth.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/signup/$', signup),
    url(r'^api/v1/repos/(?P<org>[\w-]+)/$', repos),
    url(r'^api/v1/teams/(?P<org>[\w-]+)/$', teams),
    url(r'^api/v1/members/(?P<org>[\w-]+)/(?P<team>\d+)/$', members),
    url(r'^api/v1/assign_repo/(?P<org>[\w-]+)/(?P<team>\d+)/$', assign_repo),
]
