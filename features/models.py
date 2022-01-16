from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categorie"

class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductFields(models.Model):
    quality = models.BooleanField(default=False)
    temper = models.BooleanField(default=False)
    dimensions = models.BooleanField(default=False)
    grade = models.BooleanField(default=False)
    specification_number = models.BooleanField(default=False)
    quantity = models.BooleanField(default=False)
    coating_in_gsm = models.BooleanField(default=False)
    color = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Product Field"
