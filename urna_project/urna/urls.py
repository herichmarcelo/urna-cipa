from django.urls import path
from . import views

app_name = 'urna'

urlpatterns = [
    path('', views.funcionario_login, name='funcionario_login'),
    path('vote/', views.vote_screen, name='vote_screen'),
    path('receipt/', views.receipt, name='receipt'),
]
