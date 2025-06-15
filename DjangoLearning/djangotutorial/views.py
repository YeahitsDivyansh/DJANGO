from django.shortcuts import render
from .models import DjangoVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_django(request):
    all_djangos= DjangoVariety.objects.all()
    return render(request, 'djangolearning/all_djlearning.html', 
                  {'all_djangos': all_djangos})

def django_detail(request, django_id):
    django = get_object_or_404(DjangoVariety, pk=django_id)
    return render(request, 'djangolearning/django_detail.html', {'django': django})