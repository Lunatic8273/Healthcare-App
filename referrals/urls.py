from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Home
    path('', views.home, name='home'),
    #About Page
    path('about_page', views.about_page, name='about_page'),
    #Staff Page
    path('our_staff', views.our_staff, name='our_staff'),
    #Login
    path('login/', views.login_view, name='login_view'),
    #Patient Profile Page
    path('patient_profile/', views.patient_profile, name='patient_profile'),
    #Doctor Profile Page
    path('my_page/', views.my_doctor_page, name='my_doctor_page'),
    path('my_page/<int:pk>/', views.doctor_page, name='doctor_page'),
    #Add Doctor details as a the doctor
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    #Edit Doctor details as a the doctor
    path('edit_doctor/', views.edit_doctor, name='edit_doctor'),
    #Patient List
    path('patients/', views.patient_list, name='patient_list'),
    #Doctors Patient List
    path('my_patients/', views.my_patient_list, name='my_patient_list'),
    #Delete Patient
    path('patients/<int:pk>/', views.patient_delete, name='patient_delete'),
    #Patient Details
    path('patients_detail/<int:pk>/', views.patient_detail, name='patient_detail'),
    #Patient Edit
    path('patients_edit/', views.patient_edit, name='patient_edit'),
    path('patients_edit/<int:pk>/', views.patient_edit, name='patient_edit'),
    path('patient_patient_edit/<int:pk>/', views.patient_patient_edit, name='patient_patient_edit'),
    #Patient Cancel Form
    path('patients/', views.patient_cancel, name='patient_cancel'),
    #Create new Patient
    path('patient_new/', views.patient_new, name='patient_new'),
    path('patient_new/<int:pk>/', views.patient_new, name='patient_new'),
    #Create new Patient as Doctor
    path('doctor_patient_new/', views.doctor_add_patient_new, name='doctor_add_patient_new'),
    #Referral List
    path('referrals/', views.referral_list, name='referral_list'), 
    #Doctors Referral List
    path('my_referrals/', views.my_referral_list, name='my_referral_list'), 
    #Edit A referral
    path('referrals_edit/<int:patient_id>/<int:referral_id>/', views.global_referral_edit, name='global_referral_edit'),
    #Create a new Referral
    path('referrals_new/', views.doctor_referral_new, name='doctor_referral_new'),
    path('referrals_new/<int:patient_id>/', views.patient_referral_new, name='patient_referral_new'),
    path('global_referral_new/', views.global_referral_new, name='global_referral_new'),
    #Referral Details
    path('referrals_detail/', views.referral_detail, name='referral_detail'),
    path('referrals_detail/<int:referral_id>/', views.referral_detail, name='referral_detail'),
    #Delete a Referral
    path('referrals/', views.referral_delete, name='referral_delete'),
    path('referrals/<int:patient_id>/<int:referral_id>/', views.referral_delete, name='referral_delete'),
    #View an Attached Document
    path('view_document/<int:referral_id>/', views.view_document, name='view_document'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#path('patients_detail/', views.patient_detail, name='patient_detail'),