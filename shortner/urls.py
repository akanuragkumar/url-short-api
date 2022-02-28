from django.urls import path
from . views import UrlShortnerView

app_name = 'shortner'

urlpatterns = [
    path('url/', UrlShortnerView, name='home'),
    path('<str:pk>', UrlShortnerView, name='final')
]
