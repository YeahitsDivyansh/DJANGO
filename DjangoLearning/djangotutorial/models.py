from django.db import models
from django.utils import timezone   

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


    def __str__(self):
        return self.name