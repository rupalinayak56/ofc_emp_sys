# Generated by Django 5.1.1 on 2024-10-26 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0003_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=100),
        ),
    ]
