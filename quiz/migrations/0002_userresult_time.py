# Generated by Django 3.2.3 on 2021-06-03 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresult',
            name='time',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]