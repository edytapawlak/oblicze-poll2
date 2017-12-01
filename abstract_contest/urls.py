from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^choose_lectures/$', views.choose_lectures, name = "choose_lectures"),
    url(r'^choose_posters/$', views.choose_posters, name = "choose_posters"),
    ]
