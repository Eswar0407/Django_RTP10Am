from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def showIndex(request):
    return render(request, 'index.html')

@csrf_exempt
def get_faculty_names(request):
    course = request.POST.get("course_name")
    print(course)

    if course == "Python":
        faculty_names = {1:"Naveen",2:"Eswar",3:"Hima",4:"Bhaskar"}
    elif course == "Java":
        faculty_names = {1:"Sunny",2:"Raghu",3:"Swapna",4:"Bindu"}
    else:
        faculty_names = {1:"Sorry Not Found"}

    return JsonResponse(faculty_names)