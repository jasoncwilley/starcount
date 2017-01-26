from django.contrib import admin
from hotelsite.models import Review, Hotel


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('hotel', 'rating', 'user_name', 'description', 'date')
    list_filter = ['date', 'user_name']
    search_fields = ['description']
    
admin.site.register(Hotel)
admin.site.register(Review, ReviewAdmin)

