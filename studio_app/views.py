from django.shortcuts import render, redirect, get_object_or_404
from.forms import *
from django.contrib import messages
from datetime import datetime, timedelta, date

# Create your views here.
def home(request):              
    return render(request,'studio/home.html')  

#....................................Labs...............................
def add_lab(request):
    form = addLabsForm()
    if request.method == 'POST':
        form = addLabsForm(request.POST or None)
        get_lab = request.POST.get('name')
        if form.is_valid():          
            form.save()
            messages.success(request, f'Lab added successfully!')
            return redirect('addLab')

    context = {
     'form': form,
    }
    myTemplate = 'studio/addLab.html'
    return render(request, myTemplate, context) 

def viewLab(request):
    labs = Lab.objects.all()

    context = {
        'labs': labs,
         }
    myTemplate = 'studio/viewLabs.html'
    return render(request, myTemplate, context)

def deleteLab(request, id):
    get_lab = Lab.objects.filter(id=id)
    get_lab.delete()
    return redirect('viewLab')

#.........................Components...................
def addComponent(request):
    form = addComponentsForm()
    if request.method == 'POST':
        form = addComponentsForm(request.POST or None)
        if form.is_valid():          
            form.save()
            messages.success(request, f'Component added successfully!')
            return redirect('addComponent')

    context = {
     'form': form,
    }
    myTemplate = 'studio/addComponent.html'
    return render(request, myTemplate, context) 

def viewComponent(request):
    components = Component.objects.all()

    context = {
        'Components': components,
         }
    myTemplate = 'studio/viewComponent.html'
    return render(request, myTemplate, context)

def deleteComponent(request, id):
    get_object = Lab.objects.filter(id=id)
    get_object.delete()
    return redirect('viewComponent')

#.....................................Source of income...................................
def addSourceOfIncome(request):
    form = addSourceOfIncomeForm()
    if request.method == 'POST':
        form = addSourceOfIncomeForm(request.POST or None)
        if form.is_valid():          
            form.save()
            messages.success(request, f'Source of income added successfully!')
            return redirect('addSourceOfIncome')

    context = {
     'form': form,
    }
    myTemplate = 'studio/addSourceofIncome.html'
    return render(request, myTemplate, context) 

def viewSourceOfIncome(request):
    IncomeSources = Source_of_Income.objects.all()

    context = {
        'IncomeSources': IncomeSources,
         }
    myTemplate = 'studio/viewSourceOfIncome.html'
    return render(request, myTemplate, context)

def deleteSourceOfIncome(request, id):
    get_object = Source_of_Income.objects.filter(id=id)
    get_object.delete()
    return redirect('viewSourceOfIncome')

#............................................Income..................................
def addIncome(request):
    form = addIncomeForm()
    if request.method == 'POST':
        form = addIncomeForm(request.POST or None)
        if form.is_valid():          
            form.save()
            messages.success(request, f'Income added successfully!')
            return redirect('addIncome')

    context = {
     'form': form,
    }
    myTemplate = 'studio/addIncome.html'
    return render(request, myTemplate, context) 

def viewIncome(request):
    Incomes = Income.objects.all()

    context = {
        'Incomes': Incomes,
         }
    myTemplate = 'studio/viewIncome.html'
    return render(request, myTemplate, context)

def deleteIncome(request, id):
    get_object = Income.objects.filter(id=id)
    get_object.delete()
    return redirect('viewIncome')

#............................................Purchases..................................
def addPurchase(request):
    form = addPurchaseForm()
    if request.method == 'POST':
        form = addPurchaseForm(request.POST or None)
        if form.is_valid():          
            form.save()
            messages.success(request, f'Purchase added successfully!')
            return redirect('addPurchase')

    context = {
     'form': form,
    }
    myTemplate = 'studio/addPurchase.html'
    return render(request, myTemplate, context) 

def viewPurchases(request):
    purchases = Purchases.objects.all()

    context = {
        'purchases': purchases,
         }
    myTemplate = 'studio/viewPurchases.html'
    return render(request, myTemplate, context)

def deletePurchase(request, id):
    get_object = Purchases.objects.filter(id=id)
    get_object.delete()
    return redirect('viewPurchases')

#.............................................Source of expenses................................................
def addSourceOfExpenses(request):
    form = addSourceOfExpensesForm()
    if request.method == 'POST':
        form = addSourceOfExpensesForm(request.POST or None)
        if form.is_valid():          
            form.save()
            messages.success(request, f'Source of Expenses added successfully!')
            return redirect('addSourceOfExpenses')

    context = {
     'form': form,
    }
    myTemplate = 'studio/addSourceOfExpenses.html'
    return render(request, myTemplate, context) 

def viewSourceOfExpenses(request):
    ExpenseSources = Source_Of_Expenses.objects.all()

    context = {
        'ExpenseSources': ExpenseSources,
         }
    myTemplate = 'studio/viewSourceOfExpenses.html'
    return render(request, myTemplate, context)

