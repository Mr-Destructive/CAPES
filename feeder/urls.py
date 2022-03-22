from django.urls import path
from .views import ( 
        FeedFetch, FeedView, AddFeed, DeleteFeed, EditFeed,
        PublicationFeedView, FeedListView 
        )

urlpatterns = [
        path('', FeedView.as_view(), name='feedlist'),
        path('fetch/', FeedFetch.as_view(), name='fetchfeed'),
        path('create/', AddFeed.as_view(), name='createfeedlink'),
        path('publications/', FeedListView.as_view(), name='publicationlist'),
        path('get/<str:pub_name>', PublicationFeedView.as_view(), name='publicationfeed'),

        path('<pk>/delete/', DeleteFeed.as_view(), name="deletefeedlink"),
        path('<pk>/update/', EditFeed.as_view(), name="updatefeedlink"),
        ]
