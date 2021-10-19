from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView

from rest_framework.views import APIView
from rest_framework.response import Response
from app7.models import EmployeeModel
from app7.serializers import EmployeeSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
# Create your views here.
#class ViewAllEmployees(APIView):
    #def get(self,request):
       #emp = EmployeeModel.objects.get(idno=1)
       #emp = {"idno":101,"name":"Eswar1","salary":150000}
       #return Response(emp)

class ViewAllEmployees(APIView):
    #used to read all employees info
    def get(self,request):
        query_set = EmployeeModel.objects.all()
        es = EmployeeSerializer(query_set,many=True)
        return Response(es.data)

    #used to insert a employee
    def post(self,request):
        b_data = request.data
        es = EmployeeSerializer(data=b_data)
        if es.is_valid():
            es.save()
            return Response({"message":"Employee Saved"})
        else:
            return Response({"error":es.errors})

class DeleteEmployee(APIView):
     #used to delete a employee
     def delete(self,request,employee_id):
        res = EmployeeModel.objects.filter(idno=employee_id).delete()
        if res[0]:
           return Response({"message":"Employee Deleted"})
        else:
            return Response({"error":"Sorry!!! Employee Not Found"})


class EmployeeOperations(ViewSet):
    def list(self, request):
        query_set = EmployeeModel.objects.all()
        es = EmployeeSerializer(query_set, many=True)
        return Response(es.data)

    def create(self, request):
        b_data = request.data
        es = EmployeeSerializer(data=b_data)
        if es.is_valid():
            es.save()
            return Response({"message": "Employee Saved"})
        else:
            return Response({"error": es.errors})

    def destroy(self, request, pk=None):
        res = EmployeeModel.objects.filter(idno=pk).delete()
        if res[0]:
            return Response({"message": "Employee Deleted"})
        else:
            return Response({"error": "Sorry!!! Employee Not Found"})

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

class EmployeeOpe(ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeCreateAPIView(CreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeListAPIView(ListAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveAPIView(RetrieveAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = ['idno', 'name']