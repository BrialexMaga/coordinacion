from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('export-contacts/', views.exportContacts, name='export-contacts'),
    path("createform/", views.createFormStudent, name="createFormStudent"),
    path("contactform/<int:idStudent>/", views.createFormContact, name='contact-form'),
    path("contact/<int:idStudent>/", views.showContact, name='show-contact'),
]