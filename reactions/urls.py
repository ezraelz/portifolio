from django.urls import path
from .views import (
    ReactionView,
)

urlpatterns = [
    path('reactions/', ReactionView.as_view(), name='reactions'),
]
