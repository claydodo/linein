from django.db import models


class User(models.Model):
    class Meta:
        pass

    username = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=16, default='', null=True, blank=True)

    def __str__(self):
        return self.username


class Product(models.Model):
    class Meta:
        pass

    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=16, default='', null=True, blank=True)
    desc = models.TextField(default='', null=True, blank=True)
    on_shelf = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    class Meta:
        pass

    id = models.CharField(max_length=32, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return self.id
