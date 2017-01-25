from django.conf.urls import url
from hotelsite import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', (TemplateView.as_view(template_name="home.html"))),
	url(r'^reviews$', views.review_list, name='review_list'),
    url(r'^reviewdetails/(?P<review_id>[0-9]+)/$', views.reviewdetails, name='reviewdetails'),
    url(r'^hotels$', views.hotels, name='hotels'),
    url(r'^hoteldetails/(?P<hotel_id>[0-9]+)/$', views.add_review, name='hoteldetails'),
	url(r'^hotel/(?P<hotel_id>[0-9]+)/$', views.hoteldetails),
    url(r'^hotel/(?P<hotel_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]
