# Generated by Django 5.1.6 on 2025-03-08 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("join_api_app", "0010_remove_contact_first_name_remove_contact_last_name"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Subtasks",
        ),
    ]
