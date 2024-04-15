from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('intake-details/', views.intake_details, name='intake_details'),
]
