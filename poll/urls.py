from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^view_poll/$', views.view_poll, name = "view_poll"),
    url(r'^edit_poll/$', views.edit_poll, name = "edit_poll"),
    ]
