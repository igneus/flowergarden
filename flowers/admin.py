from flowers.models import *
from django.contrib import admin

class FlowerInline(admin.StackedInline):
    model = Flower
    extra = 3

class BouquetAdmin(admin.ModelAdmin):
    inlines = [FlowerInline]
    
    list_display = ('receiver', 'sender', 'given')

admin.site.register(User)
admin.site.register(Bouquet, BouquetAdmin)