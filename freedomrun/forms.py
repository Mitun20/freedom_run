from django import forms
from .models import Individual,Team_Family, Member ,Category, Tshirt_Size
from django.contrib import admin
from django.utils import timezone


#Base data form field

class Individual_Form(forms.ModelForm): 
    
    class Meta:
        model = Individual
        fields = ['name','dob','email','blood_group','gender','phone_no','additional_ph_no','area','category','tshirt_size','registration_fee']

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'max': '2019-12-31'}),
        }

    def __init__(self, *args, **kwargs):
        super(Individual_Form, self).__init__(*args, **kwargs)
        # Set the 'your_field_name' field as disabled
        
        # Set the 'area' field to "Chennai" and make it readonly
        self.fields['area'].initial = 'Chennai'
        self.fields['area'].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control'})
        self.fields['tshirt_size'].queryset = Tshirt_Size.objects.all().order_by('length_inch')
        
        # Apply 'form-control' class to all fields
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class': 'form-control'}) 

        self.fields['registration_fee'].disabled = True
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class': 'form-control'}) 

        self.fields['category'].choices = [choice for choice in self.fields['category'].choices] #if choice[0] != '10 KM'
    
    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        if category == '10 KM Run':
            cleaned_data['registration_fee'] = 700.00
        elif category == '5 KM Run':
            cleaned_data['registration_fee'] = 500.00
        elif category == '5 KM Walk':
            cleaned_data['registration_fee'] = 500.00
        else:
            cleaned_data['registration_fee'] = 500.00  # Default fee
        return cleaned_data
            
class Individual_cbe_Form(forms.ModelForm): 
    
    class Meta:
        model = Individual
        fields = ['name','dob','email','blood_group','gender','phone_no','additional_ph_no','area','category','tshirt_size','registration_fee']

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'max': '2019-12-31'}),
        }

    def __init__(self, *args, **kwargs):
        super(Individual_cbe_Form, self).__init__(*args, **kwargs)
        # Set the 'your_field_name' field as disabled
        
        # Set the 'area' field to "Chennai" and make it readonly
        self.fields['area'].initial = 'Coimbatore'
        self.fields['area'].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control'})
        
        # Sort tshirt_size in ascending order by name
        self.fields['tshirt_size'].queryset = Tshirt_Size.objects.all().order_by('length_inch')
        
        # Apply 'form-control' class to all fields
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class': 'form-control'}) 

        self.fields['registration_fee'].disabled = True
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class': 'form-control'}) 

        self.fields['category'].choices = [choice for choice in self.fields['category'].choices] #if choice[0] != '10 KM'
    
    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        if category == '10 KM Run':
            cleaned_data['registration_fee'] = 700.00
        elif category == '5 KM Run':
            cleaned_data['registration_fee'] = 500.00
        elif category == '5 KM Walk':
            cleaned_data['registration_fee'] = 500.00
        else:
            cleaned_data['registration_fee'] = 500.00  # Default fee
        return cleaned_data

class TeamFamilyForm(forms.ModelForm):
    class Meta:
        model = Team_Family
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(TeamFamilyForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = [choice for choice in self.fields['category'].choices if choice[0] != '10 KM']
    

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ('team_family',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default value for 'area' field to "Chennai"
        self.fields['area'].initial = 'Chennai'
        self.fields['tshirt_size'].queryset = Tshirt_Size.objects.all().order_by('length_inch')
MemberFormSet = forms.modelformset_factory(Member, form=MemberForm, extra=1)

class MemberFormCbe(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ('team_family',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default value for 'area' field to "Chennai"
        self.fields['area'].initial = 'Coimbatore'
        self.fields['tshirt_size'].queryset = Tshirt_Size.objects.all().order_by('length_inch')
MemberFormSetCbe = forms.modelformset_factory(Member, form=MemberFormCbe, extra=1)
