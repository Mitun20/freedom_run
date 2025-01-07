from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Individual, Team_Family , Member
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@receiver(post_save, sender=Individual)
def assign_chest_no_to_individual(sender, instance, **kwargs):
    if not instance.chest_no and instance.is_paid:  # Only assign if chest_no is not already set
        category = instance.category
        
        if category == "5 Km Walk":
            ind_last = Individual.objects.filter(category="5 Km Walk", chest_no__isnull=False).last()
            members_last = Member.objects.filter(team_family__category="5 Km Walk", chest_no__isnull=False).last()
        elif category == "5 Km Run":
            ind_last = Individual.objects.filter(category="5 Km Run", chest_no__isnull=False).last()
            members_last = Member.objects.filter(team_family__category="5 Km Run", chest_no__isnull=False).last()
        elif category == "10 Km Run":
            ind_last = Individual.objects.filter(category="10 Km Run", chest_no__isnull=False).last()
            members_last = Member.objects.filter(team_family__category="10 Km Run", chest_no__isnull=False).last()
        else:
            return  # Exit if category is not recognized

        ind_last_no = ind_last.chest_no if ind_last else 0
        member_last_no = members_last.chest_no if members_last else 0

        if category == "5 Km Walk":
            new_chest_no = max(ind_last_no, member_last_no) + 1 if ind_last_no or member_last_no else 1001
        elif category == "5 Km Run":
            new_chest_no = max(ind_last_no, member_last_no) + 1 if ind_last_no or member_last_no else 1001
        elif category == "10 Km Run":
            new_chest_no = max(ind_last_no, member_last_no) + 1 if ind_last_no or member_last_no else 5001

        instance.chest_no = new_chest_no
        instance.save()

@receiver(post_save, sender=Member)
def assign_chest_no_to_member(sender, instance, **kwargs):
    if not instance.chest_no :  # Only assign if chest_no is not already set
        team_family = instance.team_family
        if team_family.is_paid:
            
            category = team_family.category
            if category == "5 Km Walk":
                ind_last = Individual.objects.filter(category="5 Km Walk", chest_no__isnull=False).last()
                members_last = Member.objects.filter(team_family__category="5 Km Walk", chest_no__isnull=False).last()
            elif category == "5 Km Run":
                ind_last = Individual.objects.filter(category="5 Km Run", chest_no__isnull=False).last()
                members_last = Member.objects.filter(team_family__category="5 Km Run", chest_no__isnull=False).last()
            elif category == "10 Km Run":
                ind_last = Individual.objects.filter(category="10 Km Run", chest_no__isnull=False).last()
                members_last = Member.objects.filter(team_family__category="10 Km Run", chest_no__isnull=False).last()
            else:
                return  # Exit if category is not recognized

            ind_last_no = ind_last.chest_no if ind_last else 0
            member_last_no = members_last.chest_no if members_last else 0

            if category == "5 Km Walk":
                new_chest_no = max(ind_last_no, member_last_no) + 1 if ind_last_no or member_last_no else 1001
            elif category == "5 Km Run":
                new_chest_no = max(ind_last_no, member_last_no) + 1 if ind_last_no or member_last_no else 1001
            elif category == "10 Km Run":
                new_chest_no = max(ind_last_no, member_last_no) + 1 if ind_last_no or member_last_no else 5001

            instance.chest_no = new_chest_no
            instance.save()


    team = instance.team_family
    if not team.mail_sent:
        team.save()



@receiver(post_save, sender=Team_Family)
def assign_chest_no_to_member(sender, instance, **kwargs):
    
    team_family = instance
    if team_family.is_paid:
        
        category = team_family.category
        if category == "5 Km Walk":
            ind_last = Individual.objects.filter(category="5 Km Walk", chest_no__isnull=False).last()
            members_last = Member.objects.filter(team_family__category="5 Km Walk", chest_no__isnull=False).last()
        elif category == "5 Km Run":
            ind_last = Individual.objects.filter(category="5 Km Run", chest_no__isnull=False).last()
            members_last = Member.objects.filter(team_family__category="5 Km Run", chest_no__isnull=False).last()
        elif category == "10 Km Run":
            ind_last = Individual.objects.filter(category="10 Km Run", chest_no__isnull=False).last()
            members_last = Member.objects.filter(team_family__category="10 Km Run", chest_no__isnull=False).last()
        else:
            return  # Exit if category is not recognized

        ind_last_no = ind_last.chest_no if ind_last else 0
        member_last_no = members_last.chest_no if members_last else 0

        if category == "5 Km Walk":
            new_chest_no = max(ind_last_no, member_last_no) + 1 if ind_last_no or member_last_no else 1001
        elif category == "5 Km Run":
            new_chest_no = max(ind_last_no, member_last_no) + 1 if ind_last_no or member_last_no else 1001
        elif category == "10 Km Run":
            new_chest_no = max(ind_last_no, member_last_no) + 1 if ind_last_no or member_last_no else 5001

        for member in Member.objects.filter(team_family=team_family):
            if not member.chest_no:
                member.chest_no = new_chest_no
                member.save()
                new_chest_no = new_chest_no +1

    


