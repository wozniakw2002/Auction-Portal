from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import datetime
from datetime import timedelta
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    auction = models.ForeignKey('Auction', on_delete=models.SET_NULL, null=True)
    picture = models.ImageField()

    def __str__(self) -> str:
        return self.name

class Auction(models.Model):
    host = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    start_price = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10000)])
    min_bid = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    last_bid = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    duration = models.DateTimeField(default=datetime.datetime.now() + timedelta(days=7))
    has_ended = models.BooleanField(default=False, editable=False)
    current_price = models.IntegerField(editable=False, default=1)

    def save(self, *args, **kwargs):
        if not self.id:
            self.current_price = self.start_price
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    user =  models.ForeignKey(User, on_delete = models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete = models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.comment[0:50]