# Generated by Django 5.0 on 2024-04-01 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_work', '0019_alter_collectionrequest_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserGarbageBin',
        ),
    ]
