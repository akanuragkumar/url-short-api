from django.urls import path

from .views import *

urlpatterns = [
    path('url/', UrlShortnerView.as_view(), name='url_shortner'),
    path('redirect_url/', ReDirectUrl.as_view(), name='url_redirect'),
    path('search/', SearchKeyword.as_view(), name='search'),
]
