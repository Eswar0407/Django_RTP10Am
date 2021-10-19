import json

from django.shortcuts import render
import requests
from requests.exceptions import ConnectionError
from django.http import HttpResponse
import json
# Create your views here.

def showIndex(request):
    try :
       response = requests.get('http://127.0.0.1:8888/view_all_employees')
       json_string = response.text
       dict_data = json.loads(json_string)
       return render(request,'index.html',{"data":dict_data})
    except ConnectionError:
        return HttpResponse("Sorry!!!! Server is Not Active")
