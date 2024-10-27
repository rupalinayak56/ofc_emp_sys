from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class Role(models.Model):
    name=models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name

class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()

    def __str__(self):
        return self.first_name
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    clock_in = models.TimeField(null=True, blank=True)
    clock_out = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee.user.username} - {self.date}"