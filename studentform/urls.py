from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="contacts"),
    path('export-contacts/', views.exportContacts, name='export-contacts'),
    path('contactform/<int:idStudent>/export/', views.exportStudentData, name='export-student-contact'),

    path("createform/", views.createFormStudent, name="createFormStudent"),
    path("contactform/<int:idStudent>/", views.createFormContact, name='contact-form'),
    path("contact/<int:idStudent>/", views.showContact, name='show-contact'),
]