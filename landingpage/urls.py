from django.urls import path
from .views import MyLoginView, my_logout_view
from . import views

urlpatterns = [
    path('', views.landingPage, name='landing-page'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', my_logout_view, name='logout'),
]