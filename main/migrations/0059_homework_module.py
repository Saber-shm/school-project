# Generated by Django 4.2.1 on 2023-06-24 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0058_homework'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.module'),
        ),
    ]
