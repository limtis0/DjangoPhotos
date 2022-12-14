# Generated by Django 4.1.2 on 2022-10-26 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('albumId', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=7, null=True)),
                ('url', models.CharField(max_length=2048)),
            ],
        ),
    ]
