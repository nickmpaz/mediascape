from django.urls import path
from . import views
from .forms import CustomAuthenticationForm
from django.urls import include, path
from django.conf.urls import url

from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=CustomAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('comments/', views.comments, name='comments')
]