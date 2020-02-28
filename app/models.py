from django.db import models

CATEGORY_CHOICES = (
    ('AB', 'Abacus'),
    ('VM', 'Vedic Mathematics'),
    ('QM', 'Quick Math'),
    ('UC', 'Unplug Coding'),
    ('PC', 'Python Club'),
    ('EE', 'Electrical and Electronics'),
    ('SC', 'Science Club'),
    ('MC', 'Math Club'),
    ('EC', 'English Club'),
    ('RO', 'Robotics'),
    ('CL', 'Cyber Literacy'),
    ('AI', 'Artificial Intelligence')
)

LABEL1_CHOICES = (
    ('TR', 'top rated'),
    ('BS', 'Bestseller')
)

LABEL2_CHOICES = (
    ('B', 'Beginner'),
    ('I', 'Intermediate'),
    ('A', 'All Level')
)


class Course(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label1 = models.CharField(choices=LABEL1_CHOICES, max_length=2)
    label2 = models.CharField(choices=LABEL2_CHOICES, max_length=1)

    def __str__(self):
        return self.title
