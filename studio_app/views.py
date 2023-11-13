from django.shortcuts import render, redirect, get_object_or_404
from.forms import *
from django.contrib import messages
from datetime import datetime, timedelta, date
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from accounts.models import *
from dateutil.relativedelta import relativedelta
import pandas as pd


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
        get_unit = request.POST.get('unit')

        try:
            component = Component.objects.get(name=get_name, unit=get_unit)
            messages.warning(request, f'Component already exists!')
        except Component.DoesNotExist:
            if form.is_valid():
                form.save()
                messages.success(request, f'Component added successfully!')
                return redirect('viewComponent')
                                

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

def updateComponent(request, id):
    instance = get_object_or_404(Component, pk = id)
    form =addComponentsForm(request.POST or None, instance = instance)
    get_name =request.POST.get('name')
    get_unit = request.POST.get('unit')

    try:
        component = Component.objects.get(name=get_name, unit = get_unit)
        messages.warning(request, f'Component already exists!')
    except Component.DoesNotExist:
        if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request, f'Component updated successfully!')
            return redirect('viewComponent')
    context = {
     'form': form,
    }
    myTemplate = 'studio/updateComponent.html'
    return render(request, myTemplate, context)

def deleteComponent(request, id):
    instance = get_object_or_404(Component, pk = id)
    try:
        instance.delete()
        messages.success(request,"Component deleted successfully!")
        return redirect('viewComponent')
    except:
        messages.warning(request,"Component can't be deleted ")
        return redirect('viewComponent')
    
#...................................Lab Component..................................................
def view_lab_components(request):
    labComponents = LabComponent.objects.all()
    context = {
     'labComponents': labComponents,
    }
    myTemplate = 'studio/viewLabComponents.html'
    return render(request, myTemplate, context)

def add_component_to_lab(request):
    if request.method == 'POST':
        get_lab =request.POST.get('lab')
        get_component = request.POST.get('component')
        get_quantity = request.POST.get('quantity')

        lab = get_object_or_404(Lab, pk = get_lab)
        component = get_object_or_404(Component, pk = get_component)

        try:
            labComponent = LabComponent.objects.get(lab=lab, component=component)
            messages.warning(request, f"Component {component.name} already exists in lab {lab.name}!")
        except LabComponent.DoesNotExist:
            labComponent = LabComponent(
                lab = lab,
                component = component,
                quantity = get_quantity
            )
            labComponent.save()
            messages.success(request, f"Component {component.name} - {component.unit} added to lab {lab.name}!")
        return redirect('viewLabComponents')
    labs = Lab.objects.all()
    components = Component.objects.all()
    context = {
     'labs': labs,
     'components': components,
    }
    myTemplate = 'studio/addLabComponent.html'
    return render(request, myTemplate, context)

def update_component_in_lab(request, id):
    labComponent = get_object_or_404(LabComponent, pk = id)
    if request.method == 'POST':
        get_lab =request.POST.get('lab')
        get_component = request.POST.get('component')
        get_quantity = request.POST.get('quantity')

        lab = get_object_or_404(Lab, pk = get_lab)
        component = get_object_or_404(Component, pk = get_component)

        labComponent.lab = lab
        labComponent.component = component
        labComponent.quantity = get_quantity
        labComponent.save()
        messages.success(request, f"Component {component.name}- {component.unit} in lab {lab.name} has been updated!")
        return redirect('viewLabComponents')
    labs = Lab.objects.all()
    components = Component.objects.all()
    context = {
     'labs': labs,
     'components': components,
     'labComponent': labComponent
    }
    myTemplate = 'studio/addLabComponent.html'
    return render(request, myTemplate, context)


def remove_component_to_lab(request, id):
    lab_component = get_object_or_404(LabComponent, pk = id)
    component_name = lab_component.component.name + " - " + lab_component.component.unit
    lab_name = lab_component.lab.name
    lab_component.delete()
    messages.success(request, f"Component {component_name} removed from lab {lab_name}!")
    return redirect('viewLabComponents')

#...................................Department..................................................
def addDepartment(request):
    form = addDepartmentForm()
    if request.method == 'POST':       
        form = addDepartmentForm(request.POST or None)
        get_name =request.POST.get('name')
        
        try:
            department = Department.objects.get(name = get_name)
            messages.warning(request, f'Department already exists!')
        except Department.DoesNotExist:
            if form.is_valid():               
                form.save()
                messages.success(request, f'Department added successfully!')
                return redirect('viewDepartment')
  

    context = {
     'form': form,
    }
    myTemplate = 'studio/addDepartment.html'
    return render(request, myTemplate, context)

def viewDepartment(request):
    departments = Department.objects.all()

    context = {
     'departments': departments,
    }
    myTemplate = 'studio/viewDepartment.html'
    return render(request, myTemplate, context)

