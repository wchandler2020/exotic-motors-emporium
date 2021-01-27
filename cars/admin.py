from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):

    #allows the use of a thumbnail in the admin section
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius: 50% "/>'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'
    #control which fields are displayed on the change list page of the admin.
    list_display = ('id', 'thumbnail', 'car_title', 'city', 'state', 'color', 'model', 'year', 'body_style', 'is_featured', 'fuel_type', 'vin_number')
    # to control if and which fields in list_display should be linked to the “change” page for an object.
    list_display_links = ('id', 'car_title', 'thumbnail')
    #to a list of field names on the model which will allow editing on the change list page
    list_editable = ('is_featured',)
    #adds search functionality to the admin section, when a search is initiated these the fields that will be searched
    search_fields = ('city', 'state', 'year', 'body_style', 'color', 'model')
    #allows lists in the admin sections to listed/prioritized by the following fields.
    list_filter = ('city', 'state', 'year', 'color')
#allows the objects in the model/db to be visualized in the user admin
admin.site.register(Car, CarAdmin)
