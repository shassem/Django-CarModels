from django.db import models
from django.urls.base import reverse

# Create your models here.

class Car(models.Model):
    mod = models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    production_year=models.IntegerField(default=2022)

    def __str__(self):
        return f"{self.mod}"


    @classmethod
    def get_all_cars(cls):
        return cls.objects.all()

    def get_show_url(self):
        return reverse("cars.show", args=[self.id])

    def get_edit_url(self):
        return reverse("cars.edit", args=[self.id])

    def get_delete_url(self):
        return reverse("cars.delete", args=[self.id])