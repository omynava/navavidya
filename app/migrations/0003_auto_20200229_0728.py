# Generated by Django 3.0.3 on 2020-02-29 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_course_levels'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('label3', models.CharField(choices=[('1', 'Level 1'), ('2', 'Level 2'), ('3', 'Level 3'), ('4', 'Level 4'), ('5', 'Level 5'), ('6', 'Level 6'), ('6', 'Level 7'), ('8', 'Level 8')], max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='levels',
        ),
    ]
