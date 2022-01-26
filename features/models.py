from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categorie"


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sub Categorie"



class Product(models.Model):
    name = models.CharField(max_length=30)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE , null = True)

    quality = models.BooleanField(default=False)
    temper = models.BooleanField(default=False)
    dimensions = models.BooleanField(default=False)
    grade = models.BooleanField(default=False)
    specification_number = models.BooleanField(default=False)
    quantity = models.BooleanField(default=False)
    coating_in_gsm = models.BooleanField(default=False)
    color = models.BooleanField(default=False)



    def __str__(self):
        return self.name


