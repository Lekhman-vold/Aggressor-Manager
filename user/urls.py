from django.urls import path
from django.contrib.auth import views
from .views import user_profile, user_login, user_register, get_dashboard, user_cards

app_name = 'user'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register-user'),
    path('dashboard/', get_dashboard, name='dashboard'),
    path('profile/', user_profile),
    path('users/', user_cards)

]
