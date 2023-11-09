from django.urls import path
from . import views

urlpatterns = [
    path('', views.searchPage, name='history-search-page'),
    path('show/', views.showHistory, name='show-history-page'),
]