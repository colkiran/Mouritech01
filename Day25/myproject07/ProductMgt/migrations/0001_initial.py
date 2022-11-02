# Generated by Django 4.1.2 on 2022-11-02 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Prodid", models.CharField(max_length=7, unique=True)),
                ("Prodname", models.CharField(max_length=50)),
                ("Category", models.CharField(max_length=25)),
                ("Prodtype", models.CharField(max_length=25)),
                ("Price", models.FloatField()),
            ],
        ),
    ]
