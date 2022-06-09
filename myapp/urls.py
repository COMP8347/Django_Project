from django.urls import path
from myapp import views
app_name = 'myapp'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'about', views.about),
    path(r'<int:top_no>', views.detail)
]