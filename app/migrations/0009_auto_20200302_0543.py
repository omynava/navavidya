# Generated by Django 3.0.3 on 2020-03-02 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200302_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='level',
            field=models.CharField(choices=[('Level 1', 'Level 1'), ('Level 2', 'Level 2'), ('Level 3', 'Level 3'), ('Level 4', 'Level 4'), ('Level 5', 'Level 5'), ('Level 6', 'Level 6'), ('Level 6', 'Level 7'), ('Level 8', 'Level 8')], max_length=10),
        ),
    ]
