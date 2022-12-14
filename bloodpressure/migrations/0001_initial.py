# Generated by Django 4.1 on 2022-08-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloodpressure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systolic', models.IntegerField(max_length=3)),
                ('diastolic', models.IntegerField(max_length=3)),
                ('pulse', models.IntegerField(max_length=3)),
                ('data', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
    ]
