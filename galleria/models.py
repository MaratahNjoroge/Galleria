from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    # str representation of the object location
    def __str__(self):
        return self.name

    # save location
    def save_location(self):
        self.save()

    # delete location
    def delete_location(self):
        self.delete()

# a dictionary of some categories
# CATEGORIES = (
#     ( '1 ' 'Animals'),
#     ( '2 ' 'Sunsets'),
#     ( '3 ' 'Africa'),
#     ( '4 ' 'Vegetation'),
#     ( '5 ' 'Art'),
#     ( '6 ' 'Library'),
#     ( '7 ' 'Cars'),
#     ( '8 ' 'History'),
#     ( '9 ' 'Houses'),
#     ( '10 ' 'Travel'),
#     ( '11 ' 'Food'),
# )

class images(models.Model):
    name = models.CharField(max_length=30) 
    images_choices = models.CharField(max_length=10)

    # str representation of the object images
    def __str__(self):
        return self.name

    # save images
    def save_images(self):
        self.save()

    # delete images
    def delete_images(self):
        self.delete()


class Gallery(models.Model):
    image_name = models.CharField(max_length=40)
    image_description = models.CharField(max_length=40)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    images = models.ManyToManyField(images)
    image = models.ImageField(upload_to = 'photos/',blank=True)

    def __str__(self):
        return self.image_name

      # save gallery
    def save_gallery(self):
        self.save()

    # delete gallery
    def delete_gallery(self):
        self.delete()