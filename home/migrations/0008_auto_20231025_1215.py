# Generated by Django 2.1.15 on 2023-10-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20231025_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='Qualification',
            new_name='qualification',
        ),
        migrations.AddField(
            model_name='doctors',
            name='docimage',
            field=models.ImageField(blank=True, null=True, upload_to='docimage/'),
        ),
    ]
