from django.urls import path
from .views import Inquiry

urlpatterns = [
    #url path for user inquiries
    path('inquiry', Inquiry, name='inquiry'),
]