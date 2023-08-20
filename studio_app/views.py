from django.shortcuts import render, redirect, get_object_or_404
from.forms import *
from django.contrib import messages
from datetime import datetime, timedelta, date
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from accounts.models import *

# Create your views here.
#....................................Labs...............................
def add_lab(request):
    form = addLabsForm()
    if request.method == 'POST':
        form = addLabsForm(request.POST or None)
        get_name =request.POST.get('name') 
        check_name = Lab.objects.filter(name=get_name ).count()
        if form.is_valid():   
            if check_name == 0:       
                 form.save()
                 messages.success(request, f'Lab added successfully!')
                 return redirect('viewLab')
            else:
                 messages.warning(request, f'Lab already exists!')      

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

def updateLab(request,id):
    instance = get_object_or_404(Lab, pk = id)
    form = updateLabsForm(request.POST or None,instance = instance)
    get_name =request.POST.get('name') 
    check_name = Lab.objects.filter(name=get_name ).count()
    if request.method == 'POST': 
        if form.is_valid():  
            if check_name == 0:       
                 form.save()
                 messages.success(request, f'Lab added successfully!')
                 return redirect('viewLab')
            else:
                 messages.warning(request, f'Lab already exists!') 

    context = {
     'form': form,
    }
    myTemplate = 'studio/updateLab.html'
    return render(request, myTemplate, context) 

def deleteLab(request, id):
    try:
        get_lab = Lab.objects.get(id=id)
        get_lab.delete()
        return redirect('viewLab')
    except:
        messages.success(request,"Lab is already used can't be deleted ")
        return redirect('viewLab')

#.........................Components...................
def addComponent(request):
    form = addComponentsForm()
    if request.method == 'POST':
        form = addComponentsForm(request.POST or None)
        get_name =request.POST.get('name') 
        get_lab = request.POST.get('lab')   
        get_value = request.POST.get('value')   
        check_name = Component.objects.filter(name=get_name,lab = get_lab, value = get_value).count()
    if request.method == 'POST': 
        if form.is_valid():  
            if check_name == 0:       
                 form.save()
                 messages.success(request, f'Component added successfully!')
                 return redirect('viewComponent')
            else:
                 messages.warning(request, f'Component already exists!') 

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

def updateComponent(request,id):
    instance = get_object_or_404(Component, pk = id)
    form =addComponentsForm(request.POST or None,instance = instance)
    get_name =request.POST.get('name') 
    get_lab = request.POST.get('lab')   
    get_value = request.POST.get('value') 
    get_quantity = request.POST.get('quantity')
    check_name = Component.objects.filter(name=get_name,lab = get_lab,value = get_value,quantity = get_quantity).count()
    if request.method == 'POST': 
        if form.is_valid():  
            if check_name == 0:       
                 form.save()
                 messages.success(request, f'Component added successfully!')
                 return redirect('viewComponent')
            else:
                 messages.warning(request, f'Component already exists!') 
    context = {
     'form': form,
    }
    myTemplate = 'studio/updateComponent.html'
    return render(request, myTemplate, context) 

def deleteComponent(request, id):
    try:
        get_object = Lab.objects.filter(id=id)
        get_object.delete()
        return redirect('viewComponent')
    except:
        messages.success(request,"component is already used can't be deleted ")
        return redirect('viewComponent')
    

#.....................................Source of income...................................
def addSourceOfIncome(request):
    form = addSourceOfIncomeForm()
    if request.method == 'POST':
        form = addSourceOfIncomeForm(request.POST or None)
        get_name = request.POST.get('name')     
        check_name = Source_of_Income.objects.filter(name=get_name).count()
    if request.method == 'POST': 
        if form.is_valid():  
            if check_name == 0:       
                 form.save()
                 messages.success(request, f'Source of income added successfully!')
                 return redirect('viewSourceOfIncome')
            else:
                 messages.warning(request, f'Source of income already exists!')

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

