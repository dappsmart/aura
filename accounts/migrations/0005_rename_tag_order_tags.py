# Generated by Django 4.1.3 on 2022-12-20 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_tag_order_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='tag',
            new_name='tags',
        ),
    ]
