from rest_framework import serializers
from myapp.models import Departments,Employees

class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Departments
		fields = ('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employees
		fields = ('EmployeeId','EmployeeName','Department','DateOfjoining','PhotoFileName')