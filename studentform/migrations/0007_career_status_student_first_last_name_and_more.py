# Generated by Django 4.2.5 on 2023-11-01 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentform', '0006_alter_school_cycle_cycle_period_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('idCareer', models.AutoField(primary_key=True, serialize=False)),
                ('code_name', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=100)),
                ('needed_credits', models.PositiveSmallIntegerField()),
                ('semesters', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('idStatus', models.AutoField(primary_key=True, serialize=False)),
                ('code_name', models.CharField(max_length=3)),
                ('status', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='first_last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='last_cycle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='last_cycle', to='studentform.school_cycle'),
        ),
        migrations.AddField(
            model_name='student',
            name='second_last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='admission_cycle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='admission_cycle', to='studentform.school_cycle'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='idCareer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='students', to='studentform.career'),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='students', to='studentform.status'),
        ),
    ]
