# Generated by Django 5.1.3 on 2024-11-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=50)),
                ('voice_id', models.CharField(max_length=50, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
