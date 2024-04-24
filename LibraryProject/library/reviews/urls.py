from django.urls import path
from .views import *
from django.views.generic.list import ListView

urlpatterns = [
    path('rev/',reviews, name='reviews'),
   # path('rev/',List.as_view(model=Review, tepmlate_name="reviews.html"),

]