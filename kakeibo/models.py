from django.db import models

# Create your models here.
class ICategory(models.Model):
    name = models.CharField(unique=True, max_length=20)
    discription = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Income(models.Model):
    date = models.DateField()
    category = models.ForeignKey(ICategory, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    memo = models.TextField(max_length=200, null=True, blank=True)


class ECategory(models.Model):
    name = models.CharField(unique=True, max_length=20)
    discription = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    date = models.DateField()
    category = models.ForeignKey(ECategory, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    memo = models.TextField(max_length=200, null=True, blank=True)