from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createform/", views.createFormStudent, name="createFormStudent"),
    path("contact/<int:student_id>/", views.createFormContact, name='contact-form'),
]