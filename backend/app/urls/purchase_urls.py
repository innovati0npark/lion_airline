from django.urls import path
from app.views.purchase_views import purchase

urlpatterns = [
    path('', purchase, name='purchase'),
    
]