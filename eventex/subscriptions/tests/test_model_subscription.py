from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Júnior',
            cpf='12345678901',
            email='joseadolfojr@gmail.com',
            phone='21996016875'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        '''Subscription must have an auto create_at'''
        self.assertIsInstance(self.obj.created_at, datetime)