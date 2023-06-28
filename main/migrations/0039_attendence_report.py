# Generated by Django 4.2.1 on 2023-06-16 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_lesson_teacher_alter_module_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('m1', models.BooleanField(default=True)),
                ('m2', models.BooleanField(default=True)),
                ('m3', models.BooleanField(default=True)),
                ('m4', models.BooleanField(default=True)),
                ('e1', models.BooleanField(default=True)),
                ('e2', models.BooleanField(default=True)),
                ('e3', models.BooleanField(default=True)),
                ('e4', models.BooleanField(default=True)),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.classroom')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.student')),
            ],
        ),
    ]