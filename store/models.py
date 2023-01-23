from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField("Называние", max_length=100)
    price = models.DecimalField("Цена", max_digits=7, decimal_places=2)
    author_name = models.CharField("Автор", max_length=50)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Владелец")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.name