def deleteSourceOfExpenses(request, id):
    get_object = Source_Of_Expenses.objects.filter(id=id)
    get_object.delete()
    return redirect('viewSourceOfExpenses')

#......................................................Expenses...........................
def addExpenses(request):
    form = addExpensesForm()
    if request.method == 'POST':
        form = addExpensesForm(request.POST or None)
        if form.is_valid():          
            form.save()
            messages.success(request, f'Expenses added successfully!')
            return redirect('addExpenses')

    context = {
     'form': form,
    }
    myTemplate = 'studio/addExpenses.html'
    return render(request, myTemplate, context) 

def viewExpenses(request):
    expenses = Expenses.objects.all()

    context = {
        'expenses': expenses,
         }
    myTemplate = 'studio/viewExpenses.html'
    return render(request, myTemplate, context)

def deleteExpenses(request, id):
    get_object = Expenses.objects.filter(id=id)
    get_object.delete()
    return redirect('viewExpenses')

#.......................................................Location........................................
def addLocation(request):
    form =addLocationForm()
    if request.method == 'POST':
        form = addLocationForm(request.POST or None)
        if form.is_valid():          
            form.save()
            messages.success(request, f'Member Location added successfully!')
            return redirect('addLocation')

    context = {
     'form': form,
    }
    myTemplate = 'studio/addLocation.html'
    return render(request, myTemplate, context) 

def viewLocation(request):
    locations = Location.objects.all()

    context = {
        'locations': locations,
         }
    myTemplate = 'studio/viewLocation.html'
    return render(request, myTemplate, context)

def deleteLocation(request, id):
    get_object = Location.objects.filter(id=id)
    get_object.delete()
    return redirect('viewLocation')

#.....................................................Member Type........................................
def addMemberType(request):
    form = addMemberTypeForm()
    if request.method == 'POST':
        form = addMemberTypeForm(request.POST or None)
        if form.is_valid():          
            form.save()
            messages.success(request, f'Member Type added successfully!')
            return redirect('addMemberType')

    context = {
     'form': form,
    }
    myTemplate = 'studio/addMemberType.html'
    return render(request, myTemplate, context) 

def viewMemberType(request):
    memberTypes = Member_type.objects.all()

    context = {
        'memberTypes': memberTypes,
         }
    myTemplate = 'studio/viewMemberType.html'
    return render(request, myTemplate, context)

def deleteMemberType(request, id):
    get_object = Member_type.objects.filter(id=id)
    get_object.delete()
    return redirect('viewMemberType')


#......................................................Member.................................................
def addMember(request):
    form = addMemberForm()
    if request.method == 'POST':
        form = addMemberForm(request.POST or None)
        if form.is_valid():  
            get_fname =request.POST.get('firstName')        
            get_mname =request.POST.get('middleName')        
            get_lname =request.POST.get('lastName')        
            get_DOB =request.POST.get('dateOfBirth')        
            get_regNo =request.POST.get('registrationNumber')        
            get_phone =request.POST.get('phoneNumber')         
            get_email =request.POST.get('email')        
            get_nationality =request.POST.get('nationality')         
            get_gender =request.POST.get('gender')                
            get_registeredDate =datetime.now()  
            get_location =request.POST.get('location') 
            get_memberType = request.POST.get('type')
            print(get_memberType)
            #get name of member type and location using their Id
            get_memberTypeName = Member_type.objects.get(id=get_memberType )  
            get_LocationName = Location.objects.get(id=get_location )  
            memberType = str(get_memberTypeName ) 
            print("hello"+str(get_memberTypeName)) 
           
            dob = datetime.strptime(get_DOB, '%Y-%m-%d').date().day
           
            get_idNumber =f'{get_nationality.strip()[0].upper()} {get_fname.strip()[0].upper()} {get_lname.strip()[0].upper()} {get_gender.strip()[0].upper()} {memberType.strip()[0].upper()} {get_registeredDate.date().day} {str(get_phone).strip()[-2:]} {dob}'  
            form = Member(
                firstName = get_fname,
                middleName = get_mname,
                lastName = get_lname,
                dateOfBirth = get_DOB,
                registrationNumber = get_regNo,
                phoneNumber = get_phone,
                email=get_email,
                nationality = get_nationality,
                gender = get_gender,
                registeredDate = get_registeredDate,
                idNumber = get_idNumber, 
                location = get_LocationName,
                type = get_memberTypeName          
            )     
            form.save()
            messages.success(request, f'Student added successfully!')
            return redirect('addMember')

    context = {
     'form': form,
    }
    myTemplate = 'studio/addMember.html'
    return render(request, myTemplate, context) 

def viewMembers(request):
    members = Member.objects.all()

    context = {
        'members': members,
         }
    myTemplate = 'studio/viewMembers.html'
    return render(request, myTemplate, context)

def deleteMember(request, id):
    get_object = Member.objects.filter(id=id)
    get_object.delete()
    return redirect('viewMembers')