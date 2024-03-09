from django.urls import path
from . import views

urlpatterns = [
    path('async/', views.http_call_async, name='async_call'),
]
