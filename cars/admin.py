from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius: 50% "/>'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'

    list_display = ('id', 'thumbnail', 'car_title', 'city', 'state', 'color', 'model', 'year', 'body_style', 'is_featured', 'fuel_type', 'vin_number')
    list_display_links = ('id', 'car_title', 'thumbnail')
    list_editable = ('is_featured',)
    search_fields = ('city', 'state', 'year', 'body_style', 'color', 'model')
    list_filter = ('city', 'state', 'year', 'color')

admin.site.register(Car, CarAdmin)
