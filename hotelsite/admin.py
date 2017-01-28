from django.contrib import admin
from .models import Hotel, Review
from django_google_maps.widgets import GoogleMapsAddressWidget
from django_google_maps.fields import AddressField, GeoLocationField
from django.forms.widgets import TextInput

class HotelAdmin(admin.ModelAdmin):
	formfield_overrides = {
		AddressField: {'widget': GoogleMapsAddressWidget},
		GeoLocationField: {'widget': TextInput(attrs={'readonly': 'readonly'})},
	}




class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('hotel', 'rating', 'user_name', 'description', 'date')
    list_filter = ['date', 'user_name']
    search_fields = ['description']
    

admin.site.register(Review, ReviewAdmin)
admin.site.register(Hotel, HotelAdmin)
