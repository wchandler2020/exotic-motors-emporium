from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    # to control if and which fields in list_display should be linked to the “change” page for an object.
    list_display = ('id', 'first_name', 'last_name', 'email', 'car_title', 'city', 'create_date')
    # to a list of field names on the model which will allow editing on the change list page
    list_display_links = ('id', 'first_name', 'last_name')
    # adds search functionality to the admin section, when a search is initiated these the fields that will be searched
    search_fields = ('first_name', 'last_name', 'email', 'car_title')
    #number of items on a page
    list_per_page = 25

#allows the objects in the model/db to be visualized in the user admin
admin.site.register(Contact, ContactAdmin)