@receiver(post_save, sender=Individual)
def send_registration_email_individual(sender, instance, created, **kwargs):
    if instance.is_paid and instance.paid_ref and instance.chest_no and not instance.mail_sent:
        print(f"Sending registration email to {instance.email}")
        
        # Determine the event details based on the selected location
        #selected_location = instance.location
        event_details =  {"date": "1st September 2024 (Sunday)", "time": "[5.30 am - 8.30 am]"}
        #"Chennai": {"date": "1st September 2024 (Sunday)", "time": "[5.30 am - 8.30 am]"}
        
        #selected_event_details = event_details.get(selected_location, None)
        
        # Ensure the selected location is valid
        
        #if selected_event_details:
    
        # Render the email HTML template with individual's details and event details
        html_content = render_to_string('registration_email_individual.html', {
            'instance': instance,
            'event_name': "Freedom Run 2024 - For Cyber Crime Against Women",
            'event_details':event_details,
        })
        
        # Create the plain text version of the email
        text_content = strip_tags(html_content)
        
        # Create the email message
        msg = EmailMultiAlternatives(
            subject='Registration Successful',
            body=text_content,
            from_email='admin@freedomrun.co.in',
            to=[instance.email],
        )
        msg.attach_alternative(html_content, "text/html")  # Attach HTML content
        
        # Send the email
        msg.send()
        instance.mail_sent =True
        instance.save()
        
        print("Registration email sent successfully.")


@receiver(post_save, sender=Team_Family)
def send_registration_email_team_family(sender, instance, created, **kwargs):
    if instance.is_paid and instance.paid_ref:
        first_member_email = instance.first_member_email
        first_member_chest_no = instance.first_member_chest_no
    
        if first_member_email and first_member_chest_no and not instance.mail_sent:
            print(f"Sending registration email to {first_member_email}")

            # Get the first member of the team
            first_member = instance.member_set.first()

            if first_member:
                # Determine the event details based on the first member's selected location
                #event_details = {}
                #if first_member.location == 'Coimbatore':
                event_details = {"date": "1st September 2024 (Sunday)", "time": "[5.30 am - 8.30 am]" ,"location": "Coimbatore"}
                #elif first_member.location == 'Chennai':
                    #event_details = {"date": "1st September 2024 (Sunday)", "time": "[5.30 am - 8.30 am]","location": "Chennai"}

                event_name = "Freedom Run 2024 - For Cyber Crime Against Women"

                # Render the HTML email template
                html_content = render_to_string('registration_email_team.html', {
                    'instance': instance,
                    'event_name': event_name,
                    'event_details': event_details,
                })

                # Create the plain text version of the email
                text_content = f"Dear {instance.team_name},\n\nCongratulations! You're now officially registered for the We Wonder Women event: {event_name}.\n\nWe are thrilled to have you join us in this empowering initiative dedicated to promoting women's safety and equality. Your participation makes a significant difference, and we can't wait to see you at the event."

                # Create the email message
                msg = EmailMultiAlternatives(
                    subject='Registration Successful',
                    body=text_content,  # Plain text version of the email
                    from_email='admin@freedomrun.co.in',
                    to=[first_member_email],
                )
                msg.attach_alternative(html_content, "text/html")  # Attach HTML content

                # Send the email
     
                if Team_Family.objects.filter(mail_sent=False,id=instance.pk,).exists():
                    msg.send()
                    Team_Family.objects.filter(id=instance.pk).update(mail_sent=True)

                print("Registration email sent successfully.")
            else:
                print("No members found for the team.")
        else:
            print("No first member email found.")


'''@receiver(post_save, sender=Team_Family)
def send_registration_email_team_family(sender, instance, created, **kwargs):
    if instance.is_paid and instance.paid_ref:
        first_member_email = instance.first_member_email
        if first_member_email:
            print(f"Sending registration email to {first_member_email}")
            
            event_name = "Freedom Run 2024 - For Women Safety & Equality"
            # HTML content of the email with black color text
            html_content = f"""
                <p style="color: black;">Dear <strong>{instance.team_name},</strong></p>

                <p style="color: black;"><strong>Congratulations!</strong> Your team registered for the <strong>We Wonder Women event: {event_name}</strong>.</p>

                <p style="color: black;">We are thrilled to have you join us in this empowering initiative dedicated to promoting women's safety and equality. Your participation makes a significant difference, and we can't wait to see you at the event.</p>

        
                """
            text_content = f"Dear {instance.team_name},\n\nCongratulations! You're now officially registered for the We Wonder Women event: {event_name}.\n\nWe are thrilled to have you join us in this empowering initiative dedicated to promoting women's safety and equality. Your participation makes a significant difference, and we can't wait to see you at the event."
            
            msg = EmailMultiAlternatives(
                subject='Registration Successful',
                body=text_content,  # Plain text version of the email
                from_email='admin@freedomrun.co.in',
                to=[first_member_email],
            )
            msg.attach_alternative(html_content, "text/html")  # Attach HTML content
        
            # Send the email
            msg.send()
        
            print("Registration email sent successfully.") '''


