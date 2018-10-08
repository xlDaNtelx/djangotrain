from django.conf.urls import url
from django.contrib import admin
from .views import (
    MessageListAPIView,
    MessageSingleAPIView,
    MessageUpdateAPIView,
    MessageDestroyAPIView,
)

urlpatterns = [
    url(r'^$', MessageListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', MessageSingleAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', MessageUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', MessageDestroyAPIView.as_view(), name='delete'),
]