# Generated by Django 2.0.1 on 2018-01-30 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=300, null=True, verbose_name='FIO')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('INN', models.PositiveSmallIntegerField(null=True, verbose_name='INN')),
                ('OGRN', models.PositiveSmallIntegerField(null=True, verbose_name='OGRN')),
            ],
        ),
        migrations.CreateModel(
            name='OrgType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=10, verbose_name='ShortName')),
                ('full_name', models.CharField(max_length=300, verbose_name='FullName')),
            ],
        ),
    ]