# Generated by Django 4.2.7 on 2023-11-23 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_client_team_alter_client_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('name',)},
        ),
    ]