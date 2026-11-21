from django.contrib import admin
from .models import Product, Category, Tag, OrderedProduct, Cart, User
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(OrderedProduct)
admin.site.register(User)

class OrderedProductInline(admin.TabularInline):
    model = OrderedProduct
    extra = 0
    pass


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_filter = ['size', 'category', 'instock']
    list_display = ['title', 'price', 'category']
    list_editable = ['price']


    readonly_fields = ['title']
    # exclude = ['quantity']
    fieldsets = (
        ('اطلاعات محصول',{
            'fields': ['title', 'description', 'discount']
        }),
        ('اطلاعات انبار داری',{
            'fields':['quantity', 'instock', 'price'],
            'classes': ['collapse']

        }),
        ('متا',{
            'fields':['image']
        }),

    )




admin.site.register(Product, ProductAdmin)

admin.site.site_header = 'پنل مدیریت املاک'
admin.site.site_title = 'مدیریت املاک'
admin.site.index_title = 'به پنل مدیریت خوش آمدید'

class CartAdmin(admin.ModelAdmin):
    inlines = [OrderedProductInline]
    pass
admin.site.register(Cart, CartAdmin)
