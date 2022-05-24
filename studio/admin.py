from django.contrib import admin

# Register your models here.
from .models import Photographer,Images,tags

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
    
admin.site.register(Photographer)
admin.site.register(Images)
admin.site.register(tags)
