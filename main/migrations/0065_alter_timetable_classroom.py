# Generated by Django 4.2.1 on 2023-06-30 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0064_alter_student_user_alter_teacher_user_monitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.classroom'),
        ),
    ]
