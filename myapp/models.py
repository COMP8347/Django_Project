from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class Topic(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, null=False, blank=False, default='Development')

    def __str__(self):
        return  self.name + ' - Course Name | Category: ' + self.category

class Course(models.Model):
    topic = models.ForeignKey(Topic, related_name='courses', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    for_everyone = models.BooleanField(default=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    # interested = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name + ' - Course Name'  + ' | Topic Name: ' + self.topic.name + ' | Description: ' + self.description

class Student(User):
    CITY_CHOICES = [('WS', 'Windsor'),
    ('CG', 'Calgery'),
    ('MR', 'Montreal'),
    ('VC', 'Vancouver')]
    school = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='WS')
    interested_in = models.ManyToManyField(Topic)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ,School ' + self.school + ', City ' + self.city

class Order(models.Model):
    VALID_CHOICES = [
        (0, 'Cancelled'),
        (1, 'Confirmed')
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    levels = models.PositiveIntegerField(default=1)
    order_status = models.IntegerField(choices=VALID_CHOICES, default=1)
    order_date = models.DateField(default=timezone.now)

    def __str__(self):
        return 'Order # ' + str(self.id) + ': For ' + str(self.course.name) + '(s) by ' + str(self.student)

    def total_cost(self):
        return self.course.price * self.order_status