def updateSourceOfIncome(request,id):
    instance = get_object_or_404(Source_of_Income, pk = id)
    form =addSourceOfIncomeForm(request.POST or None,instance = instance)
    get_name = request.POST.get('name')     
    check_name = Source_of_Income.objects.filter(name=get_name).count()
    if request.method == 'POST': 
        if form.is_valid():  
            if check_name == 0:       
                 form.save()
                 messages.success(request, f'Source of income added successfully!')
                 return redirect('viewSourceOfIncome')
            else:
                 messages.warning(request, f'Source of income already exists!')
    context = {
     'form': form,
    }
    myTemplate = 'studio/updateSourceOfIncome.html'
    return render(request, myTemplate, context) 

def deleteSourceOfIncome(request, id):
    try:
        get_object = Source_of_Income.objects.filter(id=id)
        get_object.delete()
        return redirect('viewSourceOfIncome')
    except:
        messages.success(request,"Source of income is already used can't be deleted ")
        return redirect('viewSourceOfIncome')

#............................................Income..................................
def addIncome(request):
    form = addIncomeForm()
    if request.method == 'POST':
        form = addIncomeForm(request.POST or None)
        if form.is_valid():          
            form.save()
            messages.success(request, f'Income added successfully!')
            return redirect('viewIncome')

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

def updateIncome(request,id):
    instance = get_object_or_404(Income, pk = id)
    form =addIncomeForm(request.POST or None,instance = instance)
    if request.method == 'POST': 
        if form.is_valid():          
            form.save()
            messages.success(request, f'Income updated successfully!')
            return redirect('viewIncome')

    context = {
     'form': form,
    }
    myTemplate = 'studio/updateIncome.html'
    return render(request, myTemplate, context) 

def deleteIncome(request, id):
    try:
        get_object = Income.objects.filter(id=id)
        get_object.delete()
        return redirect('viewIncome')
    except:
        messages.success(request,"Income is already used can't be deleted ")
        return redirect('viewIncome')

#............................................Purchases..................................
def addPurchase(request):
    form = addPurchaseForm()
    if request.method == 'POST':
        form = addPurchaseForm(request.POST or None)
        if form.is_valid():          
            form.save()
            messages.success(request, f'Purchase added successfully!')
            return redirect('viewPurchases')

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

def updatePurchases(request,id):
    instance = get_object_or_404(Purchases, pk = id)
    form =addPurchaseForm(request.POST or None,instance = instance)
    if request.method == 'POST': 
        if form.is_valid():          
            form.save()
            messages.success(request, f'Purchases updated successfully!')
            return redirect('viewPurchases')

    context = {
     'form': form,
    }
    myTemplate = 'studio/updatePurchase.html'
    return render(request, myTemplate, context) 

def deletePurchase(request, id):
    try:
        get_object = Purchases.objects.filter(id=id)
        get_object.delete()
        return redirect('viewPurchases')
    except:
        messages.success(request,"Purchases is already used can't be deleted ")
        return redirect('viewPurchases')

#.............................................Source of expenses................................................
def addSourceOfExpenses(request):
    form = addSourceOfExpensesForm()
    if request.method == 'POST':
        form = addSourceOfExpensesForm(request.POST or None)
        get_name = request.POST.get('name')     
        check_name = Source_Of_Expenses.objects.filter(name=get_name).count()
        if request.method == 'POST': 
            if form.is_valid():  
                if check_name == 0:       
                    form.save()
                    messages.success(request, f'Source of expenses added successfully!')
                    return redirect('viewSourceOfExpenses')
                else:
                    messages.warning(request, f'Source of expenses already exists!')
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

def updateExpensesSource(request,id):
    instance = get_object_or_404(Source_Of_Expenses, pk = id)
    form =addSourceOfExpensesForm(request.POST or None,instance = instance)
    if request.method == 'POST': 
        if form.is_valid():          
            form.save()
            messages.success(request, f'Source of expenses updated successfully!')
            return redirect('viewSourceOfExpenses')

    context = {
     'form': form,
    }
    myTemplate = 'studio/updateSourceOfExpenses.html'
    return render(request, myTemplate, context) 

