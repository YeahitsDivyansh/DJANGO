from django.shortcuts import render
from .models import DjangoVariety

# Create your views here.
def all_django(request):
    all_djangos= DjangoVariety.objects.all()
    return render(request, 'djangolearning/all_djlearning.html', 
                  {'all_djangos': all_djangos})