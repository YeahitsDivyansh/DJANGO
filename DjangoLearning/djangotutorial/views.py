from django.shortcuts import render
from .models import DjangoVariety, Store
from django.shortcuts import get_object_or_404
from .forms import DjangoVarietyForm

# Create your views here.
def all_django(request):
    all_djangos= DjangoVariety.objects.all()
    return render(request, 'djangolearning/all_djlearning.html', 
                  {'all_djangos': all_djangos})

def django_detail(request, django_id):
    django = get_object_or_404(DjangoVariety, pk=django_id)
    return render(request, 'djangolearning/django_detail.html', {'django': django})

def django_store_view(request):
    stores = None
    if request.method == 'POST':
        form = DjangoVarietyForm(request.POST)
        if form.is_valid():
            django_variety = form.cleaned_data['django_variety']
            stores = Store.objects.filter(django_varieties=django_variety)

    else:
        form = DjangoVarietyForm()
    return render(request, 'djangolearning/django_stores.html', {'stores': stores, 'form':form})