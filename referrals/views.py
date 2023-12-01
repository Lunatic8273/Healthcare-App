from django.shortcuts import render, get_object_or_404, redirect
from .models import Person, Referral, Doctor
from .forms import PersonForm, ReferralForm
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse
import os

@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')  # Redirect to the home page or any other desired page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'referrals/home.html')

def home(request):
    return render(request, 'referrals/home.html')
    
@login_required
def person_cancel(request):
    return render(request, 'referrals/person_list.html')    

@login_required
def my_person_list(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    persons = Person.objects.filter(GP=doctor.id)
    return render(request, 'referrals/my_person_list.html', {'doctor':doctor, 'persons': persons})

@login_required
def person_list(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    persons = Person.objects.all()
    return render(request, 'referrals/person_list.html', {'doctor':doctor, 'persons': persons})

@login_required
def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    referrals = Referral.objects.filter(person=person)
    return render(request, 'referrals/person_detail.html', {'person': person, 'referrals': referrals})

@login_required
def person_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.user = request.user
            person.save()
            return redirect('person_detail', pk=person.pk)
    else:
        form = PersonForm()
    return render(request, 'referrals/person_new.html', {'form': form})

@login_required
def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.user = request.user
            person.save()
            return redirect('person_detail', pk=person.pk)
    else:
        form = PersonForm(instance=person)
    return render(request, 'referrals/person_edit.html', {'form': form, 'person': person})
 

@login_required
def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('person_list')

@login_required
def referral_list(request):  
    referrals = Referral.objects.all()
    return render(request, 'referrals/referral_list.html', {'referrals': referrals})

@login_required
def referral_detail(request, referral_id):
    referral = get_object_or_404(Referral, id=referral_id)
    person = get_object_or_404(Person, id=referral.person.id)
    return render(request, 'referrals/referral_detail.html', {'person': person, 'referral': referral})
    
@login_required
def view_document(request, referral_id):
    referral = get_object_or_404(Referral, id=referral_id)
    if referral.document:
        with open(referral.document.path, 'rb') as document_file:
            response = HttpResponse(document_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename={referral.document.name}'
            return response
    else:
        return HttpResponse("Document not found", status=404)


@login_required
def referral_new(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == "POST":
        form = ReferralForm(request.POST)
        if form.is_valid():
            referral = form.save(commit=False)
            referral.person = person
            referral.save()
            return render(request, 'referrals/referral_detail.html',{'person': person, 'referral':referral})
    else:
        form = ReferralForm()
    return render(request, 'referrals/referral_new.html', {'form': form, 'person': person})

@login_required
def referral_edit(request, person_id, referral_id):
    referral = get_object_or_404(Referral, id=referral_id, person__id=person_id, person__user=request.user)
    if request.method == "POST":
        form = ReferralForm(request.POST, request.FILES, instance=referral)
        if form.is_valid():
            referral = form.save(commit=False)
            referral.person = referral.person
            referral.save()
            return redirect('referral_detail', referral_id=referral.pk)
    else:
        form = ReferralForm(instance=referral)
    return render(request, 'referrals/referral_edit.html', {'form': form, 'person': referral.person, 'referral':referral})

@login_required
def referral_delete(request, person_id, referral_id):
    referral = get_object_or_404(Referral, id=referral_id, person__id=person_id, person__user=request.user)
    referral.delete()
    return redirect('referral_list')
