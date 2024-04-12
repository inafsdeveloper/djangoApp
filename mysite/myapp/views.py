from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Course
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return HttpResponse("Hello")


def loadData(request):
    # Opening JSON file
    f = open('courses.json')

    # Load JSON object as an dictionary
    courses = json.load(f)
    # Adding all courses to the database
    for course in courses:
        # Creating a new Course
        new_course = Course(title=course['title'], author=course['author'], overview=course['overview'],
                            image=course['img'], url=course['url'])
        print('before')
        # Adding course to database
        new_course.save()
        print('after')
        print(new_course)
    # Closing File
    f.close()
    # Success Message
    return HttpResponse('Data Loaded Successfully')


def listData(request):
    course = Course.objects.all()
    print(len(course))
    return render(request, 'courses_view.html', {'course': course})
