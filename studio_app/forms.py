from django import forms
from .models import *


class addLabsForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = '__all__'

class updateLabsForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = '__all__'

class addComponentsForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = '__all__'

class updateComponentsForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = '__all__'

class addSourceOfIncomeForm(forms.ModelForm):
    class Meta:
        model = Source_of_Income
        fields = '__all__'

class addIncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'

        name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        widgets = {
            'date': forms.DateInput(attrs={'type':'date' }),
        }

class addPurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={'type':'date' }),
        }

class addSourceOfExpensesForm(forms.ModelForm):
    class Meta:
        model = Source_Of_Expenses
        fields = '__all__'

class addExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={'type':'date' }),
        }

        def __init__(self, *args, **kwargs):
            super(addExpensesForm, self).__init__(*args, **kwargs)
            self.fields['name','lab'].widget.attrs.update({'class': 'form-control'})

class updateExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'

class addSourceOfExpensesForm(forms.ModelForm):
    class Meta:
        model = Source_Of_Expenses
        fields = '__all__'

class addMemberTypeForm(forms.ModelForm):
    class Meta:
        model = Member_type
        fields = '__all__'

class addLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

class addMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('firstName','middleName', 'lastName', 'dateOfBirth', 'registrationNumber', 'phoneNumber', 'email', 'nationality', 'gender','type','location' )

        widgets = {
            'dateOfBirth': forms.DateInput(attrs={'type':'date' }),
        }

class addCheckInAndOutForm(forms.ModelForm):    
    class meta: 
        model = CheckInAndout  
        fields ='__all__'  

class addRequestForm(forms.ModelForm):    
    class Meta: 
        model = Request  
        fields =('email',)


# class addrequestedComponentsForm(forms.ModelForm):
#     components = Component.objects.all()    
#     component_choices  =(    
#     ( component.value, component.name ) for component in components ), 

#     comp =  forms.MultipleChoiceField(choices=component_choices)        
#     class Meta: 
#         model = Requestcomponents
#         fields =(comp,'quantity'  )

class addrequestedComponentsForm(forms.Form):
    OPTIONS = (
        ("AUT", "Austria"),
        ("DEU", "Germany"),
        ("NLD", "Neitherlands"),
    )
    Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)

