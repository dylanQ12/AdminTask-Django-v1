# Generated by Django 5.0.6 on 2024-05-15 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_customuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.TextField(null=True),
        ),
    ]
