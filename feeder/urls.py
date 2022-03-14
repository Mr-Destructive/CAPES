from django.urls import path
from .views import FeedFetch

urlpatterns = [
        path('', FeedFetch.as_view(), name='getfeed'),
        ]
