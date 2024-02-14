from django.urls import path
from . import views

urlpatterns = [
    path('', views.filterRateSubjectFailures, name='filter-failure-page'),
    path('cycle/', views.byCycleFilter, name='cycle-page'),
    path('cycle_subject/', views.byCycleSubjectFilter, name='cycle-subject-page'),
    path('range_cycle/', views.byCycleRangeFilter, name='cycle-range-page'),
    path('export_by_cycle/', views.exportByCycle, name='export-by-cycle-page'),
    path('export_by_cycle_subject/', views.exportByCycleSubject, name='export-by-cycle-subject-page'),
]