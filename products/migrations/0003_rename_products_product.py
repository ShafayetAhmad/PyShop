# Generated by Django 4.1.6 on 2023-02-09 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_offer"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Products",
            new_name="Product",
        ),
    ]
