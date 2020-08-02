from django.contrib import admin
from .models import Location, Gallery, images

class GalleryAdmin(admin.ModelAdmin):
    filter_horizontal =('images',)

# Register your models here.
admin.site.register(Location)
admin.site.register(Gallery)
admin.site.register(images)