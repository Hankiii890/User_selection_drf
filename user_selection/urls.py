from django.urls import path
from .views import UserDetailViews

urlpatterns = [
    path('api/users/<int:pk>/', UserDetailViews.as_view(), name='user-detail')
]