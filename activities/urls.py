from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^edit_lecture/$', views.register_lecture, name = "edit_lecture"),
    url(r'^view_lecture/$', views.view_lecture, name = "view_lecture" ),
    ]
