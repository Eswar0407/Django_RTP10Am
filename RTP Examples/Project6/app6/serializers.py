from rest_framework import serializers
from app6.models import EmployeeModel


def validate_name(name):
    if len(name) > 3:
      return name
    else:
        raise serializers.ValidationError("Wrong Number")
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[validate_name])
    fee = serializers.FloatField()

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[validate_name])
    salary = serializers.FloatField()

    def validate_salary(self,salary):
        if salary >= 10000.00:
            return salary
        else:
            raise serializers.ValidationError("Min salary is 10000.00")


    def create(self, validated_data):
        return EmployeeModel.objects.create(**validated_data)