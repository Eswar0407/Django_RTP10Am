from rest_framework.serializers import ModelSerializer
from app7.models import EmployeeModel
from rest_framework import serializers
class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = "__all__"

    def validate_salary(self,salary):
        if salary > 5000.00:
          return salary
        else:
          raise serializers.ValidationError("Minimum Salary Is 5000.00")










