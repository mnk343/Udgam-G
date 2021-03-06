# Generated by Django 2.1.5 on 2019-01-20 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20190119_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='doctor'),
        ),
        migrations.AddField(
            model_name='patient',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='patient'),
        ),
    ]
