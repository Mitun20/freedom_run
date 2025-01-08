from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import Individual_Form, TeamFamilyForm, MemberForm ,MemberFormSet
from .models import Team_Family, Member, Tshirt_Size ,Individual, Coupen ,Category
from django.forms.models import inlineformset_factory
from decimal import Decimal
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def registration_status(request):
    id = request.GET.get('id')
    registration_type = request.GET.get('type')
    if  registration_type == 'Individual':        
        individual = get_object_or_404(Individual, id=id)
        name = individual.name
        amount = individual.paid_amount
        paid_ref = individual.paid_ref
        chest_no = individual.chest_no
        category = individual.category
    else:
        team_object = get_object_or_404(Team_Family, id=id)
        amount = team_object.paid_amount
        name = team_object.team_name
        paid_ref = team_object.paid_ref
        chest_no = None
        category = team_object.category
    context = {
        'chest_no':chest_no,
        'amount': amount,
        'name':name,
        'paid_ref':paid_ref,
        'category':category,
        }
    return render(request, 'reg_status.html', context)

def registration(request):
    t_shirt_sizes = Tshirt_Size.objects.all()

    if request.method == "POST":
        form = Individual_Form(request.POST)
        if form.is_valid():
            data=form.save()
            
            return redirect(reverse('registration-status') + f'?id={data.id}&type=Individual')
    else:  # GET request
        form = Individual_Form()

    context = {
        'individual_form': form,
        'operation': "add",
        "t_shirt_sizes":t_shirt_sizes
    }
    return render(request, 'index.html', context)

def team_registration(request):
    if request.method == "POST":
        
        team_name = request.POST.get('team_name')
        org_name = request.POST.get('org_name')
        total_members = int(request.POST.get('total_members'))
        fees = int(request.POST.get('amount'))
        category = request.POST.get('category')
        print(category)
        print("#############################################")
    
        if category == '5 Km Walk':
            fee_per_member = 1
        elif category == '5 Km Run':
            fee_per_member = 1
        elif category == '10 Km Run':
            fee_per_member = 1
        else:
            fee_per_member = 1  

        total_fees = fee_per_member * total_members

        
        # Create Team_Family instance
        team_family_instance = Team_Family.objects.create(
            team_name=team_name,
            organization_name=org_name,
            no_of_persons=total_members,
            category=category,
            fees=total_fees,
        )
        
        member_name_list = request.POST.getlist(f'name[1]')
        member_dob_list = request.POST.getlist(f'dob[]')
        member_email_list = request.POST.getlist(f'email[]')
        #member_location_list = request.POST.getlist(f'location[]')
        member_blood_group_list = request.POST.getlist(f'blood_group[]')
        member_gender_list = request.POST.getlist(f'gender[]')
        member_phone_list = request.POST.getlist(f'phone[]')
        member_additional_ph_no_list = request.POST.getlist(f'additional_ph_no[]')
        member_area_list = request.POST.getlist(f'address[]')
        member_tshirt_size_list = request.POST.getlist(f't_shirt_size[]')
        
        for i in range(total_members):
            tshirt_size = Tshirt_Size.objects.get(pk=int(member_tshirt_size_list[i]))

            if member_gender_list[i] == "male":
                gender = "M"
            elif member_gender_list[i] == "female":
                gender = "F"
            else:
                gender = "O"

            member_data = {
                'team_family_id': team_family_instance.id,
                'name': member_name_list[i],
                'dob': member_dob_list[i],
                'email': member_email_list[i],
                'blood_group': member_blood_group_list[i],
                'gender': gender,
                'phone_no': member_phone_list[i],
                'additional_ph_no':member_additional_ph_no_list[i],
                'area': member_area_list[i],
                'tshirt_size_id': member_tshirt_size_list[i],
                
            }
      
            print(member_data)
            Member.objects.create(**member_data)            
        #return render(request, 'index.html', {'success_message': 'Payment successful!', 'amount': fees, 'name': team_name, 'team': True})
        return redirect(reverse('registration-status') + f'?id={team_family_instance.id}&type=Team')
    else:
        
        return render(request, 'team.html')


