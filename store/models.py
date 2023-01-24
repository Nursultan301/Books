from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField("Называние", max_length=100)
    price = models.DecimalField("Цена", max_digits=7, decimal_places=2)
    author_name = models.CharField("Автор", max_length=50)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_books',
                              verbose_name="Владелец")
    readers = models.ManyToManyField(User, through='UserBookRelation', related_name='books')

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.name


class UserBookRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Incredible'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f'{self.user.username}: {self.book}, RATE {self.rate}'
