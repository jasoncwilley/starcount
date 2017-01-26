from django.conf.urls import url
from hotelsite import views

urlpatterns = [

    url(r'^$', views.review_list, name='review_list'),
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    url(r'^hotel$', views.hotel_list, name='hotel_list'),
    url(r'^hotel/(?P<hotel_id>[0-9]+)/$', views.hotel_detail, name='hotel_detail'),
    url(r'^hotel/(?P<hotel_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    url(r'^hotelsite/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    url(r'^hotelsite/user/$', views.user_review_list, name='user_review_list'),
]
