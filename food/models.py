from django.db import models
from baseapp.models import BaseModel

class Category(BaseModel):
    title = models.CharField(null=False, blank=False, max_length=100)
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = "Kategoriyalar"



class Product(BaseModel):
    title = models.CharField(null=False, blank=False, max_length=100)
    description = models.TextField(null=False, blank=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    cost = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='products')
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = "Mahsulotlar"


class Customer(BaseModel):
    first_name = models.CharField(null=False, blank=False,max_length=100)
    last_name = models.CharField(null=False, blank=False,max_length=100)
    phone_number = models.CharField(null=False, unique=True ,blank=False,max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Mijoz'
        verbose_name_plural = "Mijozlar"


class Order(BaseModel):
    payment_type = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(null=False, blank=True, default=1)
    address = models.CharField(null=False, blank=False, max_length=250)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)



    class Meta:
        verbose_name = 'Sotib oluvchi'
        verbose_name_plural = "Sotib oluvchilar"



class OrderProduct(BaseModel):
    count = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)


    class Meta:
        verbose_name = "Sotib_oluvchi_mahsulotlari"