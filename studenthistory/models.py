from django.db import models
from django.core.validators import MaxValueValidator
from studentform.models import School_Cycle, Student, Career, Subject, SoftDeletionModel, SoftDeletionModelManager

class Section(SoftDeletionModel):
    idSection = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    nrc = models.CharField(max_length=15)
    section = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.section} - {self.subject}"

class GradePeriod(models.Model):
    idGradePeriod = models.AutoField(primary_key=True)
    code_name = models.CharField(max_length=3)
    grade_period = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.grade_period} ({self.code_name})"

class Course(SoftDeletionModel):
    idCourse = models.AutoField(primary_key=True)
    school_cycle = models.ForeignKey(School_Cycle, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    grade = models.CharField(max_length=5)
    grade_period = models.ForeignKey(GradePeriod, on_delete=models.PROTECT)
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.school_cycle} - {self.section} - {self.student}"

class CareerSubject(SoftDeletionModel):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('career', 'subject')