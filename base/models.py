from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=127, null=True, blank=True)
    description = models.TextField(max_length=2047, null=True, blank=True)
    price = models.IntegerField(null=True)
    # image = 
    quantity = models.IntegerField(null=True)
    instock = models.BooleanField(null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title + " " + str(self.price)


class Category(models.Model):
    title = models.CharField(max_length=127, null=True, blank=True)

    def __str__(self):
        return self.title

    pass

