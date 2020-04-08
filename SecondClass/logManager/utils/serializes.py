from rest_framework import serializers
from logManager.models import *


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admins
        fields = '__all__'
        depth = 1


class ChargerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chargers
        fields = '__all__'
        depth = 1

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
        depth = 4


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = '__all__'
        depth = 3


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'
        depth = 2


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Majors
        fields = '__all__'
        depth = 1


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'