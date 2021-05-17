from django.urls import path
from django.contrib.auth import views
from .views import user_profile, user_login


urlpatterns = [
    path('login/', user_login, name='login'),
    # path('login/', views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('profile/', user_profile),
]
