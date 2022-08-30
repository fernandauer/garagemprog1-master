# Generated by Django 4.1 on 2022-08-24 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_editora"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carro",
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
                ("modelo", models.CharField(max_length=50)),
                ("ano", models.IntegerField(blank=True, null=True)),
                ("cor", models.CharField(blank=True, max_length=50, null=True)),
                ("preco", models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Marca",
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
                ("nome", models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name="Editora",
        ),
        migrations.AlterField(
            model_name="categoria",
            name="descricao",
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name="carro",
            name="categoria",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="carros",
                to="core.categoria",
            ),
        ),
        migrations.AddField(
            model_name="carro",
            name="marca",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="carros",
                to="core.marca",
            ),
        ),
    ]
