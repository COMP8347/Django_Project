# Import necessary classes
from django.http import HttpResponse
from .models import Topic, Course, Student, Order
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    course_list = Course.objects.all().order_by('-price')[:5]
    response = HttpResponse()
    heading1 = '<p>' + 'List of Courses: ' + '</p>'
    response.write(heading1)
    for course in course_list:
        para = '<p>'+ str(course.id) + '. ' + str(course) + ' Price: ' + str(course.price)  + ' | Course Availability: ' +\
            '<a style="color:#008080"><b>'+ \
               ('This Course is For Everyone!'
                if (course.for_everyone == True)
                else
                'This Course is Not For Everyone!') +\
            '</b></a></p>'
        response.write(para)
    return response

def about(request):
    response = HttpResponse()
    heading1 = '<p><a style="color:#008080"><b>' + "This is an E-learning Website!Search our Topics to find all available Courses." + '</b></a></p>'
    response.write(heading1)
    return response

def detail(request, top_no):
    response = HttpResponse()
    course = Course.objects.filter(topic__id__contains = top_no)
    if(len(course) >0):
        para = '<p>The topic found is: ' + str(course.first().topic.category) + '' + '</p>'
        response.write(para)
        response.write('</br><p>The Course List is as follows - </p>')
        response.write('<ul>')
        for item in course:
            list = '<li>' + str(item.name) + '</li>'
            response.write(list)
        response.write('</ul>')
        return response
    else:
        return get_object_or_404(Course, topic_id=top_no)
