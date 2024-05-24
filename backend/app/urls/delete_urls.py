from django.urls import path
from app.views.delete_views import Delete_User


urlpatterns = [
    path('', Delete_User, name='Delete_User'),
]