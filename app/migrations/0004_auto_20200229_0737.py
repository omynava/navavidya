# Generated by Django 3.0.3 on 2020-02-29 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200229_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='label3',
            new_name='label',
        ),
    ]
