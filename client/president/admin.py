from django.contrib import admin
from .models import *
# Register your models here.

class PresidentAdmin(admin.ModelAdmin):
    list_display = ('pre_id','pre_name')

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('type_id','type_name')

admin.site.register(President,PresidentAdmin)
admin.site.register(UserType,UserTypeAdmin)