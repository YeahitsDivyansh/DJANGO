from django.db import models
from django.utils import timezone  
from django.contrib.auth.models import User

# Create your models here.
class DjangoVariety(models.Model): 
    DJANGO_TYPE_CHOICE = [
        ('DJ', 'Django'),
        ('DF', 'Django Rest Framework'),
        ('DM', 'Django CMS'),
        ('DC', 'Django Channels'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField( upload_to='djangos/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(
        max_length=2,
        choices=DJANGO_TYPE_CHOICE,
        default='DJ',
    )
    description = models.TextField(default='')


    def __str__(self):
        return self.name
    
# One to Many relationship with User model
class DjangoReview(models.Model):
    django = models.ForeignKey(DjangoVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(default='')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.django.name} Review"
    

# Many to Many relationship with DjangoVariety
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    django_varieties = models.ManyToManyField(DjangoVariety, related_name='stores')
   
    def __str__(self):
        return self.name
    
# One to One relationship with DjangoVariety
class DjangoCertification(models.Model):
    django = models.OneToOneField(DjangoVariety, on_delete=models.CASCADE, related_name='certification')
    certification_number = models.CharField(max_length=100)
    date_issued = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f"For {self.django.name}"