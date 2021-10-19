from django.shortcuts import render
from app_Provider.models import EmployeeModel
from django.http import JsonResponse,HttpResponse
from django.core.serializers import serialize
import json
from app_Provider.forms import EmployeeForm

# this function need to get  all the records from database and
# convert into json to string and send the response in json format

def view_all_Employees(request):
    # emps = EmployeeModel.objects.all()

    #all_employees = []
    #for employee in emps:
     #   all_employees.append({"idno":employee.idno,
      #                        "name":employee.name,
       #                       "salary":employee.salary})
    #return JsonResponse(data=all_employees,safe=False)

    emps = EmployeeModel.objects.all()
    json_string = serialize(format="json",queryset=emps)
    #return JsonResponse(data=json_string,safe=False)
    return HttpResponse(json_string,content_type="application/json")


def view_one_Employee(request,emp_id):
     try:
         # reading the one employee data from employee model
         #emp = EmployeeModel.objects.get(idno=emp_id)
         # Converting Tuple object to Dict Data
         #json_string = {"idno":emp.idno,"name":emp.name,"salary":emp.salary}
         #return JsonResponse(data=json_string).

        emp = EmployeeModel.objects.get(idno=emp_id)
        json_string = {"id":emp.idno,"name":emp.name,"salary":emp.salary}
        return JsonResponse(data=json_string)
     except EmployeeModel.DoesNotExist:
         #raise ValueError("Please Check Your Employee ID")
         return JsonResponse(data={"error":"Please Check Your Employee ID"})


def addoneEmployee(request):
    json_string = json.loads(request.body)
    emp = EmployeeForm(json_string)
    if emp.is_valid():
        emp.save()
        return HttpResponse(json.dumps({"message":"Employee Saved"}),content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error": "Employee not Saved"}),content_type="application/json")


def updateEmployee(request,emp_id):
   try:
    old_employee = EmployeeModel.objects.get(id =emp_id)
    new_employee = json.loads(request.body)
    ef = EmployeeForm(new_employee,instance=old_employee)
    if ef.is_valid():
        ef.save()
        return HttpResponse(json.dumps({"message":"Employee Updated"}),content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error":"Student not Upadated"}),content_type="application/json")
   except EmployeeModel.DoesNotExist:
       return JsonResponse(data={"error":"Sorry!!! Wrong Employee ID"})

def deleteEmployee(request,emp_id):
    try:
        result = EmployeeModel.objects.get(id=emp_id).delete()
        if result[0] == 1:
            json_data = json.dumps({"message":"Employee is Deleted"})
            return HttpResponse(json_data,content_type="application/json")
    except EmployeeModel.DoesNotExist:
         return JsonResponse(data={"error":"Sorry!!!! Wrong Employee ID"})