# Generated by Django 4.1.7 on 2023-04-03 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_alter_places_end_date_alter_places_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('uid', models.IntegerField()),
                ('phn_no', models.IntegerField()),
                ('passenger', models.IntegerField()),
                ('book_date', models.DateTimeField()),
            ],
        ),
    ]
