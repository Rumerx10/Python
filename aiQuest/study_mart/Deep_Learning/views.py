from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def deep_learning(request):
    return render(request, 'deep_learning/deep_learning.html')

def registration(request):
    if request.method=='POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserCreationForm()        
    return render(request, 'deep_learning/registration.html', {'form':fm})


# def deep_learning_os(request):
#     return HttpResponse('<h1>Deep Learning Page : 2</h1></b><h3>OS</h3>')
# def deep_learning_ai(request):
#     return HttpResponse('<h1>Deep Learning Page : 3</h1></b><h3>AI</h3>')
