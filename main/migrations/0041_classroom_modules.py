# Generated by Django 4.2.1 on 2023-06-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_alter_attendence_report_classroom_alter_lesson_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='modules',
            field=models.ManyToManyField(to='main.module'),
        ),
    ]
