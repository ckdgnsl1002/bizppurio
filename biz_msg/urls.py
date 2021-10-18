from django.urls import path
from . import views

urlpatterns = [
    path('get_token/', views.request_token),
]
