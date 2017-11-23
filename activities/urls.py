from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^edit_lecture/$', views.register_lecture, name = "edit_lecture"),
    url(r'^view_lecture/$', views.view_lecture, name = "view_lecture" ),
    url(r'^view_poster/$', views.view_poster, name = "view_poster"), 
    url(r'edit_poster/$', views.edit_poster, name = "edit_poster"), 
    ]
