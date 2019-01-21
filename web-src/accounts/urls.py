from django.urls import path
from .views import LoginView, logout_user, RegistrationView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('signup', RegistrationView.as_view(), name='signup'),
]