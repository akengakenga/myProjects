from django.contrib import admin
from .models import *
# Register your models here.
class TreatAdmin(admin.ModelAdmin):
    list_display = ('treat_id','patient','register','doctor','treat_problem','treat_time')

admin.site.register(Treat,TreatAdmin)