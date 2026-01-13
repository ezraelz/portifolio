from django.urls import path
from .views import track_view, total_views

urlpatterns = [
    path('track-view/', track_view),
    path('total-view/', total_views),
]
