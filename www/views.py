from django.shortcuts import render
from www.forms import PatientSignupForm, DoctorSignupForm, UserLogin
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from core.lib.user_management import create_doctor, create_patient
from core.models import UserProfile




def dan_home(request):
    return render(request, 'html/home.html')


def dan_waiting_room(request):
    pass

def dan_doctor_profile(request):
    pass



def landing_page(request):
    return render(request, 'jade/landing_page.jade')

def home_page(request):
    if request.user.is_authenticated():
        if request.user.groups.filter(name='doctor').count()==1:
            print 'user is part of the doctor group'
        if request.user.groups.filter(name='patient').count()==1:
            print 'user is part of the patient group'
    return landing_page(request)



def login_user(request):
    form = UserLogin(request.POST)
    if form.is_valid():
        user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])

        if user is None:
            form = UserLogin()
            return render(request, 'jade/landing_page.jade', {'form': form})

        login(request, user)
        return redirect('/')
    else:
        form = UserLogin()
    return render(request, 'jade/landing_page.jade', {'form': form})



def signup_doctor(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST)
        if form.is_valid():
            create_doctor(form.cleaned_data['email'], form.cleaned_data['password'])
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/')
    else:
        form = PatientSignupForm()
    return render(request, 'jade/doctor/signup.jade', {'form': form})


def signup_patient(request):
    if request.method == 'POST':
        form = PatientSignupForm(request.POST)
        if form.is_valid():
            create_patient(form.cleaned_data['email'], form.cleaned_data['password'])
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/')
    else:
        form = PatientSignupForm()
    return render(request, 'jade/patient/signup.jade', {'form': form})



def doctor_profile(request, username):
    is_logged_in = False
    is_patient = False
    is_doctor = False

    if request.user.is_authenticated():
        is_logged_in = True

    if request.user.username == username:
        is_doctor = True

    return render(request, 'jade/doctor/profile.jade',{'is_patient' : is_patient,
                                                      'is_logged_in' : is_logged_in,
                                                      'is_doctor' : is_doctor
                                                      })





"""
def landing_page(request):
	if request.user.is_authenticated():
		user_profile = UserProfile.objects.get(user=request.user)
		if user_profile.user_type == UserProfile.PATIENT:
			return render(request, 'jade/patient/home.jade')

		if user_profile.user_type == UserProfile.DOCTOR:
			return render(request, 'jade/doctor/home.jade')

	return render(request, 'jade/landing_page.jade')




def login_user(request):
    form = UserLogin(request.POST)
    if form.is_valid():
        user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])

        if user is None:
            form = UserLogin()
            return render(request, 'jade/landing_page.jade', {'form': form})

        login(request, user)
        return redirect('/')
    else:
        form = UserLogin()
    return render(request, 'jade/landing_page.jade', {'form': form})


def dashboard(request):
	if request.user.is_authenticated():
		user_profile = UserProfile.objects.get(user=request.user)
		if user_profile.user_type == UserProfile.PATIENT:
			return render(request, 'jade/patient/dashboard.jade')

		if user_profile.user_type == UserProfile.DOCTOR:
			return render(request, 'jade/doctor/dashboard.jade')

	return render(request, 'jade/landing_page.jade')

def profile(request):
	if request.user.is_authenticated():
		user_profile = UserProfile.objects.get(user=request.user)
		if user_profile.user_type == UserProfile.PATIENT:
			return render(request, 'jade/patient/profile.jade')

		if user_profile.user_type == UserProfile.DOCTOR:
			return render(request, 'jade/doctor/profile.jade')

	return render(request, 'jade/landing_page.jade')




def admin_dashboard(request):
    return render(request, 'jade/admin/dashboard.jade')


def doctor_profile(request, username):
    is_logged_in = False
    is_patient = False
    is_doctor = False

    if request.user.is_authenticated():
        is_logged_in = True

    if request.user.username == username:
        is_doctor = True


    return render(request, 'jade/doctor/profile.jade',{'is_patient' : is_patient,
                                                      'is_logged_in' : is_logged_in,
                                                      'is_doctor' : is_doctor
                                                      })

"""