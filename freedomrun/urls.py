from django.urls import path
from . import views


urlpatterns = [
    path('',views.registration, name="home"),
    path('ajax-submit',views.ajax_submit, name="ajax-submit"),
    path('ajax-team-submit',views.ajax_team_submit, name="ajax-team-submit"),
    path('check-coupon',views.check_coupon, name="check-coupon"),

    path('freedomrun/',views.registration, name="registration"),
    path('registration-status/', views.registration_status, name='registration-status'),
    path('team/', views.team_registration, name="team_registration"),
    path('individual/<int:individual_id>/edit/', views.edit_individual_registration, name='edit-individual-registration'),
    path('team/<int:team_id>/edit/', views.edit_team_registration, name='edit-team-registration'),
    #path('edit/<str:registration_type>/<int:id>/',views.edit_registration, name="edit_registration"),

    path('cancellation-policy/',views.cancellation_policy, name="cancellation-policy"),
    path('privacy-policy/',views.privacy_policy, name="privacy-policy"),
    path('shipping-policy/',views.shipping_policy, name="shipping-policy"),
    path('terms-conditions/',views.terms_conditions, name="terms-conditions"),
    path('testing/',views.testing, name="testing"),
    path('contact-us/',views.contact_us, name="contact-us"),

    
]
