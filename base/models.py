from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=13, null=True)



class Product(models.Model):
    SIZES = [
        ('0','small'),
        ('1','medium'),
        ('2','large'),
        ('3','X large'),
    ]
    title = models.CharField(max_length=127, null=True, blank=True)
    description = models.TextField(max_length=2047, null=True, blank=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    instock = models.BooleanField(null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    size = models.CharField(max_length=1, choices=SIZES, null=True)

    created = models.DateTimeField(auto_now=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, null=True)
    Expire = models.DateField(null=True)

    def __str__(self):
        return self.title + " " + str(self.price)


class Category(models.Model):
    title = models.CharField(max_length=127, null=True, blank=True)

    def __str__(self):
        return self.title

    pass


class Tag(models.Model):
    title = models.CharField(max_length=127, null=True, blank=True)

class Cart(models.Model):
    products = models.ManyToManyField('OrderedProduct')
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)



class OrderedProduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True)
    size = models.CharField(max_length=1, choices=Product.SIZES)












# class Book(models.Model):
#     title = models.CharField(max_length=127, null=True, blank=True)
#     description = models.TextField(max_length=2047, null=True, blank=True)
#     price = models.IntegerField(null=True)
#     # image = 
#     quantity = models.IntegerField(null=True)
#     instock = models.BooleanField(null=True)
#     rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)

#     Writer = models.ForeignKey('Writer', on_delete=models.SET_NULL, null=True)
#     publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)


# class Person(models.Model):
#     title = models.CharField(max_length=127, null=True, blank=True)
#     description = models.TextField(max_length=2047, null=True, blank=True)
#     price = models.IntegerField(null=True)
 

# class Writer(Person):
#     pass



# class Publisher(models.Model):
#     pass

# class BorrowedBook(models.Model):
#     book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
#     user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
#     BorrowDate = models.DateField(auto_now=True)
#     returned = models.BooleanField(default=False)

