# Generated by Django 4.1.5 on 2024-04-17 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_work', '0030_alter_user_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttable',
            name='reason',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
