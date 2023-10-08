from . import views
from django.urls import path

# app_name = 'studio_app'

urlpatterns = [
    path('', views.addRequestedComponents, name='addRequestedComponents'),
    path('dashboard/', views.dashboard, name='dashboard'),
   

    #............................lab...................................
    path('addLab/', views.add_lab, name='addLab'),
    path('viewLab/', views.viewLab, name='viewLab'),
    path('delete/lab/<int:id>/', views.deleteLab, name='deleteLab'),
    path('update/lab/<int:id>/', views.updateLab, name='updateLab'),
   
    #...........................components.............................
    path('addComponent/', views.addComponent, name='addComponent'),
    path('viewComponent/', views.viewComponent, name='viewComponent'),
    path('delete/component/<int:id>/', views.deleteComponent, name='deleteComponent'),
    path('update/component/<int:id>/', views.updateComponent, name='updateComponent'),

    #.............................Departments.................................
     path('addDepartment/', views.addDepartment, name='addDepartment'),
     path('viewDepartment/', views.viewDepartment, name='viewDepartment'),
     path('updateDepartment/<int:id>/', views.updateDepartment, name='updateDepartment'),
     path('deleteDepartment/<int:id>/', views.deleteDepartment, name='deleteDepartment'),

    #....................................source ofincome........................
    path('addSourceOfIncome/', views.addSourceOfIncome, name='addSourceOfIncome'),
    path('viewSourceOfIncome/', views.viewSourceOfIncome, name='viewSourceOfIncome'),
    path('delete/SourceOfIncome/<int:id>/', views.deleteSourceOfIncome, name='deleteSourceOfIncome'),
    path('update/SourceOfIncome/<int:id>/', views.updateSourceOfIncome, name='updateSourceOfIncome'),

    #..................................income.............................
    path('addIncome/', views.addIncome, name='addIncome'),
    path('viewIncome/', views.viewIncome, name='viewIncome'),
    path('delete/Income/<int:id>/', views.deleteIncome, name='deleteIncome'),
    path('update/Income/<int:id>/', views.updateIncome, name='updateIncome'),

    #...........................purchases.........................
    path('addPurchase/', views.addPurchase, name='addPurchase'),
    path('viewPurchases/', views.viewPurchases, name='viewPurchases'),
    path('delete/Purchase/<int:id>/', views.deletePurchase, name='deletePurchase'),
    path('update/Purchase/<int:id>/', views.updatePurchases, name='updatePurchases'),
    
    path('addSourceOfExpenses/', views.addSourceOfExpenses, name='addSourceOfExpenses'),
    path('viewSourceOfExpenses/', views.viewSourceOfExpenses, name='viewSourceOfExpenses'),
    path('delete/SourceOfExpenses/<int:id>/', views.deleteSourceOfExpenses, name='deleteSourceOfExpenses'),
    path('update/SourceOfExpenses/<int:id>/', views.updateExpensesSource, name='updateExpensesSource'),
    
    path('addExpenses/', views.addExpenses, name='addExpenses'),
    path('viewExpenses/', views.viewExpenses, name='viewExpenses'),
    path('delete/Expenses/<int:id>/', views.deleteExpenses, name='deleteExpenses'),
    path('update/Expenses/<int:id>/', views.updateExpenses, name='updateExpenses'),
    
    path('addLocation/', views.addLocation, name='addLocation'),
    path('viewLocation/', views.viewLocation, name='viewLocation'),
    path('delete/Location/<int:id>/', views.deleteLocation, name='deleteLocation'),
    path('update/Location/<int:id>/', views.updateLocation, name='updateLocation'),
    
    path('addMemberType/', views.addMemberType, name='addMemberType'),
    path('viewMemberType/', views.viewMemberType, name='viewMemberType'),
    path('delete/MemberType/<int:id>/', views.deleteMemberType, name='deleteMemberType'),
    path('update/MemberType/<int:id>/', views.updateMemberType, name='updateMemberType'),
    
    path('addMember/', views.addMember, name='addMember'),
    path('viewMembers/', views.viewMembers, name='viewMembers'),
    path('delete/Member/<int:id>/', views.deleteMember, name='deleteMember'),
    path('update/Member/<int:id>/', views.updateMember, name='updateMember'),
    
    path('checkInAndOut/', views.viewCheck, name='checkInAndOut'),
    path('addCheckInAndOut/<int:member_id>', views.addCheckInAndOut, name='addCheckInAndOut'),
    path('viewCheckInAndOut/', views.viewCheckedInAndOut, name='viewCheckedInAndOut'),
    
    path('viewRequestedComponents/', views.viewRequestedComponents, name='viewRequestedComponents'),
    path('updateRequestedComponents/<int:id>/', views.updateRequestedComponents, name='updateRequestedComponents'),
    path('updateComponentRequest/', views.updateComponentRequest, name='updateComponentRequest'),
    path('updateRequest/<int:id>/', views.updateRequest, name='updateRequest'),
    path('issueComponents/<int:id>/', views.issueComponents, name='issueComponents'),
    path('declinedComponents/<int:id>/', views.declinedComponents, name='declinedComponents'),


    path('returnComponents/<int:id>/', views.returnComponents, name='returnComponents'),
    path('viewAcceptedRequest/', views.viewAcceptedRequest, name='viewAcceptedRequest'),
    path('viewReturnedComponents/', views.viewReturnedComponents, name='viewReturnedComponents'),


    path('addPaymentSetting/', views.addPaymentSetting, name='addPaymentSetting'),
    path('viewPaymentSetting/', views.viewPaymentSetting, name='viewPaymentSetting'),

]
