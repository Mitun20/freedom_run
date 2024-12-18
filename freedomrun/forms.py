from django import forms
from .models import Individual,Team_Family, Member ,Category
from django.contrib import admin
from django.utils import timezone


#Base data form field

class Individual_Form(forms.ModelForm): 
    
    class Meta:
        model = Individual
        fields = ['name','dob','email','gender','phone_no','area','category','tshirt_size','registration_fee']

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'max': '2018-12-31'}),
        }

    def __init__(self, *args, **kwargs):
        super(Individual_Form, self).__init__(*args, **kwargs)
        # Set the 'your_field_name' field as disabled
        self.fields['registration_fee'].disabled = True
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class': 'form-control'}) 

        self.fields['category'].choices = [choice for choice in self.fields['category'].choices] #if choice[0] != '10 Km'
    
    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        if category == '5km':
            cleaned_data['registration_fee'] = 500.00
        elif category == '10km':
            cleaned_data['registration_fee'] = 700.00
        else:
            cleaned_data['registration_fee'] = 500.00  # Default fee
        return cleaned_data
            

class TeamFamilyForm(forms.ModelForm):
    class Meta:
        model = Team_Family
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(TeamFamilyForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = [choice for choice in self.fields['category'].choices if choice[0] != '10 Km']
    

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ('team_family',)

MemberFormSet = forms.modelformset_factory(Member, form=MemberForm, extra=1)
