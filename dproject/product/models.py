from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Access(models.Model):
    access = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.product.id)


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.FileField(upload_to='filesInput/')
    duration = models.IntegerField()  # Длительность видео
    last_look_date = models.DateTimeField(default=datetime.now())
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title


class Statistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    less = models.ForeignKey(Lesson, on_delete=models.PROTECT)
    viewing_time = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.status)

