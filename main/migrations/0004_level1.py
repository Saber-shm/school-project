# Generated by Django 4.2.1 on 2023-06-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_level_students_info_delete_level1_delete_level2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
    ]