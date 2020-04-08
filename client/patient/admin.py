from django.contrib import admin
from .models import *
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('p_id','p_name','p_gender','p_phone','p_address')
class PatientStatusAdmin(admin.ModelAdmin):
    list_display = ('status_id','status_name')

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('reg_id','reg_patient','reg_type','reg_time')
admin.site.register(Patient,PatientAdmin)
admin.site.register(PatientStatus,PatientStatusAdmin)
admin.site.register(Register,RegisterAdmin)