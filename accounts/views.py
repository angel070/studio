from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from datetime import datetime, timedelta, date

# Create your views here.
def login(request):              
    return render(request,'accounts/login.html')  

def addUser(request):
    form = addUserForm()
    if request.method == 'POST':
        form = addUserForm(request.POST or None)
        get_userName =  request.POST.get('userName')      
        if form.is_valid():          
            obj = form.save()
            obj.password = get_userName
            obj.save()
            messages.success(request, f'User  added successfully!')
            return redirect('addUser')

    context = {
     'form': form,
    }
    myTemplate = 'accounts/addUser.html'
    return render(request, myTemplate, context) 

def login(request):  
    get_userName =request.POST.get('username') 
    get_password = request.POST.get('password') 

    check = RegisterUser.objects.filter(userName=get_userName , password=get_password).count() 
    if check != 0:
        return redirect('addLab')
      
    else:
        messages.success(request, f'wrong username or password')
        myTemplate = 'accounts/login.html'
        return render(request,myTemplate)

