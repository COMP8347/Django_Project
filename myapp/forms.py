from django import forms
from django.http import HttpResponse

from myapp.models import Order

class InterestForm(forms.Form):
    response = HttpResponse
    response.write('<form action = "/your-name/" method = "post">')

    response.write('<label> Interested: </label>')
    response.write('<label for ="interested_1"> Yes </label >')
    response.write('<input type = "radio" id = "interested_1" value = "1" >')
    response.write('< label for ="interested_0" > No < / label >')
    response.write('< input type = "radio" id = "interested_0" value = "0" >')

    response.write('<label for ="level"> Levels: </label>')
    response.write('<input type = "number" id = "level" min = "1" value="1" required>')

    response.write('<label for ="comments"> Additional Comments: </label>')
    response.write('<textarea id = "comments"></textarea>')

    response.write('</form>')
    response.write('< input type = "submit" value = "OK" >')

    # return response