from django.db import models


class User(models.Model):
    class Meta:
        pass

    username = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=16, default='', null=True, blank=True)


class Product(models.Model):
    class Meta:
        pass

    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=16, default='', null=True, blank=True)
    desc = models.TextField(default='', null=True, blank=True)
    on_shelf = models.BooleanField(default=True)
