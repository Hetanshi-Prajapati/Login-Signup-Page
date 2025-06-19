from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index,name='index'),
    path('hello/', views.hello,name='hello'),
    path('signup/', views.signup_view,name='signup'),
    path('', views.login_view,name='login'),
    path('lgsuccess/', views.welcome_view,name='lgsuccess'),
]