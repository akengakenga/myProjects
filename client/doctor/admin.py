from django.contrib import admin
from .models import *
# Register your models here.


class DoctorTypeAdmin(admin.ModelAdmin):
    list_display = ('type_id','type_name')

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doc_id','doc_name','doc_phone','doc_birth','doc_type','doc_experience')

admin.site.register(Doctor,DoctorAdmin)
admin.site.register(DoctorType,DoctorTypeAdmin)