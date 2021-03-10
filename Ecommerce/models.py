from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import uuid
from .managers import CustomUserManager


class Basket(models.Model):
    uid = models.CharField(unique=True, max_length=255, blank=True, null=True, default=uuid.uuid4)
    user = models.ForeignKey('Person', models.CASCADE, db_column='user', blank=False, null=False)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    is_ordered = models.BooleanField(blank=True, null=True, default=False)

    class Meta:
        db_table = 'basket'


class Category(models.Model):
    uid = models.CharField(unique=True, max_length=255, blank=True, null=True, default=uuid.uuid4)
    name = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    image = models.FileField(upload_to='categories/%Y/%m/%d/', default=None)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class Newsletter(models.Model):
    uid = models.CharField(max_length=255, blank=True, null=True, default=uuid.uuid4)
    email = models.CharField(max_length=256, blank=True, null=True)
    registered_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    is_active = models.BooleanField(blank=True, null=True, default=True)

    class Meta:
        db_table = 'newsletter'


class Order(models.Model):
    uid = models.CharField(max_length=255, blank=True, null=True, default=uuid.uuid4)
    reference_code = models.CharField(max_length=256, blank=True, null=True)
    user = models.ForeignKey('Person', models.CASCADE, db_column='user', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    state = models.CharField(max_length=128, blank=True, null=True)
    payment_method = models.CharField(max_length=128, blank=False, null=False, default="")
    total = models.FloatField(blank=True, null=True)
    basket = models.ForeignKey(Basket, models.DO_NOTHING, db_column='basket', blank=True, null=True)
    shipping_details = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'order'


class Product(models.Model):
    uid = models.CharField(unique=True, max_length=255, blank=True, null=True, default=uuid.uuid4)
    banner = models.FileField(upload_to='banner/%Y/%m/%d/', default=None)
    name = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)
    tags = models.CharField(max_length=512, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    in_stock = models.BooleanField(default=True)
    quantity = models.IntegerField(blank=True, null=True)
    image = models.FileField(upload_to='products/%Y/%m/%d/', default=None)
    subcategory = models.ForeignKey('Subcategory', models.DO_NOTHING, db_column='subcategory', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    @property
    def tags_list(self):
        return self.tags.split(",")

    class Meta:
        db_table = 'product'


class ProductToBasket(models.Model):

    uid = models.CharField(max_length=255, blank=True, null=True, default=uuid.uuid4)
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='product', blank=True, null=True)
    user = models.ForeignKey('Person', models.CASCADE, db_column='user', blank=True, null=True)
    basket = models.ForeignKey(Basket, models.DO_NOTHING, db_column='basket', blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    is_valid = models.BooleanField(blank=True, null=True, default=True)
    added_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    class Meta:
        db_table = 'product_to_basket'


class Subcategory(models.Model):
    uid = models.CharField(unique=True, max_length=255, blank=True, null=True, default=uuid.uuid4)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    image = models.FileField(upload_to='sub_categories/%Y/%m/%d/', default=None)
    category = models.ForeignKey(Category, models.CASCADE, db_column='category', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subcategory'


class Person(AbstractUser):

    username = None
    uid = models.CharField(unique=True, max_length=255, blank=True, null=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=32, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = "users"


class Wishlist(models.Model):
    uid = models.CharField(max_length=255, blank=True, null=True, default=uuid.uuid4)
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='product', blank=True, null=True)
    user = models.ForeignKey('Person', models.CASCADE, db_column='user', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    is_active = models.IntegerField(blank=True, null=True, default=True)

    class Meta:
        db_table = 'wishlist'
