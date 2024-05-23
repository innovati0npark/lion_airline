from django.urls import path
from app.views.signup_views import signup

urlpatterns = [
    path('', signup, name='signup'),
]