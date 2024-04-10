from django.shortcuts import render, get_object_or_404
from .models import Review



def reviews(request):
    context = {
    "reviews" : Review.objects.all()
    }

    return render(request,"reviews.html")
