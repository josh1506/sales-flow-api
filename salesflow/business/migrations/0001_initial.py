# Generated by Django 4.1.9 on 2023-06-25 07:39

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
            name="Business",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField(auto_now=True)),
                ("date_modified", models.DateTimeField()),
                (
                    "assistant_manager",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assistant_manager_business",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "manager",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="manager_business",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owned_business",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_created",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_business",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_deleted",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="deleted_business",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_updated",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="updated_business",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
