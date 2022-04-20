# Generated by Django 4.0.3 on 2022-04-18 11:01

from django.db import migrations, models
import django.db.models.deletion
import filiere.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
                ('adress', models.CharField(max_length=100, null=True)),
                ('telephone', models.CharField(max_length=20, null=True)),
                ('logo', models.ImageField(upload_to=filiere.models.upload_location)),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_filiere', models.CharField(max_length=30)),
                ('logo', models.ImageField(upload_to=filiere.models.upload_location)),
                ('etablissement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='filiere.etablissement')),
            ],
        ),
    ]
