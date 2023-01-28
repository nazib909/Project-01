from django.db import models

# Create your models here.


class Category(models.Model):
    c_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.c_name)


class Products(models.Model):
    p_name = models.CharField(max_length=45)
    price = models.FloatField()
    p_price = models.FloatField()
    decription = models.TextField(max_length=500)
    quantity = models.PositiveIntegerField(default=1)
    p_pic = models.ImageField(upload_to='product_pic', null=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.p_name
