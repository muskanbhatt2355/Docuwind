# Generated by Django 2.2.5 on 2020-03-12 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
