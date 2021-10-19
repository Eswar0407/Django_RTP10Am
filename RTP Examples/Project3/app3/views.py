from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def showIndex(request):
    return render(request,"index.html")


@csrf_exempt
def get_faculty_names(request):

    course = request.POST.get("course_name")
    print(course)

    if course == "Python":
        faculty_names = {1:"Ravi",2:"Kumar",3:"Mohan",4:"Murali"}
    elif course == "Java":
        faculty_names = {1:"Krishna",2:"Prasad"}
    else:
        faculty_names = {1:"Sorry Not Found"}

    return JsonResponse(faculty_names)
