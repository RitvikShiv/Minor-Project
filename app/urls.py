from django.urls import path
from . import views

urlpatterns = [
    path('', views.showcovid,name='home'),
    path('india/', views.showIndia,name='india'),
    path('state/', views.showState,name='state'),
    path('vaccine/', views.showVaccine,name='vaccine'),
]