def edit_individual_registration(request, individual_id):
    individual = get_object_or_404(Individual, id=individual_id)

    if individual.category == "5 Km Walk":
        amount = 1
    elif individual.category == "5 Km Run":
        amount = 1
    elif individual.category == "10 Km Run":
        amount = 1

    individual.registration_fee = amount
    individual.save()

    if individual.is_paid: 
        return HttpResponse("Payment has already been made")

    t_shirt_sizes = Tshirt_Size.objects.all()
    individual_id = individual_id
    if request.method == "POST":
        form = Individual_Form(request.POST, instance=individual)
        if form.is_valid():
            form.save()
            return redirect(reverse('registration-status') + f'?id={individual_id}&type=Individual')
    else:  
        form = Individual_Form(instance=individual)


    if individual.category == "5 Km Walk":
        amount = 1
    elif individual.category == "5 Km Run":
        amount = 1
    elif individual.category == "10 Km Run":
        amount = 1

   
    context = {
        'individual_form': form,
        'individual_id': individual_id,
        'operation': "edit",
        "t_shirt_sizes": t_shirt_sizes,
        'registration_type': "Individual",
        "amount":int(individual.registration_fee),
        
    }
    return render(request,'individual.html', context) 


def edit_team_registration(request, team_id):
    team = get_object_or_404(Team_Family, id=team_id)

    if team.is_paid:
        return HttpResponse("Payment has already been made")
        
    else:
        team_id=team_id
        t_shirt_sizes = Tshirt_Size.objects.all()
        # Define formset with the appropriate queryset filter
        MemberFormSet = inlineformset_factory(Team_Family, Member, fields=('name', 'dob', 'email', 'gender', 'phone_no', 'area', 'tshirt_size'), extra=1)

        if request.method == "POST":
            team_form = TeamFamilyForm(request.POST, instance=team)
            member_formset = MemberFormSet(request.POST, instance=team)  # Pass the instance of team
            if team_form.is_valid() and member_formset.is_valid():
                team_form.save()
                member_formset.save()
                return redirect(reverse('registration-status') + f'?id={team_id}&type=Team')
        else:
            team_form = TeamFamilyForm(instance=team)
            # Filter member queryset based on the team
            member_formset = MemberFormSet(instance=team, queryset=Member.objects.filter(team_family=team))

        context = {
            'team_form': team_form,
            'member_formset': member_formset,
            'operation':"edit",
            'registration_type':"Team", 
            'team_id': team_id,    
            't_shirt_sizes':t_shirt_sizes, 
            'amount':int(team.fees),
            'team':team
        }
    return render(request,'team.html', context)


'''
def edit_team_registration(request, team_id):
    team = get_object_or_404(Team_Family, id=team_id)

    if request.method == "POST":
        team_form = TeamFamilyForm(request.POST, instance=team)
        member_formset = MemberFormSet(request.POST)
        if team_form.is_valid() and member_formset.is_valid():
            team_form.save()
            member_formset.instance = team  # Set the instance for the formset
            member_formset.save()
            return redirect(reverse('registration-status') + f'?id={team_id}&type=Team')
    else:
        team_form = TeamFamilyForm(instance=team)
        member_formset = MemberFormSet()

    context = {
        'team_form': team_form,
        'member_formset': member_formset,
        'operation': "edit",
    }
    return render(request, 'team.html', context)'''

'''def edit_team_registration(request, team_id):
    team = get_object_or_404(Team_Family, id=team_id)
    member_formset = MemberFormSet(instance=team)

    if request.method == "POST":
        team_form = TeamFamilyForm(request.POST, instance=team)
        if team_form.is_valid() and member_formset.is_valid():
            team_form.save()
            member_formset.save()
            return redirect(reverse('registration-status') + f'?id={team_id}&type=Team')
    else:
        team_form = TeamFamilyForm(instance=team)

    context = {
        'team_form': team_form,
        'member_formset': member_formset,
        'operation': "edit",
    }
    return render(request, 'team.html', context)'''



def ajax_submit(request):
    if request.method == "POST":
        individual_id = request.POST.get('individual_id',None)
        if individual_id:
            individual_object = Individual.objects.get(id=individual_id)
            paid_ref = request.POST.get('paid_ref',None)
            paid_fees = request.POST.get('paid_fees',None)
            if paid_fees:
                paid_fees = round(float(paid_fees))
            current_date = datetime.now().date()
            if paid_ref:
                individual_object.is_paid = True
                individual_object.paid_ref = paid_ref
                individual_object.paid_date = current_date
                individual_object.paid_amount = paid_fees
                individual_object.save()
                return JsonResponse({'is_paid':True})
            else:
                return JsonResponse({'obj_id':individual_object.id}) 

        else:
            form = Individual_Form(request.POST)
            if form.is_valid():
                data=form.save()
                return JsonResponse({'obj_id':data.id})  
            else:
                print(form.errors.as_data())              

    else:
        pass


