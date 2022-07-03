# Import necessary classes
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import OrderForm, InterestForm
from .models import Topic, Course, Student, Order
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'top_list': top_list})


def about(request):
    return render(request, 'myapp/about.html')


def detail(request, top_no):
    course = Course.objects.filter(topic__id__contains=top_no)
    if (len(course) > 0):
        return render(request, 'myapp/detail.html', {'course': course})
    else:
        return get_object_or_404(Course, topic_id=top_no)


def courses(request):
    courlist = Course.objects.all().order_by('id')
    return render(request, 'myapp/courses.html', {'courlist': courlist})


def place_order(request):
    msg = ''
    courlist = Course.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.levels <= order.course.stages:
                order.save()
                msg = 'Your course has been ordered successfully.'
                # Call Discount
                if order.course.price >= 150:
                    print(order.course.price)
                    order.course.discount()
                    print(order.course.price)
                    order.course.save()

            else:
                msg = 'You exceeded the number of levels for this course.'
            return render(request, 'myapp/order_response.html', {'msg': msg})
    else:
        form = OrderForm()
    return render(request, 'myapp/placeorder.html', {'form': form, 'msg': msg, 'courlist': courlist})


def coursedetail(request, cour_id):
    msg = ''
    cour = Course.objects.filter(id=cour_id).get()
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            # Check Interest
            if form.cleaned_data['interested'] == '1':
                msg = 'Your interest has been recorded.'
                print(cour.interested)
                cour.interested += 1
                cour.save()
                print(cour.interested)
            else:
                msg = 'You are not interested, got it'
            print(msg)
            return redirect('../../myapp/')
    else:
        form = InterestForm()
    return render(request, 'myapp/coursedetail.html', {'form': form, 'cour': cour})

def user_login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'myapp/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(('myapp:index')))

def myaccount(request):
    user
    # Student = Student.objects.filter