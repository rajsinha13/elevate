# Generated by Django 3.0.3 on 2020-02-12 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='teamdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeofcompany', models.CharField(max_length=50)),
                ('insti_name', models.CharField(max_length=50)),
                ('pl1', models.CharField(max_length=50)),
                ('phone1', models.IntegerField(default=0)),
                ('email1', models.TextField(max_length=100)),
                ('pl2', models.CharField(max_length=50)),
                ('phone2', models.IntegerField(default=0)),
                ('email2', models.TextField(max_length=100)),
                ('pl3', models.CharField(max_length=50)),
                ('phone3', models.IntegerField(default=0)),
                ('email3', models.TextField(max_length=100)),
                ('pl4', models.CharField(max_length=50)),
                ('phone4', models.IntegerField(default=0)),
                ('email4', models.TextField(max_length=100)),
                ('pl5', models.CharField(max_length=50)),
                ('phone5', models.IntegerField(default=0)),
                ('email5', models.TextField(max_length=100)),
                ('pl6', models.CharField(max_length=50)),
                ('phone6', models.IntegerField(default=0)),
                ('email6', models.TextField(max_length=100)),
                ('pl7', models.CharField(max_length=50)),
                ('phone7', models.IntegerField(default=0)),
                ('email7', models.TextField(max_length=100)),
                ('pl8', models.CharField(max_length=50)),
                ('phone8', models.IntegerField(default=0)),
                ('email8', models.TextField(max_length=100)),
                ('pl9', models.CharField(max_length=50)),
                ('phone9', models.IntegerField(default=0)),
                ('email9', models.TextField(max_length=100)),
                ('pl10', models.CharField(max_length=50)),
                ('phone10', models.IntegerField(default=0)),
                ('email10', models.TextField(max_length=100)),
                ('pl11', models.CharField(max_length=50)),
                ('phone11', models.IntegerField(default=0)),
                ('email11', models.TextField(max_length=100)),
                ('pl12', models.CharField(max_length=50)),
                ('phone12', models.IntegerField(default=0)),
                ('email12', models.TextField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
