from django.urls import path
from app.views.login_views import login

urlpatterns = [
    path('', login, name='login'),
]