from django.db import models
from mongoengine import *
from django.contrib.auth.models import User
import numpy as np
from django_google_maps import fields as map_fields

class Hotel(models.Model):
	#namehotel = models.CharField(max_length=60)
	name = models.CharField(max_length=60)
	add1 = models.CharField(max_length=50)
	add2 = models.CharField(max_length=50, null=True, blank=True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length= 2)
	zipcode = models.CharField(max_length=5)
	address = map_fields.AddressField(max_length=200)
	geolocation = map_fields.GeoLocationField(max_length=100, blank=True)

	def averagerating(self):
		all_ratings = map(lambda x: x.rating, self.review_set.all())
		return np.mean(all_ratings)

	def __str__(self):
		return self.name

    
		
class Review(models.Model):
	RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
	
	hotel = models.ForeignKey(Hotel, null=False, blank=False)
	user_name = models.CharField(max_length=25)
	date = models.DateTimeField('date')
	title = models.CharField(max_length= 50)
	description = models.TextField(max_length=5000)
	rating = models.IntegerField(choices=RATING_CHOICES)
