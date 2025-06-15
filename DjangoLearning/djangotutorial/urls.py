from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_django, name='all_django'),
    path('<int:django_id>/', views.django_detail, name='django_detail'),
]
 