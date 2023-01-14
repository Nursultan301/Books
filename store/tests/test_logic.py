from django.test import TestCase

from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(2, 3, '+')
        self.assertEqual(5, result)

    def test_minus(self):
        result = operations(3, 3, '-')
        self.assertEqual(0, result)

    def test_multiply(self):
        result = operations(3, 3, '*')
        self.assertEqual(9, result)