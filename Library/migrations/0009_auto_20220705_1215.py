# Generated by Django 3.0.5 on 2022-07-05 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0008_remove_adminprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=100),
        ),
    ]