def deleteSourceOfExpenses(request, id):
    try:
        get_object = Source_Of_Expenses.objects.filter(id=id)
        get_object.delete()
        return redirect('viewSourceOfExpenses')
    except:
        messages.success(request,"Source of expenses is already used can't be deleted ")
        return redirect('viewSourceOfExpenses')

#......................................................Expenses...........................
def addExpenses(request):
    form = addExpensesForm()
    if request.method == 'POST':
        form = addExpensesForm(request.POST or None)
        if form.is_valid():          
            form.save()
            messages.success(request, f'Expenses added successfully!')
            return redirect('viewExpenses')

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

def updateExpenses(request,id):
    instance = get_object_or_404(Expenses, pk = id)
    form = updateExpensesForm(request.POST or None,instance = instance)
    if request.method == 'POST': 
        if form.is_valid():          
            form.save()
            messages.success(request, f'Expenses updated successfully!')
            return redirect('viewExpenses')

    context = {
     'form': form,
    }
    myTemplate = 'studio/updateExpenses.html'
    return render(request, myTemplate, context) 

def deleteExpenses(request, id):
    try:
        get_object = Expenses.objects.filter(id=id)
        get_object.delete()
        return redirect('viewExpenses')
    except:
        messages.success(request,"Expenses is already used can't be deleted ")
        return redirect('viewExpenses')

#.......................................................Location........................................
def addLocation(request):
    form =addLocationForm()
    if request.method == 'POST':
        form = addLocationForm(request.POST or None)
        get_name = request.POST.get('name')     
        check_name = Location.objects.filter(name=get_name).count()
        if request.method == 'POST': 
            if form.is_valid():  
                if check_name == 0:       
                    form.save()
                    messages.success(request, f'Location added successfully!')
                    return redirect('viewLocation')
                else:
                    messages.warning(request, f'Location already exists!')
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

def updateLocation(request,id):
    instance = get_object_or_404(Location, pk = id)
    form =addLocationForm(request.POST or None,instance = instance)
    get_name = request.POST.get('name')     
    check_name = Location.objects.filter(name=get_name).count()
    if request.method == 'POST': 
        if form.is_valid():  
            if check_name == 0:       
                form.save()
                messages.success(request, f'Location added successfully!')
                return redirect('viewLocation')
            else:
                messages.warning(request, f'Location already exists!')
                return redirect('addLocation')
    context = {
     'form': form,
    }
    myTemplate = 'studio/updateLocation.html'
    return render(request, myTemplate, context) 

def deleteLocation(request, id):
    try:
        get_object = Location.objects.filter(id=id)
        get_object.delete()
        return redirect('viewLocation')
    except:
        messages.success(request,"Location is already used can't be deleted ")
        return redirect('viewLocation')

#.....................................................Member Type........................................
def addMemberType(request):
    form = addMemberTypeForm()
    if request.method == 'POST':
        form = addMemberTypeForm(request.POST or None)
        get_name = request.POST.get('type')     
        check_name = Member_type.objects.filter(type=get_name).count()
        if request.method == 'POST': 
            if form.is_valid():  
                if check_name == 0:       
                    form.save()
                    messages.success(request, f'Member type added successfully!')
                    return redirect('viewMemberType')
                else:
                    messages.warning(request, f'Member type already exists!')
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

def updateMemberType(request,id):
    instance = get_object_or_404(Member_type, pk = id)
    form =addMemberTypeForm(request.POST or None,instance = instance)
    get_name = request.POST.get('type')     
    check_name = Member_type.objects.filter(type=get_name).count()
    if request.method == 'POST': 
        if form.is_valid():  
            if check_name == 0:       
                form.save()
                messages.success(request, f'Member type added successfully!')
                return redirect('viewMemberType')
            else:
                messages.warning(request, f'Member type already exists!')
                return redirect('addMemberType')

    context = {
     'form': form,
    }
    myTemplate = 'studio/updateMemberType.html'
    return render(request, myTemplate, context) 

