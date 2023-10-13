from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student

from .factories import ContactFactory

@receiver(post_save, sender=Student)
def create_contact(sender, instance, created, **kwargs):
     if created:
        contact = ContactFactory(idStudent=instance)
        contact.save()