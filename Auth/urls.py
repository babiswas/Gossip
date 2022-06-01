from django.urls import path
from .views import AppLogin
from .views import RegisterView

app_name = 'Auth'

urlpatterns = [
    path('login/', AppLogin.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]