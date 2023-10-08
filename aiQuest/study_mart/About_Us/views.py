from django.http import HttpResponse
from django.shortcuts import render

from About_Us.models import Teachers

# Create your views here.
def about(request):
    return render(request, 'about/about.html')


def teachers_info(request):
    teachers = Teachers.objects.all()
    return render(request, 'about/teachers.html', {'thr':teachers})