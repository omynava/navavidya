# Generated by Django 3.0.3 on 2020-02-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('AB', 'Abacus'), ('VM', 'Vedic Mathematics'), ('QM', 'Quick Math'), ('UC', 'Unplug Coding'), ('PC', 'Python Club'), ('EE', 'Electrical and Electronics'), ('SC', 'Science Club'), ('MC', 'Math Club'), ('EC', 'English Club'), ('RO', 'Robotics'), ('CL', 'Cyber Literacy'), ('AI', 'Artificial Intelligence')], max_length=2)),
                ('label1', models.CharField(choices=[('TR', 'top rated'), ('BS', 'Bestseller')], max_length=2)),
                ('label2', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'All Level')], max_length=1)),
            ],
        ),
    ]
