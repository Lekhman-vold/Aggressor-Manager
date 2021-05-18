from django.urls import path
from django.contrib.auth import views
from .views import user_profile, user_login, user_register

app_name = 'user'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register-user'),
    # path('login/', views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('profile/', user_profile),
]
