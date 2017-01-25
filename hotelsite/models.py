from django.db import models
from mongoengine import *
from django.contrib.auth.models import User
import numpy as np


class Hotel(models.Model):
	#namehotel = models.CharField(max_length=60)
	name = models.CharField(max_length=60)
	user = models.ForeignKey(User, null=False, blank=False)		
	add1 = models.CharField(max_length=50)
	add2 = models.CharField(max_length=50, null=True, blank=True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length= 2)
	zipcode = models.CharField(max_length=5)

	def average_rating(self):
		all_ratings = map(lambda x: x.rating, self.review_set.all())
		return np.mean(all_ratings)

	def __str__(self):
		return self.name

class Review(models.Model):
	rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
	#hotelname = models.ForeignKey(User, null=False, blank=False)
	user = models.ForeignKey(User, null=False, blank=False)	
	name = models.ForeignKey(Hotel, null=False, blank=False)	
	date = models.DateTimeField()	
	title = models.CharField(max_length= 50)
	description = models.TextField(max_length=5000)
	rating = models.IntegerField(choices=rating)
