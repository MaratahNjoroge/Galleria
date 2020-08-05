from django.test import TestCase
from django.test import TestCase
from .models import Location,Gallery,images
import datetime as dt

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kenya= Location(name = 'kenya')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kenya,Location))

     # Testing Save Method
    def test_save_method(self):
        self.kenya.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class GalleryTestClass(TestCase):

    def setUp(self):
        # Creating a new location and saving it
        self.kenya= Location(first_name = 'Kenya', last_name ='Muriuki', email ='kenya@moringaschool.com')
        self.kenya.save_location()

        # Creating a new image and saving it
        self.new_image = images(name = 'testing')
        self.new_image.save()

        self.new_gallery= Gallery(title = 'Test Gallery',post = 'This is a random test Post',location = self.kenya)
        self.new_gallery.save()

        self.new_gallery.images.add(self.new_image)

    def tearDown(self):
        Location.objects.all().delete()
        images.objects.all().delete()
        Gallery.objects.all().delete()

    

   