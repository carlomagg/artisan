# Generated by Django 3.1.1 on 2020-10-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bwari', models.CharField(max_length=100)),
                ('dutse', models.CharField(max_length=100)),
                ('kubwa', models.CharField(max_length=100)),
                ('garki', models.CharField(max_length=11)),
                ('wuse', models.CharField(max_length=100)),
                ('gwarinpa', models.CharField(max_length=100)),
                ('maitama', models.CharField(max_length=100)),
                ('apo', models.CharField(max_length=100)),
                ('jabi', models.CharField(max_length=100)),
                ('utako', models.CharField(max_length=100)),
                ('wuye', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
