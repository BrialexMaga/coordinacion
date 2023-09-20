from django.db import models

# Create your models here.
class School_Cycle(models.Model):
    cycle_id = models.AutoField(primary_key=True)
    period = models.CharField(max_length=5)

    def __str__(self):
        return self.period
    
class Contact(models.Model):
    contact_id = models.BigAutoField(primary_key=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    udg_email = models.EmailField()
    emergency_phone = models.CharField(max_length=15)
    url_socialnet = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.phone
    
class Student(models.Model):
    student_id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    contact_id = models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.name