# Generated by Django 4.2.1 on 2023-06-19 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_student_adress_teacher_lesson_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='father_full',
            new_name='father_full_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='mothers_full',
            new_name='mothers_full_name',
        ),
    ]