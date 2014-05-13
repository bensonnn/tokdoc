from django.http import HttpResponse
from django.contrib.auth.models import User
from core.models import  UserProfile
import json

def get_doctors(request):
    doctors = UserProfile.objects.filter(user_type=UserProfile.DOCTOR)
    email_list = [doctor.user.email for doctor in doctors]

    data = json.dumps({'doctor_contacts':email_list})
    return HttpResponse(data, mimetype='application/json')
