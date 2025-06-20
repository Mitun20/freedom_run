from django.db import models
from decimal import Decimal
# Create your models here.
BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]
gender_choices = [
    ('', 'Choose Gender'),
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
]
category_choices =[
    ('', 'Choose category '),
    ('10 KM Run', '10 KM Run'),
    ('5 KM Run', '5 KM Run'),
    ('5 KM Walk', '5 KM Walk'),
    
    
]
'''location_choices = [
    ('', 'Choose location'),
    ('Coimbatore', 'Coimbatore'),
    ('Chennai', 'Chennai'),
    
]'''

'''class Location(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name '''

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Coupen(models.Model):
    code = models.CharField(max_length=20)
    #percentage = models.IntegerField(default=0)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    

class Tshirt_Size(models.Model):
    name = models.CharField(max_length=250)
    chest_inch = models.BigIntegerField(null=True)
    length_inch = models.BigIntegerField(null=True)

    def __str__(self):
        return self.name

class Individual(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    email = models.EmailField()
    blood_group = models.CharField( max_length=10, choices=BLOOD_GROUP_CHOICES, default="O+",null=True,blank=True)
    #location = models.CharField(max_length=50,choices=location_choices)
    category = models.CharField(max_length=20,choices=category_choices,null=True,default="")
    gender = models.CharField(max_length=1,choices=gender_choices)
    phone_no = models.CharField(max_length=10)
    additional_ph_no = models.CharField(max_length=10, blank=True, null=True)
    area = models.TextField()
    tshirt_size = models.ForeignKey(Tshirt_Size,on_delete=models.SET_NULL,null=True)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2,default=500.00)
    registered_date = models.DateField(auto_now=True,null=True)

    is_paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True,blank=True)
    paid_ref = models.CharField(max_length=100,null=True,blank=True)
    paid_amount = models.IntegerField(default=0)
    chest_no = models.IntegerField(null=True, blank=True)
    mail_sent = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    
    def get_paid_amount(self):
        return self.paid_amount
    
        
class Team_Family(models.Model):
    team_name = models.CharField(max_length=250)
    organization_name = models.CharField(max_length=250,null=True,blank=True)
    category = models.CharField(max_length=20,choices=category_choices,null=True,default="")
    no_of_persons = models.BigIntegerField()
    registered_date = models.DateField(auto_now=True,null=True)
    fees = models.IntegerField(default=0)
    
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True,blank=True)
    paid_ref = models.CharField(max_length=100,null=True,blank=True)
    paid_amount = models.IntegerField(default=0)
    mail_sent = models.BooleanField(default=False)


    def __str__(self):
        return self.team_name
    
    @property
    def first_member_email(self):
        first_member = self.member_set.first()
        if first_member:
            return first_member.email
        return None
    

    @property
    def first_member_chest_no(self):
        first_member = self.member_set.first()
        if first_member:
            return first_member.chest_no
        return None


    @property
    def first_member_phone(self):
        first_member = self.member_set.first()
        if first_member:
            return first_member.phone_no
        return None

class Member(models.Model):
    team_family = models.ForeignKey(Team_Family,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=250,null=False)
    dob = models.DateField()
    email = models.EmailField()
    blood_group = models.CharField( max_length=10, choices=BLOOD_GROUP_CHOICES, default="O+",null=True,blank=True)
    #location = models.CharField(max_length=50 ,choices=location_choices)
    gender = models.CharField(max_length=1,choices=gender_choices)
    phone_no = models.CharField(max_length=10)
    additional_ph_no = models.CharField(max_length=10, blank=True, null=True)
    area = models.TextField()
    tshirt_size = models.ForeignKey(Tshirt_Size,on_delete=models.SET_NULL,null=True)
    registered_date = models.DateField(auto_now=True,null=True)
    chest_no = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.name
    