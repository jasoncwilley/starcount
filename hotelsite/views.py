from django.shortcuts import get_object_or_404, render
from .models import Review, Hotel

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import ReviewForm
import datetime

def review_list(request):
    review_list = Review.objects.order_by('-date')[:5]
    context = {'review_list':review_list}
    return render(request, 'review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})


def hotel_list(request):
    hotel_list = Hotel.objects.order_by('-name')
    context = {'hotel_list':hotel_list}
    return render(request, 'hotel_list.html', context)


def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'hotel_detail.html', {'hotel': hotel})


def add_review(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        description = form.cleaned_data['description']
        #user_name = form.cleaned_data['user_name']
        user_name = request.user.username
        review = Review()
        review.hotel = hotel
        review.user_name = user_name
        review.rating = rating
        review.description = description
        review.date = datetime.datetime.now()
        review.name = review.hotel
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('hotelsite:hotel_detail', args=(hotel.id,)))

    return render(request, 'hotel_detail.html', {'hotel': hotel, 'form': form})


def user_review_list(request, username=None):
    if not username:
        username = request.user.username
        review_list = Review.objects.filter(user_name=username).order_by('-date')
        context = {'review_list':review_list, 'username':username}
        return render(request, 'hotelsite/review/user.id', context)
        
def registration_form(request):
    return render(request, 'registration_form.html')
