"""oblicze URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from oblicze import views

urlpatterns = [
    url(r'^$', views.login_redirect, name = 'login_redirect') ,
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls', namespace = 'accounts')),
    url(r'^accomodation/', include('accomodation.urls', namespace = 'accomodation')),
    url(r'^activities/', include('activities.urls', namespace = 'activities')),
    url(r'^schedule/', include('schedule.urls', namespace = 'schedule')),  
    url(r'^abstract_contest/', include('abstract_contest.urls', namespace = 'abstract_contest')),
    url(r'^poll/', include('poll.urls', namespace = 'poll')),  
]
