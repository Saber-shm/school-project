# Generated by Django 4.2.1 on 2023-06-07 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_level_student_level'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]