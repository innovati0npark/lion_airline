from django.urls import path
from app.views.flights_views import get_flights


urlpatterns = [
    path('', get_flights, name='get_tickets'),
    
]