def deleteMemberType(request, id):
    try:
        get_object = Member_type.objects.filter(id=id)
        get_object.delete()
        return redirect('viewMemberType')
    except:
        messages.success(request,"Member type is already used can't be deleted ")
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
            memberType = str(get_memberTypeName)
           
            dob = datetime.strptime(get_DOB, '%Y-%m-%d').date().day
           
            get_idNumber =f'{get_nationality.strip()[0].upper()}{get_fname.strip()[0].upper()}{get_lname.strip()[0].upper()}{get_gender.strip()[0].upper()}{memberType.strip()[0].upper()}{get_registeredDate.date().day}{str(get_phone).strip()[-2:]}{dob} '  
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
            return redirect('viewMembers')

    context = {
     'form': form,
    }
    myTemplate = 'studio/addMember.html'
    return render(request, myTemplate, context) 

@login_required
def viewMembers(request):
    members = Member.objects.all()

    context = {
        'members': members,
         }
    myTemplate = 'studio/viewMembers.html'
    return render(request, myTemplate, context)

@login_required
def updateMember(request,id):
    instance = get_object_or_404(Member, pk = id)
    form =addMemberForm(request.POST or None,instance = instance)
    if request.method == 'POST': 
        if form.is_valid(): 
            get_fname =request.POST.get('firstName')        
            get_mname =request.POST.get('middleName')        
            get_lname =request.POST.get('lastName')        
            get_DOB =request.POST.get('dateOfBirth')        
            get_regNo =request.POST.get('registrationNumber')        
            get_phone =request.POST.get('phoneNumber')         
            get_email =request.POST.get('email')        
            # get_registeredDate =request.POST.get('registeredDate')              
            get_nationality =request.POST.get('nationality')         
            get_gender =request.POST.get('gender')       
            get_location =request.POST.get('location') 
            get_memberType = request.POST.get('type')
            get_memberTypeName = Member_type.objects.get(id=get_memberType )  
            get_LocationName = Location.objects.get(id=get_location )

            memberType = str(get_memberTypeName)  
            memberEdited  = Member.objects.get(id=id)
            get_registeredDate = memberEdited.registeredDate
    
            print(get_registeredDate.day) 

            dob = datetime.strptime(get_DOB, '%Y-%m-%d').date().day           
            get_idNumber =f'{get_nationality.strip()[0].upper()} {get_fname.strip()[0].upper()} {get_lname.strip()[0].upper()} {get_gender.strip()[0].upper()} {memberType.strip()[0].upper()} {get_registeredDate.day} {str(get_phone).strip()[-2:]} {dob} '  
            
            updateMember = Member.objects.get(id = id)
           
            # updateMember.firstName = get_fname,
            # updateMember.middleName = get_mname,
            # updateMember.lastName = get_lname,
            # updateMember.dateOfBirth = get_DOB,
            # updateMember.registrationNumber = get_regNo,
            # updateMember.phoneNumber = get_phone,
            # updateMember.email=get_email,
            # updateMember.nationality = get_nationality,
            # updateMember.gender = get_gender,
            # updateMember.registeredDate = get_registeredDate,
            updateMember.idNumber = get_idNumber
            # updateMember.location= get_location,
            # # updateMember.type = get_memberTypeName          
               

            updateId=form.save()
            updateId.idNumber = get_idNumber
            updateId.save()
            messages.success(request, f'Member updated successfully!')
            return redirect('viewMembers')

    context = {
     'form': form,
    }
    myTemplate = 'studio/updateMember.html'
    return render(request, myTemplate, context) 

@login_required
def deleteMember(request, id):
    try:
        get_object = Member.objects.filter(id=id)
        get_object.delete()
        return redirect('viewMembers')
    except:
        messages.success(request,"Member is already used can't be deleted ")
        return redirect('viewMembers')

#.........................................CheckInAndCheckOut....................................................
@login_required
def viewCheck(request):
    allMembers = Member.objects.all()

    context = {
        'allMembers': allMembers,
         }
    myTemplate = 'studio/checkinAndOut.html'
    return render(request, myTemplate, context)

