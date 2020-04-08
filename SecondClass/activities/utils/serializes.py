from rest_framework import serializers
from activities.models import *
from logManager.utils.serializes import *

class ActiviyTypeSerializer(serializers.ModelSerializer):
     class Meta:
        model = ActivityTypes
        fields = '__all__'

class ActiviySerializer(serializers.ModelSerializer):
    activity_status = serializers.CharField(source='get_activity_status_display')
    class Meta:
        model = Activities
        fields = ['activity_id','activity_name','activity_description','activity_address','activity_start_time','activity_end_time','activity_credit','activity_status','activity_type','creater_id','activity_img','activity_max_size','activity_attend_size','charger','creater']
        depth = 3


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


class StudentActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StuedntActivity
        fields = '__all__'
        depth = 5

