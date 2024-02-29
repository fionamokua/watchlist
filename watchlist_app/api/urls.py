from django.urls import path
from .views import StreamingPlartformAV,WatchDetailAV,WatchListAV,StreamingPlartformDetailAV
urlpatterns = [
    path('list/',WatchListAV.as_view(),name="movie_list"),
    path("<int:pk>/",WatchDetailAV.as_view(),name="movie_details"),
    path("stream/",StreamingPlartformAV.as_view(),name="stream"),
    path("stream/<int:pk>/",StreamingPlartformDetailAV.as_view(),name="streamdetail"),
]
