from django.contrib import admin
from travelapp.models import Places,Book

# Register your models here.
class PlacesAdmin(admin.ModelAdmin):
    
    list_display=['State','Package','Days','Image','Start_date','End_date','Hotel_name','Description','created_on']
    
class BookAdmin(admin.ModelAdmin):
    
    list_display=['pid','uid','phn_no','passenger','book_date']

admin.site.register(Places,PlacesAdmin)
admin.site.register(Book,BookAdmin)