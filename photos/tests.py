from django.test import TestCase
from .models import Location,Category,Image
import datetime as dt

class LocationTestClass(TestCase):
    def setUp(self):
        self.Nairobi= Location(location='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.Nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

