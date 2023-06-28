# Generated by Django 4.2.1 on 2023-06-19 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_grade_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='year_of_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.year_study'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='year_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.year_study'),
        ),
        migrations.AddField(
            model_name='level',
            name='year_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.year_study'),
        ),
        migrations.AddField(
            model_name='module',
            name='year_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.year_study'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='year_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.year_study'),
        ),
    ]
