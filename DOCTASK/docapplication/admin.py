from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','phone',)
admin.site.register(User,UserAdmin)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('owner','created_time','type','source_type','source_id',)

admin.site.register(Document,DocumentAdmin)
# Register your models here.
