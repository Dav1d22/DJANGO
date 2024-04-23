# Generated by Django 5.0.3 on 2024-04-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="articulo",
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
                ("nombre", models.CharField(max_length=30)),
                ("seccion", models.CharField(max_length=20)),
                ("precio", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="cliente",
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
                ("nombre", models.CharField(max_length=30)),
                ("direccion", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=30)),
                ("telefono", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="pedido",
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
                ("numero", models.IntegerField()),
                ("fecha", models.DateField()),
                ("entregado", models.BooleanField()),
            ],
        ),
    ]
