# Generated by Django 2.2.1 on 2019-07-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190721_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]