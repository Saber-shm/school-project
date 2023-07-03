# Generated by Django 4.2.1 on 2023-06-29 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0060_student_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lunch_break', models.CharField(max_length=120)),
                ('classroom', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.classroom')),
                ('p1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable_p1', to='main.module')),
                ('p2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable_p2', to='main.module')),
                ('p3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable_p3', to='main.module')),
                ('p4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable_p4', to='main.module')),
                ('p5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable_p5', to='main.module')),
                ('p6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable_p6', to='main.module')),
                ('posted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('year_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.year_study')),
            ],
        ),
    ]
