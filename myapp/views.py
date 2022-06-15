# Import necessary classes
from django.http import HttpResponse
from .models import Topic, Course, Student, Order
from django.shortcuts import get_object_or_404
from django.shortcuts import render
# Create your views here.

def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index0.html', {'top_list': top_list})

def about(request):
    return render(request, 'myapp/about0.html')


def detail(request, top_no):
    course = Course.objects.filter(topic__id__contains = top_no)
    if(len(course) >0):
        return render(request, 'myapp/detail0.html', {'course': course})
    else:
        return get_object_or_404(Course, topic_id=top_no)
