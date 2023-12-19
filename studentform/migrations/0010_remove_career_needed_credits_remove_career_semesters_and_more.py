# Generated by Django 4.2.5 on 2023-12-19 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentform', '0009_student_exchange'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='needed_credits',
        ),
        migrations.RemoveField(
            model_name='career',
            name='semesters',
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('idSyllabus', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('semesters', models.PositiveSmallIntegerField()),
                ('needed_credits', models.PositiveSmallIntegerField()),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studentform.career')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('idSemester', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.PositiveSmallIntegerField()),
                ('syllabus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentform.syllabus')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='syllabus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='studentform.syllabus'),
        ),
    ]
