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
    
class Career(models.Model):
    idCareer = models.AutoField(primary_key=True)
    code_name = models.CharField(max_length=5)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.code_name
    
class Status(models.Model):
    idStatus = models.AutoField(primary_key=True)
    code_name = models.CharField(max_length=3)
    status = models.CharField(max_length=40)

    def __str__(self):
        return self.code_name
    
class Syllabus(models.Model):
    idSyllabus = models.AutoField(primary_key=True)
    career = models.ForeignKey(Career, on_delete=models.PROTECT)
    name = models.CharField(max_length=45)
    semesters = models.PositiveSmallIntegerField()
    needed_credits = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.career} - Plan {self.name}"

class Semester(models.Model):
    idSemester = models.AutoField(primary_key=True)
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.syllabus.career} - Semestre {self.number}"
    
class Student(models.Model):
    idStudent = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=50)
    first_last_name = models.CharField(max_length=30)
    second_last_name = models.CharField(max_length=30)

    status = models.ForeignKey(Status, on_delete=models.PROTECT,
                               related_name='students')
    exchange = models.BooleanField(default=False)
    admission_cycle = models.ForeignKey(School_Cycle, on_delete=models.PROTECT, 
                                        related_name='admission_cycle')
    last_cycle = models.ForeignKey(School_Cycle, on_delete=models.PROTECT, 
                                   related_name='last_cycle')
    idCareer = models.ForeignKey(Career, on_delete=models.PROTECT,
                                 related_name='students')
    syllabus = models.ForeignKey(Syllabus, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.name} {self.first_last_name} {self.second_last_name}"
    
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
