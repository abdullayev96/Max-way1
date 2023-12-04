from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

    list_filter = ('id', 'created_at')
    search_fields = ("title",)



class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'cost', 'price', 'image')

    list_filter = ('id', 'created_at')
    search_fields = ("title",)



admin.site.register(Category,CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Customer)

