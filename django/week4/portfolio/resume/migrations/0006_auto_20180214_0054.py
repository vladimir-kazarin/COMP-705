# Generated by Django 2.0.1 on 2018-02-14 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20180211_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='experience',
            name='company',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='experience',
            name='title',
            field=models.CharField(max_length=64),
        ),
        migrations.AddField(
            model_name='experience',
            name='parent_resume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='resume.Resume'),
        ),
    ]
