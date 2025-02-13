# Generated by Django 5.0.4 on 2024-04-18 13:44

import django.db.models.deletion
import properties.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Property",
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
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="Property Brand"),
                ),
                ("built_in", models.BooleanField(default=False)),
                (
                    "is_featured",
                    models.BooleanField(
                        default=False, verbose_name="Add to Home Page?"
                    ),
                ),
                ("address", models.CharField(max_length=200)),
                ("unit_number", models.CharField(blank=True, max_length=50, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("state", models.CharField(blank=True, max_length=50, null=True)),
                ("postal_code", models.CharField(blank=True, max_length=10, null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField(verbose_name="Property Description")),
                (
                    "tag",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Property Tag",
                    ),
                ),
                ("bedrooms", models.PositiveIntegerField()),
                (
                    "bathrooms",
                    models.DecimalField(decimal_places=2, default=1, max_digits=5),
                ),
                ("year_built", models.PositiveIntegerField()),
                ("interior_sqft", models.PositiveIntegerField()),
                ("lot_size", models.PositiveIntegerField()),
                (
                    "youtube_video_id",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=200, unique=True, verbose_name="Url Slug"
                    ),
                ),
                (
                    "priority",
                    models.PositiveIntegerField(
                        blank=True,
                        default=None,
                        null=True,
                        verbose_name="Property Order",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BuiltInProperty",
            fields=[],
            options={
                "verbose_name": "Built-In Property",
                "verbose_name_plural": "Built-In Properties",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("properties.property",),
        ),
        migrations.CreateModel(
            name="PropertyImage",
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
                (
                    "image",
                    models.ImageField(
                        upload_to=properties.models.property_image_directory_path
                    ),
                ),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="properties.property",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PropertyOrder",
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
                ("order", models.PositiveIntegerField()),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ordered_properties",
                        to="properties.property",
                    ),
                ),
                (
                    "related_property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="properties.property",
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.AddField(
            model_name="property",
            name="properties",
            field=models.ManyToManyField(
                related_name="related_properties",
                through="properties.PropertyOrder",
                to="properties.property",
            ),
        ),
    ]
