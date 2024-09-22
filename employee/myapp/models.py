from django.db import models

class Departments(models.Model):
	DepartmentId = models.CharField(max_length=10)
	DepartmentName = models.CharField(max_length=200)

class Employees(models.Model):
	EmployeeId = models.CharField(max_length=10)
	EmployeeName = models.CharField(max_length=20)
	Department = models.CharField(max_length=30)
	DateOfjoining = models.CharField(max_length=10)
	PhotoFileName = models.CharField(max_length=500)