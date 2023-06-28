# Generated by Django 4.2.1 on 2023-06-13 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0020_alter_lesson_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('french_grade', models.FloatField(blank=True)),
                ('arabic_grade', models.FloatField(blank=True)),
                ('mathematic_grade', models.FloatField(blank=True)),
                ('ei_grade', models.FloatField(blank=True)),
                ('hg_grade', models.FloatField(blank=True)),
                ('pc_grade', models.FloatField(blank=True)),
                ('svt_grade', models.FloatField(blank=True)),
                ('final_grade', models.FloatField(blank=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
