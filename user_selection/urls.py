from django.urls import path
from .views import UserDetailViews

urlpatterns = [
    # URL для получения деталей пользователя по его ID
    path('api/users/<int:pk>/', UserDetailViews.as_view(), name='user-detail')
]