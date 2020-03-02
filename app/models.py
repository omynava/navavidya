from django.db import models
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('Abacus', 'Abacus'),
    ('Vedic Mathematics', 'Vedic Mathematics'),
    ('Quick Math', 'Quick Math'),
    ('Unplug Coding', 'Unplug Coding'),
    ('Python Club', 'Python Club'),
    ('Electrical and Electronics', 'Electrical and Electronics'),
    ('Science Club', 'Science Club'),
    ('Math Club', 'Math Club'),
    ('English Club', 'English Club'),
    ('Robotics', 'Robotics'),
    ('Cyber Literacy', 'Cyber Literacy'),
    ('Artificial Intelligence', 'Artificial Intelligence')
)

LABEL1_CHOICES = (
    ('Top Rated', 'top rated'),
    ('Bestseller', 'Bestseller')
)

LABEL2_CHOICES = (
    ('Level 1', 'Level 1'),
    ('Level 2', 'Level 2'),
    ('Level 3', 'Level 3'),
    ('Level 4', 'Level 4'),
    ('Level 5', 'Level 5'),
    ('Level 6', 'Level 6'),
    ('Level 7', 'Level 7'),
    ('Level 8', 'Level 8')
)


class Course(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)
    label1 = models.CharField(choices=LABEL1_CHOICES, max_length=20)
    label2 = models.CharField(choices=LABEL2_CHOICES, max_length=20)

    def __str__(self):
        return self.title


LEVEL_CHOICES = (
    ('Level 1', 'Level 1'),
    ('Level 2', 'Level 2'),
    ('Level 3', 'Level 3'),
    ('Level 4', 'Level 4'),
    ('Level 5', 'Level 5'),
    ('Level 6', 'Level 6'),
    ('Level 6', 'Level 7'),
    ('Level 8', 'Level 8')
)


class Category(models.Model):
    title = models.CharField(max_length=100)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=10)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:category", kwargs={
            'slug': self.slug
        })


