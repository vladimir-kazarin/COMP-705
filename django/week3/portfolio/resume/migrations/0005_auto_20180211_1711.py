# Generated by Django 2.0.1 on 2018-02-11 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_experience_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
