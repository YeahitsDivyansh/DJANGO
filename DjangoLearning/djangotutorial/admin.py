from django.contrib import admin
from .models import DjangoVariety, DjangoReview, Store, DjangoCertification

# Register your models here.
class DjangoReviewInline(admin.TabularInline):
    model = DjangoReview
    extra = 2

class DjangoVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [DjangoReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('django_varieties',)

class DjangoCertificationAdmin(admin.ModelAdmin):
    list_display = ('django', 'certification_number', 'date_issued', 'valid_until')

admin.site.register(DjangoVariety, DjangoVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(DjangoCertification, DjangoCertificationAdmin)