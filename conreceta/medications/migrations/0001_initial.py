# Generated by Django 3.2.15 on 2022-08-24 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('selling_condition', models.CharField(max_length=255)),
            ],
        ),
    ]
