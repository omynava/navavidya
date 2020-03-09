from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save


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
        return reverse("app:course", kwargs={
            'slug': self.slug
        })



    # def create_slug(instance, new_slug=None):
    #     slug = slugify(instance.titile)
    #
    #     if new_slug is not None:
    #         slug = new_slug
    #         qs = Course.objects.filter(slug=slug).order_by("-id")
    #         exists =qs.exists()
    #         if exists:
    #             new_slug = "%s-%s"%(slug, qs.first().id)
    #             return create_slug(instance, new_slug=new_slug)
    #         return slug
    #
    #     def pre_save_course_receiver(sender, instance, *args, **kwargs):
    #         if not instance.slug:
    #             instance.slug = create_slug(instance)
    # pre_save.connect(pre_save_course_receiver, Course)


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
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)
    label1 = models.CharField(choices=LABEL1_CHOICES, max_length=20)
    label2 = models.CharField(choices=LABEL2_CHOICES, max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("app:course-detail", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("app:add-to-cart", kwargs={
            'slug': self.slug
        })


class OrderCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.course.title}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    course = models.ManyToManyField(OrderCourse)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)






