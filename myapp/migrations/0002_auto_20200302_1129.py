# Generated by Django 2.2.7 on 2020-03-02 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bmi',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='weight',
            field=models.FloatField(),
        ),
    ]