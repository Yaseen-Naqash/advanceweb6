from django.contrib import admin
from .models import Product, Category, Tag, OrderedProduct, Cart, User
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(OrderedProduct)
admin.site.register(Cart)
admin.site.register(User)

