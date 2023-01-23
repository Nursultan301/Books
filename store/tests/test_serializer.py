from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        self.user = User.objects.create(username='test_username')
        book_1 = Book.objects.create(name='Test book 1', price=1000, author_name='Author 1', owner=self.user)
        book_2 = Book.objects.create(name='Test book 2', price=2000, author_name='Author 2', owner=self.user)
        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price': '1000.00',
                'author_name': 'Author 1',
                "owner": book_1.owner.id
            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '2000.00',
                'author_name': 'Author 2',
                "owner": book_2.owner.id

            },
        ]
        self.assertEqual(expected_data, data)
