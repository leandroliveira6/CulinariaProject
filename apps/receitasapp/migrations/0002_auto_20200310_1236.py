# Generated by Django 3.0.4 on 2020-03-10 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitasapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='creation_date',
            field=models.DateField(auto_now=True),
        ),
    ]
