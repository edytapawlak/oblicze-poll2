from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^view_poll/$', views.view_poll, name = "view_poll"),
    url(r'^edit_poll/$', views.edit_poll, name = "edit_poll"),
    url(r'^finish_poll/$', views.finish_poll, name = "finish_poll"),
    url(r'^results/$', views.results, name = "results"),
    url(r'^edit_poll_poster/$', views.edit_poll_poster, name = "edit_poll_poster"),
    ]
