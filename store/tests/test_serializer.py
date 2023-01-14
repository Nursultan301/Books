from django.test import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test book 1', price=1000)
        book_2 = Book.objects.create(name='Test book 2', price=2000)
        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price': '1000.00'
              },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '2000.00'
            },
        ]
        self.assertEqual(expected_data, data)
