from django.db import models

# Create your models here.
class School_Cycle(models.Model):
    idCycle = models.AutoField(primary_key=True)
    year = models.CharField(max_length=5)
    cycle_period = models.CharField(max_length=1)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.year}{self.cycle_period}"
    
class Student(models.Model):
    idStudent = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    admission_cycle = models.CharField(max_length=5, null=True)

    '''
    last_cycle = models.ForeignKey(
        School_Cycle,
        on_delete=models.CASCADE,
        related_name='estudiantes_actual',
        null=True,
        blank=True,
    )
    '''

    #average_score = models.SmallIntegerField()
    #

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    idContact = models.BigAutoField(primary_key=True)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    udg_email = models.EmailField()
    emergency_phone = models.CharField(max_length=25)
    url_socialnet = models.URLField(null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    idStudent = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idContact}"