def updateDepartment(request,id):
    instance = get_object_or_404(Department, pk = id)
    form = updateDeparmentForm(request.POST or None,instance = instance)
    get_name =request.POST.get('name')
    check_name =Department.objects.filter(name=get_name ).count()
    if check_name != 0:
        messages.warning(request, f'Department already exists!')
    else:
        if request.method == 'POST':
            if form.is_valid():
                if check_name == 0:
                    form.save()
                    messages.success(request, f'Department edited successfully!')
                    return redirect('viewDepartment')
                         

    context = {
     'form': form,
    }
    myTemplate = 'studio/updateDepartment.html'
    return render(request, myTemplate, context)

def deleteDepartment(request,id):
    try:
        get_object = Department.objects.filter(id=id)
        get_object.delete()
        return redirect('viewDepartment')
    except:
        messages.success(request,"Department is already used can't be deleted ")
        return redirect('viewDepartment')


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
    myTemplate = 'studio/addSourceOfIncome.html'
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
            purchase = form.save()
            try:
                component = LabComponent.objects.get(component=purchase.component, lab=purchase.lab)
                component.quantity += purchase.quantity
                component.save()
            except LabComponent.DoesNotExist:
                labComponent = LabComponent(
                    component=purchase.component, 
                    lab=purchase.lab,
                    quantity = purchase.quantity
                )
                labComponent.save()
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
        messages.success(request,"Exgi penses is already used can't be deleted ")
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
            get_department =request.POST.get('department')
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
                type = get_memberTypeName,
                department_id = get_department
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
    # check_member = MemberPayment.objects.filter(member_id=member_id).count()
    # if check_member == 0:
    #     messages.warning(request, f'Please make payment!')
    #     return redirect('checkInAndOut')
    # else:
    #     check_payment = MemberPayment.objects.filter(member_id=member_id).last()
    #     if check_payment.remainingDays <= 0 :
    #         messages.warning(request, f'Please make payment!')
    #         return redirect('checkInAndOut')
    #     else:
            check = CheckInAndout.objects.filter(member=member_id, date__date=datetime.now().date()).count()
            member = Member.objects.get(id=member_id)
            status = "CHECK-IN" if check % 2 == 0 else "CHECK-OUT"
            check = CheckInAndout(
                member_id = member_id,
                date = datetime.now(),
                status = status
            )
            check.save()
            status_message  = "checked in" if status == "CHECK-IN" else "checked out"
            messages.success(request, f'{member.firstName} {member.lastName} you have successful {status_message}')
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
    if request.method == 'POST':
        components = Component.objects.all()
        get_email = request.POST.get('email')
        # get_member_id =Member.objects.get(email=get_email)
        # check_member = MemberPayment.objects.filter(member_id=get_member_id).count()
        try:
            get_member = Member.objects.get(email=get_email)
        except Member.DoesNotExist:
            messages.warning(request, f'Sorry,no member with this email address')
            return redirect('addRequestedComponents')
        
        # if check_member == 0:
        #     messages.warning(request, f'Please make payment')
        #     return redirect('addRequestedComponents')
        # else:
            # check_payment = MemberPayment.objects.filter(member_id=get_member_id).last()
            # if check_payment.remainingDays < 0 :
            #     messages.warning(request, f'Please make payment before requesting component!')
            #     return redirect('addRequestedComponents')
            # else:
        req, created =Request.objects.get_or_create(member = get_member, requested = False)
        items= Requestcomponents.objects.filter (request=req)
        context = {
            'components':components,
            'member': get_member,
            'items':items,
            'request':req.id,
            'email': get_email
        }
        myTemplate = 'studio/requestComponents.html'
        return render(request, myTemplate, context)

    email = request.GET.get('email')
    request_id = request.GET.get('request')
    q = request.GET.get('q')

    if request_id:
        components = None
        if q:
            components = Component.objects.filter(name__icontains=q)
        if not components:
            components = Component.objects.all()
            messages.warning(
                request, f'No component was found')

        get_member = Member.objects.get(email=email)
        req, created = Request.objects.get_or_create(member = get_member, requested = False)
        items = Requestcomponents.objects.filter (request=req)
        context = {
            'components': components,
            'member': get_member,
            'items': items,
            'request': request_id,
            'email': email
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


def updateComponentRequest(request):
    data = json.loads(request.body)
    componentId = data['componentId']
    action = data['action']
    member = data['member']

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


def updateRequest(request,id):
    req = Request.objects.get(id=id)
    req.requested = True
    req.save()
    messages.success(request, f'Your request has been sent successfully!')
    return redirect(addRequestedComponents)

def updateRequestedComponents(request, id):
    instance = get_object_or_404(Requestcomponents,pk=id)
    
    if request.method == 'POST':
        get_quantity =request.POST.get('quantity')
        get_lab_component =request.POST.get('lab')

        try:
            labComponent = LabComponent.objects.get(id=get_lab_component)
        except LabComponent.DoesNotExist:
            messages.warning(request, f'{instance.component.name}-{instance.component.unit} was not found in selected lab')
            return redirect('updateRequestedComponents', id)

        if labComponent.quantity < int(get_quantity):
            messages.warning(request, f'Insuficient {instance.component.name}-{instance.component.unit} in {labComponent.lab.name}')
            return redirect('updateRequestedComponents', id)
        responseComponent = RespondedComponents(
            request = instance.request,
            labComponent = labComponent,
            quantity = get_quantity,
            status = "ACCEPTED"
        )
        responseComponent.save()
        instance.status = "ACCEPTED"
        instance.save()
        messages.success(request, f'Request accepted successfully!')
        return redirect('viewRequestedComponents')
    context = {
        'requestComponent': instance,
        # 'component':component
    }
    myTemplate = 'studio/updateRequestedComponent.html'
    return render(request, myTemplate, context)


@login_required
def issueComponents(request,id):
    issue = Requestcomponents.objects.get(id=id)
    issue.status = "Accepted"
    issue.save()
    return redirect("viewRequestedComponents")

@login_required
def declinedComponents(request,id):
    issue = Requestcomponents.objects.get(id=id)
    issue.status = "Declined"
    issue.save()
    return redirect(viewRequestedComponents)

@login_required
def viewAcceptedRequest(request):
    acceptedRequests = RespondedComponents.objects.filter(status = "ACCEPTED")

    context = {
        'acceptedRequests': acceptedRequests
        }
    myTemplate = 'studio/viewAcceptedComponents.html'
    return render(request, myTemplate, context)

def returnComponents(request,id):
    instance = get_object_or_404(RespondedComponents,pk=id)
    quantity = request.POST.get('quantity')
    try:
        ReturnedComponents.objects.create(
            respondedComponent_id = id,
            quantity = quantity,
            status  = 'Returned',
            responseDate = datetime.now()
        ).save()
        messages.success(request, f'Your component returned successfully!')
        return redirect('viewAcceptedRequest')
    except:
        messages.success(request, f'your request has failed')
        

    context = {
        'returnComponent': instance,       
    }
    myTemplate = 'studio/returnComponent.html'
    return render(request, myTemplate, context)
   
def viewReturnedComponents(request):
    returnedComponents = RespondedComponents.objects.filter(status = "Returned")

    context = {
        'returnedComponents': returnedComponents
        }
    myTemplate = 'studio/viewReturnedComponents.html'
    return render(request, myTemplate, context)


# ..........................................dashboard...................................
@login_required
def dashboard(request):
    members = Member.objects.all().count()
    chekin = CheckInAndout.objects.filter(status ="CHECK-IN" , date__date = datetime.now().date()).count()
    requestedComponent = Requestcomponents.objects.filter(status = None).count()
    totalUsers = CustomUser.objects.all().count()
    departments = Department.objects.all()

    context = {
        'members' : members,
        'checkin' : chekin,
        'requestedComponent': requestedComponent,
        'totalUsers':totalUsers,
        'departments' : departments
    }
    myTemplate = 'studio/dashboard.html'
    return render(request, myTemplate, context)

#.......................................... PAYMENT SETTINGS ........................
# def addPaymentSetting(request):
#     form = paymentSettingsForm(request.POST or None)
#     setting = PaymentSetting.objects.first()
#     if setting:
#         form = paymentSettingsForm(instance=setting)
#     if request.method == 'POST':
#         form = paymentSettingsForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Amount added successfully!')
#             return redirect('viewPaymentSetting')
#     context = {
#      'form': form,
#     }
#     myTemplate = 'studio/addPaymentSetting.html'
#     return render(request, myTemplate, context)

# def viewPaymentSetting(request):
#     allAmounts = PaymentSetting.objects.all()

#     context = {
#         'allAmounts': allAmounts
#     }
#     myTemplate = 'studio/viewPaymentSetting.html'
#     return render(request, myTemplate, context)

#.............................MEMBER PAYMENT...............................................
# def addMemberPayment(request):
#     form = MemberPaymentForm()
#     if request.method == 'POST':
#         form = MemberPaymentForm(request.POST or None)
#         get_amount = PaymentSetting.objects.first()
#         get_member = request.POST.get('member')
#         get_payment_date = request.POST.get('paymentDate')
#         expieryDate = pd.to_datetime(get_payment_date)+pd.DateOffset(years= 1)
#         remainingDays = (expieryDate - datetime.now()).days

#         if form.is_valid():
#             paymentRecord =  MemberPayment(
#                 member_id = get_member,
#                 amount = get_amount.amount,
#                 paymentDate = get_payment_date,
#                 expieryDate = expieryDate,
#                 remainingDays = remainingDays
#             )
#             paymentRecord.save()
#             messages.success(request, f'Member payment added successfully!')
#             return redirect('addMemberPayment')
#     context = {
#      'form': form,
#     }
#     myTemplate = 'studio/addMemberPayment.html'
#     return render(request, myTemplate, context)