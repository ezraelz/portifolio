from django.urls import path
from .views import submit_contact,get_data,collect_email

urlpatterns = [
    path('contact/', submit_contact, name='submit_contact'),
    path('info/', get_data, name='get_info'),
    path('emails/', collect_email, name='get_email'),
]

