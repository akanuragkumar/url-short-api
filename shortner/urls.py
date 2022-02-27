from django.urls import path
from . views import UrlShortnerView

app_name = 'shortner'

urlpatterns = [
    path('', UrlShortnerView, name='home'),
    path('<str:pk>', UrlShortnerView, name='final')
]
