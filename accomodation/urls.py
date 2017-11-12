from django.conf.urls import url
from accomodation.views import AccomodationView


urlpatterns = [
        url(r'^$', AccomodationView.as_view(), name = "accomodation"),
        ]
