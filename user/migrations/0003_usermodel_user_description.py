# Generated by Django 3.2.3 on 2021-05-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_usermodel_work_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='user_description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
