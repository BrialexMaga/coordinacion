from django.urls import path
from . import views

urlpatterns = [
    path('', views.filterGeneration, name='student-statistics-search-page'),
    path('show/<int:generation>/', views.showStatistics, name='show-statistics'),
]