from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from core.models import  UserProfile

import json

def validate_session_token(request):
    session_id = request.GET.get('session_id')

    some_data_to_dump = {
       'session_id': session_id,
        'is_valid': False,
        'is_doctor': False,
        'is_patient': False
    }

    try:
        session = Session.objects.get(session_key=session_id)

        session_data = session.get_decoded()

        uid = session_data.get('_auth_user_id')

        user = User.objects.get(id=uid)


        some_data_to_dump['is_admin'] = user.is_superuser

        some_data_to_dump['is_valid'] = True

        if not user.is_superuser:
            user_profile = UserProfile.objects.get(user=user)
            if user_profile.user_type == UserProfile.DOCTOR:
                some_data_to_dump['is_doctor'] = True
            elif user_profile.user_type == UserProfile.PATIENT:
                some_data_to_dump['is_patient'] = True



    except Exception,e:
        print e
        some_data_to_dump['is_valid'] = False

    data = json.dumps(some_data_to_dump)
    return HttpResponse(data, mimetype='application/json')