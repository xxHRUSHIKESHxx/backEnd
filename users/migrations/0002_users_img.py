# Generated by Django 5.0.2 on 2024-02-29 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='img',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
