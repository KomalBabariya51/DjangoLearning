from rest_framework import serializers
from .models import Login, Company, Employee


class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('name', 'email')


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        depth = 1


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
