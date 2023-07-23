from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('addLab/', views.add_lab, name='addLab'),
    path('viewLab/', views.viewLab, name='viewLab'),
    path('delete/lab/<int:id>/', views.deleteLab, name='deleteLab'),
    path('addComponent/', views.addComponent, name='addComponent'),
    path('viewComponent/', views.viewComponent, name='viewComponent'),
    path('delete/component/<int:id>/', views.deleteComponent, name='deleteComponent'),
    path('addSourceOfIncome/', views.addSourceOfIncome, name='addSourceOfIncome'),
    path('viewSourceOfIncome/', views.viewSourceOfIncome, name='viewSourceOfIncome'),
    path('delete/SourceOfIncome/<int:id>/', views.deleteSourceOfIncome, name='deleteSourceOfIncome'),
    path('addIncome/', views.addIncome, name='addIncome'),
    path('viewIncome/', views.viewIncome, name='viewIncome'),
    path('delete/Income/<int:id>/', views.deleteIncome, name='deleteIncome'),
    path('addPurchase/', views.addPurchase, name='addPurchase'),
    path('viewPurchases/', views.viewPurchases, name='viewPurchases'),
    path('delete/Purchase/<int:id>/', views.deletePurchase, name='deletePurchase'),
    path('addSourceOfExpenses/', views.addSourceOfExpenses, name='addSourceOfExpenses'),
    path('viewSourceOfExpenses/', views.viewSourceOfExpenses, name='viewSourceOfExpenses'),
    path('delete/SourceOfExpenses/<int:id>/', views.deleteSourceOfExpenses, name='deleteSourceOfExpenses'),
    path('addExpenses/', views.addExpenses, name='addExpenses'),
    path('viewExpenses/', views.viewExpenses, name='viewExpenses'),
    path('delete/Expenses/<int:id>/', views.deleteExpenses, name='deleteExpenses'),
    path('addLocation/', views.addLocation, name='addLocation'),
    path('viewLocation/', views.viewLocation, name='viewLocation'),
    path('delete/Location/<int:id>/', views.deleteLocation, name='deleteLocation'),
    path('addMemberType/', views.addMemberType, name='addMemberType'),
    path('viewMemberType/', views.viewMemberType, name='viewMemberType'),
    path('delete/MemberType/<int:id>/', views.deleteMemberType, name='deleteMemberType'),
    path('addMember/', views.addMember, name='addMember'),
    path('viewMembers/', views.viewMembers, name='viewMembers'),
    path('delete/Student/<int:id>/', views.deleteMember, name='deleteMember'),

]
