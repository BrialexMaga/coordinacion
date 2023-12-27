from django.urls import path
from . import views

urlpatterns = [
    path('', views.filterRateSubjectFailures, name='filter-failure-page'),
    path('cycle/', views.byCycleFilter, name='cycle-page'),
    path('cycle_subject/', views.byCycleSubjectFilter, name='cycle-subject-page'),
    path('range_cycle/', views.byCycleRangeFilter, name='cycle-range-page'),
]