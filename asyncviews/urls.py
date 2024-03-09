from django.urls import path
from .views import AsyncCallView

urlpatterns = [
    path('async/', AsyncCallView.as_view(), name='async_view'),
]
