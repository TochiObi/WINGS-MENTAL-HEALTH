from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', views.Logout, name='logout'),
    path('recover-password/', views.RecoverPassword.as_view(),
         name='recover-password'),
    path('description/', views.Description.as_view(), name='description'),
    path('forum/<category>/', views.Forum.as_view(), name='forum'),
]
