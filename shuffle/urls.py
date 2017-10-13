from django.conf.urls import url
from . import views

app_name = 'shuffle'
urlpatterns = [
    url(r'^gettopfromsoolve/', views.get_top_from_soolve, name='gettopsoolve'),
    url(r'^gettopfromgoogle/', views.get_top_from_google, name='gettopgoogle'),
    url(r'^searchgraph/', name='searchgraph')
]