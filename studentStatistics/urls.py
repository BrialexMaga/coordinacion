from django.urls import path
from . import views

urlpatterns = [
    path('', views.statisticSearchPage, name='student-statistics-search-page'),
]