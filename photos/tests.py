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

class CategoryTestClass(TestCase):
    def setUp(self):
        self.Travel= Category(category='Travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.Travel,Category))

    def tearDown(self):
        Category.objects.all().delete()

    def test_save_method(self):
        self.Travel.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

        
