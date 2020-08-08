from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template='login.html'), name='login')
    path('logout/', auth_views.LogoutView, name='logout' )
]
