__all__ = ['User', 'Tag', 'Product', 'OrderProductEntry', 'Order', 'Entity']

from django.db import models


class User(models.Model):
    class Meta:
        pass

    username = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=16, default='', null=True, blank=True)

    def __str__(self):
        return self.username


class Tag(models.Model):
    class Meta:
        pass

    name = models.CharField(max_length=16, primary_key=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        pass

    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=16, default='', null=True, blank=True)
    desc = models.TextField(default='', null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='products', blank=True)
    on_shelf = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class OrderProductEntry(models.Model):
    class Meta:
        pass

    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='product_entries')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_entries')
    count = models.IntegerField(default=1)

    def __str__(self):
        return "{}: {} x{}".format(self.order, self.product, self.count)


class Order(models.Model):
    class Meta:
        pass

    id = models.CharField(max_length=32, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, related_name='orders', through=OrderProductEntry, blank=True)

    def __str__(self):
        return self.id


class Entity(models.Model):
    class Meta:
        pass

    id = models.CharField(max_length=32, primary_key=True)
    subs = models.ManyToManyField('self', related_name='parents', blank=True)

    def __str__(self):
        return self.id