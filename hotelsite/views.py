from django.shortcuts import get_object_or_404, render
from hotelsite.models import Review, Hotel
import mongoengine


def review_list(request):
    review_list = Review.objects.order_by('-date')[:10]
    context = {'review_list':review_list}
    return render(request, 'hotelsite/reviews.html', context)

def reviewdetails(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'hotelsite/reviewdetails.html', {'review': review})

def hotels(request):
    hotels = Hotel.objects.order_by('-hotels')
    context = {'hotels':hotels}
    return render(request, 'hotelsite/hotels.html', context)


def hoteldetails(request, hotel_id):
    hotelname = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'hotelsite/hoteldetails.html', {'hotelname': hotelname})

def add_review(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['description']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.hotel = hotel
        review.user_name = user_name
        review.rating = rating
        review.description = description
        review.date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('hotelsite:hoteldetails', args=(hotel.id,)))

    return render(request, 'hotelsite/hoteldetails.html', {'hotel': hotel, 'form': form})