@login_required
def addCheckInAndOut(request, member_id):
    check = CheckInAndout.objects.filter(member=member_id, date__date=datetime.now().date()).count()
    member = Member.objects.get(id=member_id)
    status = "CHECK-IN" if check % 2 == 0 else "CHECK-OUT"  
    check = CheckInAndout(
        member_id = member_id,
        date = datetime.now(),
        status = status
    )
    status_message  = "checked in" if status == "CHECK-IN " else "checked out"      
    messages.success(request, f'{member.firstName} {member.lastName} you have successful {status_message}')
    check.save()
    return redirect('checkInAndOut')

@login_required
def viewCheckedInAndOut(request):
    members = CheckInAndout.objects.all()       
    context = {
        'members': members 
         }  
    myTemplate ='studio/viewCheckInAndOut.html'  
    return render(request, myTemplate,context)   

#.............................................Requested components..........................

def addRequestedComponents(request):
    components = Component.objects.all()          
    if request.method == 'POST':
            get_email = request.POST.get('email') 
            try:
                get_member = Member.objects.get(email=get_email)
            except Member.DoesNotExist:
                messages.warning(request, f'Sorry,no member with this email address exists!')
                return redirect('addRequestedComponents')
            # if get_member == None:
            #     messages.success(request, f'Email does not exist')
            #     return redirect('addRequestedComponents')
            # else: 
            req, created =Request.objects.get_or_create(member = get_member, requested = False)   
            # items = order.Requestcomponents_set.all()
            items= Requestcomponents.objects.filter (request=req)  
            context = {
                'components':components,
                'member': get_member,  
                'items':items,
                'request':req.id
            }
            myTemplate = 'studio/requestComponents.html'
            return render(request, myTemplate, context) 
    
    context = { }
    myTemplate = 'studio/checkEmail.html'
    return render(request, myTemplate, context) 

@login_required
def viewRequestedComponents(request):
    # Components = Requestcomponents.objects.all()
    Components = Requestcomponents.objects.filter(status = None)

    context = {
        'Components': Components,
         }
    myTemplate = 'studio/viewRequestedComponents.html'
    return render(request, myTemplate, context)

@login_required
def updateComponentRequest(request):
    data = json.loads(request.body)
    componentId = data['componentId']
    action = data['action']
    member = data['member']
 
    print('member:', member, 'action:', action  )
    req, created =Request.objects.get_or_create(member_id = member, requested = False) 

    component = Component.objects.get(id=componentId)
    requestcomponents, created = Requestcomponents.objects.get_or_create(request = req, component=component)

    if action == 'add':
        requestcomponents.quantity = (requestcomponents.quantity + 1)
    elif action == 'remove':
        requestcomponents.quantity = (requestcomponents.quantity - 1)
    requestcomponents.save()

    if requestcomponents.quantity <= 0 or action == 'delete':
        requestcomponents.delete()
    
    return JsonResponse("component was added successfully", safe=False)

@login_required
def updateRequest(request,id):
    req = Request.objects.get(id=id)
    req.requested = True
    req.save()
    messages.success(request, f'Your request has been sent successfully!')
    return redirect(addRequestedComponents)

@login_required
def issueComponents(request,id):
    issue = Requestcomponents.objects.get(id=id)
    issue.status = "Accepted"
    issue.save()
    return redirect(viewRequestedComponents)

@login_required
def declinedComponents(request,id):
    issue = Requestcomponents.objects.get(id=id)
    issue.status = "Declined"
    issue.save()
    return redirect(viewRequestedComponents)

# ..........................................dashboard...................................
@login_required
def dashboard(request):
    members = Member.objects.all().count()
    chekin = CheckInAndout.objects.filter(status ="CHECK-IN").count()
    requestedComponent = Requestcomponents.objects.filter(status = None).count()
    totalUsers = CustomUser.objects.all().count()


    print(members)
    print(chekin)
    print("request:",request)
    context = {
        'members' : members,
        'checkin' : chekin,
        'requestedComponent': requestedComponent,
        'totalUsers':totalUsers
       
         }
    myTemplate = 'studio/dashboard.html'
    return render(request, myTemplate, context)







 