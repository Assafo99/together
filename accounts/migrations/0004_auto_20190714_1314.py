# Generated by Django 2.2.1 on 2019-07-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190714_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(upload_to='profile_pics/'),
        ),
    ]
