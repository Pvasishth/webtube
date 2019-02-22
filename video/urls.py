from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', VideoListView.as_view(), name='home-view'),
    url(r'^(?P<pk>[-\w]+)/$', VideoDetailView.as_view(), name='video-detail'),

]
