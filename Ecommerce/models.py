from django.db import models
from django.utils import timezone
import uuid
# Create your models here.


class Category(models.Model):
    uid = models.CharField(unique=True, max_length=255, blank=True, null=True, default=uuid.uuid4)
    name = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    image = models.FileField(upload_to='categories/%Y/%m/%d/', default=None)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'category'


class Product(models.Model):
    uid = models.CharField(unique=True, max_length=255, blank=True, null=True, default=uuid.uuid4)
    name = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)
    tags = models.CharField(max_length=512, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    in_stock = models.BooleanField(default=True)
    quantity = models.IntegerField(blank=True, null=True)
    image = models.FileField(upload_to='products/%Y/%m/%d/', default=None)
    subcategory = models.ForeignKey('Subcategory', models.DO_NOTHING, db_column='subcategory', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'product'

class Subcategory(models.Model):
    uid = models.CharField(unique=True, max_length=255, blank=True, null=True, default=uuid.uuid4)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    image = models.FileField(upload_to='sub_categories/%Y/%m/%d/', default=None)
    category = models.ForeignKey(Category, models.CASCADE, db_column='category', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'subcategory'


class User(models.Model):

    uid = models.CharField(unique=True, max_length=255, blank=True, null=True, default=uuid.uuid4)
    firstname = models.CharField(max_length=256, blank=False, null=False, default="")
    name = models.CharField(max_length=256, blank=False, null=False, default="")
    email = models.CharField(max_length=256, blank=False, null=False, default="")
    password = models.CharField(max_length=512, blank=False, null=False, default="")
    phone = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'
