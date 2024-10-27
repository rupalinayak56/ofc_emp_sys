from application1.models import *
from django import forms

class DepartmentModelForm(forms.ModelForm):
    class Meta():
        model=Department
        fields='__all__'

class RoleModelForm(forms.ModelForm):
    class Meta():
        model=Role
        fields='__all__'

class EmployeeModelForm(forms.ModelForm):
    class Meta():
        model=Employee
        fields='__all__'

