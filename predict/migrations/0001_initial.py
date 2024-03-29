# Generated by Django 3.1.2 on 2020-12-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('Patient_ID', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('Patient_Age', models.IntegerField()),
                ('Patient_Gender', models.IntegerField()),
                ('Patient_Blood_Pressure', models.IntegerField()),
                ('Patient_Heartrate', models.IntegerField()),
                ('Heart_Disease', models.CharField(max_length=30)),
            ],
        ),
    ]
