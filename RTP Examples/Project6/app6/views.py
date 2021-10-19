from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from app6.serializers import EmployeeSerializer
from app6.models import EmployeeModel
from django.views.generic import View

# Create your views here.
def addEmployee(request):
    #reading data from request in bytes format
    b_data = request.body

    #converting binary data into stremed data
    s_data = io.BytesIO(b_data)

    #converting stremed data to dict_data
    dict_data = JSONParser().parse(s_data)

    es = EmployeeSerializer(data=dict_data)

    if es.is_valid():
        es.save()
        message = {"messages":"Employee Saved"}
    else:
        message = {"error":es.errors}

    #converting dict_data to Json
    json_data = JSONRenderer().render(message)
    return HttpResponse(json_data,content_type="application/json")


class AllEmployees(View):
    def get(self,request):
        all = EmployeeModel.objects.all()
        es = EmployeeSerializer(all,many=True)
        json_data = JSONRenderer().render(es.data)
        return HttpResponse(json_data,content_type="application/json")

class Employee(View):
    #to read all employee's (or) for 1 Employee
    def get(self,request):
        b_data = request.body
        s_data = io.BytesIO(b_data)
        dict_data = JSONParser().parse(s_data)
        idno = dict_data.get("idno",None)

        if idno:
            try:
                data = EmployeeModel.objects.get(idno=idno)
                es = EmployeeSerializer(data)
                return HttpResponse(JSONRenderer().render(es.data),content_type="application/json")
            except EmployeeModel.DoesNotExist:
                message = {"Sorry!!! Wrong IDNO"}
                return HttpResponse(JSONRenderer().render(message),content_type="application/json")
        else:
            all = EmployeeModel.objects.all()
            es = EmployeeSerializer(all,many=True)
            json_data = JSONRenderer().render(es.data)
            return HttpResponse(json_data,content_type="application/json")