def ajax_team_submit(request):
    if request.method == "POST":
        individual_id = request.POST.get('team',None)
        if individual_id:
            individual_object = Team_Family.objects.get(id=individual_id)
            paid_ref = request.POST.get('team_paid_ref',None)
            current_date = datetime.now().date()
            paid_fees = request.POST.get('paid_fees',None)
            category = request.POST.get('category')
            print(category,'category')
            if paid_ref:
                individual_object.is_paid = True
                individual_object.paid_ref = paid_ref
                individual_object.paid_date = current_date
                individual_object.paid_amount = paid_fees
                individual_object.save()
                return JsonResponse({'is_paid':True})
            else:
                return JsonResponse({'obj_id':individual_object.id})  

        else:

            team_name = request.POST.get('team_name')
            org_name = request.POST.get('org_name')
            total_members = int(request.POST.get('total_members'))
            fees = request.POST.get('amount')
            category = request.POST.get('category')

            # Create Team_Family instance
            team_family_instance = Team_Family.objects.create(
                team_name=team_name,
                organization_name=org_name,
                no_of_persons=total_members,
                fees=fees,
                category=category,
            )
            
            member_name_list = request.POST.getlist(f'name[1]')
            member_dob_list = request.POST.getlist(f'dob[]')
            member_email_list = request.POST.getlist(f'email[]')
            member_blood_group_list = request.POST.getlist(f'blood_group[]')
            #member_location_list = request.POST.getlist(f'location[]')
            member_gender_list = request.POST.getlist(f'gender[]')
            member_phone_list = request.POST.getlist(f'phone[]')
            member_additional_ph_no_list = request.POST.getlist(f'additional_ph_no[]')
            member_area_list = request.POST.getlist(f'address[]')
            member_tshirt_size_list = request.POST.getlist(f't_shirt_size[]')
            print(member_tshirt_size_list,'size')
            print(total_members,'total_members')
            
            
            for i in range(total_members):
                
                tshirt_size = Tshirt_Size.objects.get(pk=int(member_tshirt_size_list[i]))

                if member_gender_list[i] == "male":
                    gender = "M"
                elif member_gender_list[i] == "female":
                    gender = "F"
                else:
                    gender = "O"

                member_data = {
                    'team_family_id': team_family_instance.id,
                    'name': member_name_list[i],
                    'dob': member_dob_list[i],
                    'email': member_email_list[i],
                    'blood_group': member_blood_group_list[i],
                    #'location': member_location_list[i],
                    'gender': gender,
                    'phone_no': member_phone_list[i],
                    'additional_ph_no':member_additional_ph_no_list[i],
                    'area': member_area_list[i],
                    'tshirt_size_id': member_tshirt_size_list[i]
                }
        
      
                Member.objects.create(**member_data)            
            #return render(request, 'index.html', {'success_message': 'Payment successful!', 'amount': fees, 'name': team_name, 'team': True})

            return JsonResponse({'obj_id':team_family_instance.id})                

    else:
        pass

@csrf_exempt
def check_coupon(request):
    code = request.POST.get('code',None)
    data = dict()
    try:
        obj = Coupen.objects.get(code=code)
        data['valid_code'] = True
        data['percentage'] = obj.percentage
    except:       
        data['valid_code'] = False
    
    return JsonResponse(data)



def cancellation_policy(request):
    return render(request, 'cancellation-policy.html',)

def privacy_policy(request):
    return render(request, 'privacy-policy.html',)


def shipping_policy(request):
    return render(request, 'shipping-policy.html',)



def terms_conditions(request):
    return render(request, 'terms-conditions.html',)

def testing(request):

    t_shirt_sizes = Tshirt_Size.objects.all()

    if request.method == "POST":
        form = Individual_Form(request.POST)
        if form.is_valid():
            data=form.save()
            
            return redirect(reverse('registration-status') + f'?id={data.id}&type=Individual')
    else:  # GET request
        form = Individual_Form()

    context = {
        'individual_form': form,
        'operation': "add",
        "t_shirt_sizes":t_shirt_sizes
    }
    return render(request, 'testing.html',context)


def contact_us(request):
    return render(request, 'contact.html',)

