from django.urls import path

from .views import *

urlpatterns = [
    path('url/', UrlShortnerView.as_view(), name='update_availability'),
]
