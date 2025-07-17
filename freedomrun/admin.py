from django.contrib import admin
from django import forms
from django.db import models
from .models import Tshirt_Size, Individual, Team_Family, Member, Coupen ,Category
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from django.urls import reverse
from import_export.admin import ExportMixin, ExportActionMixin
from import_export.widgets import ForeignKeyWidget
from import_export import resources, fields
from django.conf import settings
admin.site.site_header = "Freedom Run"
admin.site.site_title = "Freedom Run"
admin.site.index_title = "Dashboard"

class IndividualResource(resources.ModelResource):
    # Define fields to export and customize as needed
    tshirt_size = fields.Field(
        column_name='tshirt_size',
        attribute='tshirt_size',
        widget=ForeignKeyWidget(Tshirt_Size, 'name')
    )

    class Meta:
        model = Individual
        # Specify fields to export
        fields = ('id', 'name', 'dob', 'email', 'category', 'gender', 'phone_no',
                  'area', 'tshirt_size', 'registration_fee', 'registered_date',
                  'is_paid', 'paid_date', 'paid_ref', 'paid_amount', 'chest_no')
        # Exclude 'id' (primary key of Individual) from export
        exclude = ('id',)



class IndividualAdmin(ImportExportModelAdmin):
    resource_class = IndividualResource
    
    search_fields = ['name', 'email','phone_no','tshirt_size__name','registered_date']
    list_display = ['name','chest_no','category', 'email','phone_no','tshirt_size','registered_date','is_paid','paid_ref']
    list_filter = ['registered_date','is_paid','category']

    
    def send_reminder(self, request, queryset):
        current_time = timezone.now()
        unpaid_individuals = queryset.filter(is_paid=False)
        for individual in unpaid_individuals:
            # Customize your email subject and body as needed

            subject = 'Payment Reminder'
            edit_url = "https://register.freedomrun.co.in{}{}".format(reverse('edit-individual-registration', args=[individual.id]), "?type=Individual")

            #edit_url = "http://127.0.0.1:8000{}?id={}&type=Individual".format(reverse('registration-status'), individual.id)
            message = f"Dear {individual.name},<br><br>This is a reminder that your payment for the event is still pending.<br><br>Please make sure to complete the payment as soon as possible to secure your participation.<br><br>Click <a href='{edit_url}'>here</a> to update your registration details."
            from_email = settings. DEFAULT_FROM_EMAIL# Update with your email
            to_email = [individual.email]

            # Send email
            send_mail(subject, '', from_email, to_email, html_message=message)

            # Update last reminder sent time
            individual.last_reminder_sent = current_time
            individual.save()

        self.message_user(request, "Reminders sent successfully.")
    send_reminder.short_description = "Send Reminder"

    actions = ['send_reminder']

class MemberInline(admin.TabularInline):  
    model = Member
    extra = 1

class Team_FamilyAdmin(ImportExportModelAdmin):
    search_fields = ['team_name','organization_name','no_of_persons','registered_date']
    list_display = ['team_name','organization_name','category','no_of_persons','registered_date','first_member_email','is_paid','paid_ref']
    list_filter = ['registered_date','is_paid','category']
    inlines = [MemberInline]
    actions = ['send_reminder']


    def send_reminder(self, request, queryset):
        current_time = timezone.now()
        unpaid_teams = queryset.filter(is_paid=False)
        for team in unpaid_teams:
            # Customize your email subject and body as needed
            subject = 'Payment Reminder'
            edit_url = "{}{}".format(reverse('edit-team-registration', args=[team.id]), "?type=Team")
            message = f"Dear {team.team_name},<br><br>This is a reminder that your payment for the event is still pending.<br><br>Please make sure to complete the payment as soon as possible to secure your participation.<br><br>Click <a href='{edit_url}'>here</a> to update your registration details."
            from_email = settings.DEFAULT_FROM_EMAIL # Update with your email
            to_email = [team.first_member_email]

            # Send email
            send_mail(subject, '', from_email, to_email, html_message=message)

            # Update last reminder sent time
            team.last_reminder_sent = current_time
            team.save()

        self.message_user(request, "Reminders sent successfully.")
    send_reminder.short_description = "Send Reminder"


class MemberResource(resources.ModelResource):
    # Define fields to export and customize as needed
    tshirt_size = fields.Field(
        column_name='tshirt_size',
        attribute='tshirt_size',
        widget=ForeignKeyWidget(Tshirt_Size, 'name')
    )



    class Meta:
        model = Member
        fields = ('name', 'dob', 'email', 'gender', 'phone_no',
                  'area', 'tshirt_size', 'registered_date', 'chest_no')
        export_order = ('name', 'dob', 'email', 'gender', 'phone_no',
                        'area', 'tshirt_size_name', 'registered_date', 'chest_no')



class MemberAdmin(ImportExportModelAdmin):
    resource_class = MemberResource
    search_fields = ['name', 'email','phone_no','tshirt_size__name','registered_date','team_family__team_name']
    list_display = ['chest_no','team_family','name', 'email','phone_no','tshirt_size','registered_date']
    list_filter = ['team_family']
    

class CoupenAdmin(ImportExportModelAdmin):
    search_fields = ['code']

#admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Tshirt_Size)
admin.site.register(Coupen, CoupenAdmin)
admin.site.register(Individual,IndividualAdmin)
admin.site.register(Team_Family,Team_FamilyAdmin)
admin.site.register(Member,MemberAdmin)