# Generated by Django 3.1.3 on 2020-11-13 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_bipmobike_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicycle',
            name='qr_code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
