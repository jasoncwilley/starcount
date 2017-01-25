from django.contrib import admin
from hotelsite.models import Review, Hotel

from django.contrib import admin

from hotelsite.models import Hotel, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('name', 'rating', 'user_id', 'description', 'date')
    list_filter = ['date', 'user_id']
    search_fields = ['description']
    
admin.site.register(Hotel)
admin.site.register(Review, ReviewAdmin)

