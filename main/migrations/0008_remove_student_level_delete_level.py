# Generated by Django 4.2.1 on 2023-06-07 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_student_delete_level1_delete_level3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='level',
        ),
        migrations.DeleteModel(
            name='Level',
        ),
    ]
