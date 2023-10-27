# Generated by Django 2.1.15 on 2023-10-21 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20231021_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookappointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=200)),
                ('pphone', models.CharField(max_length=10)),
                ('pemail', models.EmailField(max_length=254)),
                ('bookingdate', models.DateField()),
                ('bookingon', models.DateField(auto_now=True)),
                ('docname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Doctors')),
                ('paddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Department')),
            ],
        ),
    ]
