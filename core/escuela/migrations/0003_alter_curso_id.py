# Generated by Django 4.0.2 on 2022-06-15 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
