from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
]
