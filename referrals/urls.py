from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.person_list, name='person_list'),
    path('my_patients/', views.my_person_list, name='my_person_list'),
    path('patients/<int:pk>/', views.person_delete, name='person_delete'),
    path('patients_detail/', views.person_detail, name='person_detail'),
    path('patients_detail/<int:pk>/', views.person_detail, name='person_detail'),
    path('patients_edit/', views.person_edit, name='person_edit'),
    path('patients_edit/<int:pk>/', views.person_edit, name='person_edit'),
    path('patients/', views.person_cancel, name='person_cancel'),
    path('patient_new/', views.person_new, name='person_new'),
    path('patient_new/<int:pk>/', views.person_new, name='person_new'),
    path('referrals/', views.referral_list, name='referral_list'), 
    path('my_referrals/', views.my_referral_list, name='my_referral_list'), 
    path('referrals_edit/', views.referral_edit, name='referral_edit'),
    path('referrals_edit/<int:person_id>/<int:referral_id>/', views.referral_edit, name='referral_edit'),
    path('referrals_new/', views.referral_new, name='referral_new'),
    path('referrals_new/<int:person_id>/', views.referral_new, name='referral_new'),
    path('global_referral_new/', views.global_referral_new, name='global_referral_new'),
    
    path('referrals_detail/', views.referral_detail, name='referral_detail'),
    path('referrals_detail/<int:referral_id>/', views.referral_detail, name='referral_detail'),
    path('view_document/<int:referral_id>/', views.view_document, name='view_document'),
    path('referrals/', views.referral_delete, name='referral_delete'),
    path('referrals/<int:person_id>/<int:referral_id>/', views.referral_delete, name='referral_delete'),
    path('login/', views.login_view, name='login_view'),
    path('my_page/', views.my_doctor_page, name='my_doctor_page'),
    
] 

#path('login/', views.login_view, name='login_view')
#path('persons/', views.person_cancel, name='person_cancel'),
#path('', views.home, name='home'),
#path('', include('nz_healthcare.urls')),