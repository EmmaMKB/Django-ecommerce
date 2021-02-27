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
