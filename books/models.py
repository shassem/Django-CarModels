from django.db import models
from django.urls.base import reverse

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    desc= models.CharField(max_length=100)
    no_of_pages = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"


    @classmethod
    def get_all_books(cls):
        return cls.objects.all()

    def get_show_url(self):
        return reverse("books.show",args=[self.id])

    def get_edit_url(self):
        return reverse("books.edit",args=[self.id])


    def get_delete_url(self):
        return reverse("books.delete",args=[self.id])
