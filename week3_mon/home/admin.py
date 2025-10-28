from django.contrib import admin
from .models import *
# Register your models here.
class blogcustom(admin.ModelAdmin):
    list_display = ('title','content','created_at',)
    list_editable =('content',)
    list_per_page = 4 

admin.site.register(Blog,blogcustom),