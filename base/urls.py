
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name = 'home'),
    path('signup', views.signup_page, name='signup'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_user, name="logout"),
    path('blog', views.blog,name='blog'),
]