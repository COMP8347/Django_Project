from django import forms
from django.http import HttpResponse

from myapp.models import Order


class InterestForm(forms.Form):
    interested = forms.ChoiceField(widget=forms.RadioSelect, choices=[
            (1, "True"),
            (0, "False"),
        ])

    # interested = forms.Select(choices=)
    level = forms.IntegerField(min_value=1)
    comments = forms.CharField(widget=forms.Textarea)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('course', 'student', 'levels', 'order_date')
        widgets = {
            'student': forms.RadioSelect,
            'order_date': forms.SelectDateWidget
        }

