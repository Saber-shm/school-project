# Generated by Django 4.2.1 on 2023-06-19 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0043_remove_attendence_report_student_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=120)),
                ('last_name', models.CharField(blank=True, max_length=120)),
                ('birthday', models.DateField(blank=True)),
                ('mothers_full', models.CharField(blank=True, max_length=120)),
                ('father_full', models.CharField(blank=True, max_length=120)),
                ('mother_email', models.EmailField(blank=True, max_length=254)),
                ('father_email', models.EmailField(blank=True, max_length=254)),
                ('mother_phone_number', models.CharField(max_length=120)),
                ('father_phone_number', models.CharField(max_length=120)),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.classroom')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.level')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('year_study', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.year_study')),
            ],
        ),
        migrations.AddField(
            model_name='attendence_report',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.student'),
        ),
    ]