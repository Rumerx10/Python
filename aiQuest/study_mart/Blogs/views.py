from django.shortcuts import render

from .forms import TeacherRegistration

# Create your views here.
def blog1(request):
    return render(request, 'blogs/blogs.html')

def showFormsData(request):
    if request.method == 'POST':
        formData = TeacherRegistration(request.POST)
        print(formData)
        if formData.is_valid():
            print('This is POST statement')
            # print(formData.cleaned_data)
            print(formData.cleaned_data['password'])
            print(formData.cleaned_data['repassword'])
    else:
        formData = TeacherRegistration()
        print('This is GET method.')    
    # formData.order_fields(field_order=['email','first_name','last_name'])
    return render(request, 'blogs/form.html', {'form':formData})