# Generated by Django 5.1.6 on 2025-03-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("join_api_app", "0003_contact_initials"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasks",
            name="assignedTo",
            field=models.ManyToManyField(
                blank=True, related_name="contactsAssignedTo", to="join_api_app.contact"
            ),
        ),
        migrations.CreateModel(
            name="ContactList",
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
                    "contact",
                    models.ManyToManyField(
                        related_name="contacts", to="join_api_app.contact"
                    ),
                ),
            ],
        ),
    ]
