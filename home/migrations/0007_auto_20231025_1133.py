# Generated by Django 2.1.15 on 2023-10-25 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20231025_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointment',
            name='depname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Department'),
        ),
    ]