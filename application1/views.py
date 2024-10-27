from django.shortcuts import render
from application1.models import *
from application1.forms import *
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
#employee navbar
def employee(request):
    return render(request,'employee.html')

def all_emp(request):
    d={'emps':Employee.objects.all()}
    return render(request,'all_emp.html',d)

def add_emp(request):
    EEMFO=EmployeeModelForm()
    d={'EEMFO':EEMFO}
    if request.method=='POST':
        EMFO=EmployeeModelForm(request.POST)
        EMFO.save()
        return HttpResponse('New Employee Added Successfully')
    return render(request,'add_emp.html',d)

def remove_emp(request,id=0):
    if id:
        try:
            empremove=Employee.objects.get(id=id)
            empremove.delete()
            return HttpResponse('Emplyee Removed Successfully')
        except:
            return HttpResponse('Please Enter A Valid EmpId')
    d={'emps':Employee.objects.all()}
    return render(request,'remove_emp.html',d)

def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains = name ) | Q(last_name__icontains = name))
        if role:
            emps=emps.filter(role__name = role)

        d={'emps':emps}
        return render(request,'all_emp.html',d)
    return render(request,'filter_emp.html')
#department navbar
def departments(request):
    return render(request,'departments.html')
def all_dept(request):
    d={'depts':Department.objects.all()}
    return render (request,'all_dept.html',d)
def add_dept(request):
    EDMFO=DepartmentModelForm()
    d={'EDMFO':EDMFO}
    if request.method=='POST':
        DMFO=DepartmentModelForm(request.POST)
        DMFO.save()
        return HttpResponse('Department added Successfully')
    return render(request,'add_dept.html',d)
def remove_dept(request,id=0):
    if id:
        try:
            deptremove=Department.objects.get(id=id)
            deptremove.delete()
            return HttpResponse('Department remove successfully')
        except:
            return HttpResponse('Please return valid dept id')
    d={'depts':Department.objects.all()}
    return render(request,'remove_dept.html',d)