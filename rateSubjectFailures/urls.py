from django.urls import path
from . import views

urlpatterns = [
    path('', views.filterRateSubjectFailures, name='filter-failure-page'),
]