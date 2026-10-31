from django.contrib import admin
from .models import multipleVarient, FIRST_APP_CHOICE, ItemReview, Store, ItemCertificate


# Register your models here.

class ItemReviewInline(admin.TabularInline):
    model = ItemReview
    extra = 2

class multipleVarientAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ItemReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('item_details',)

class ItemCertificateAdmin(admin.ModelAdmin):
    list_display = ('item', 'certificate_number', 'valid_untill')
    




admin.site.register(multipleVarient, multipleVarientAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ItemCertificate, ItemCertificateAdmin)