from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def machine_learning(request):
    # course = 'machine Learning'
    # tclass = 21
    # seat = 20
    # cduration = '2.5 months'   
    # offering = {'c':course, 'tl':tclass, 'st':seat, 'cd':cduration}
    
    Teachers = {'names':['Shakil','Mejba','Shohan']}
    
    
    
    return render(request, 'machine_learning/machine_learning.html',context = Teachers)

def random(request):
    return render(request, 'machine_learning/random_forest.html')

def knn(request):
    return render(request, 'machine_learning/knn.html')

def dt(request):
    return render(request, 'machine_learning/dt.html')
