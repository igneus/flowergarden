from flowers.models import *
from django.contrib import admin
import django.contrib.auth.models
import django.contrib.auth.admin

class FlowerInline(admin.StackedInline):
    model = Flower
    extra = 3

class BouquetAdmin(admin.ModelAdmin):
    inlines = [FlowerInline]
    
    list_display = ('receiver', 'sender', 'given')
    
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False
    
class UserAdmin(django.contrib.auth.admin.UserAdmin):
    inlines = [UserProfileInline]

admin.site.register(FlowerType)
admin.site.register(Bouquet, BouquetAdmin)

admin.site.unregister(django.contrib.auth.models.User)
admin.site.register(django.contrib.auth.models.User, UserAdmin)
