# Generated by Django 4.0.6 on 2022-07-18 14:25

from django.db import migrations


def create_data(apps, schema_editor):
    Chatsun = apps.get_model('Chatsun', 'Chatsun')
    Chatsun(name="Dim", email="joe@email.com", document="22342342", phone="00000000").save()


class Migration(migrations.Migration):

    dependencies = [
        ('Chatsun', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
