# Generated by Django 4.2.5 on 2024-01-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studenthistory', '0006_alter_careersubject_subject_alter_section_subject_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='careersubject',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
