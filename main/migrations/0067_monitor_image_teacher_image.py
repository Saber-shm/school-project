# Generated by Django 4.1.6 on 2023-07-03 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0066_alter_timetable_p1_alter_timetable_p2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]