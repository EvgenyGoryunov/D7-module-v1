# Generated by Django 4.0 on 2022-01-04 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_alter_appoint_idpkid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appoint',
            name='idpkid',
        ),
        migrations.AddField(
            model_name='appoint',
            name='idpkid',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
