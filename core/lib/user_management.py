from django.contrib.auth.models import User
from core.models import DoctorProfile, PatientProfile, UserProfile
from django.db import IntegrityError
from django.db import transaction

@transaction.atomic
def create_doctor(email, password):
    try:
        sid = transaction.savepoint()
        user = User.objects.create_user(username=email, email=email, password=password)
        doctor_profile = DoctorProfile(user=user, user_type=UserProfile.DOCTOR)
        doctor_profile.save()
        transaction.savepoint_commit(sid)
        return user
    except (IntegrityError) as e:
        transaction.savepoint_rollback(sid)

@transaction.atomic
def create_patient(email, password):
    try:
        sid = transaction.savepoint()
        user = User.objects.create_user(username=email, email=email, password=password)
        patient_profile = PatientProfile(user=user, user_type=UserProfile.PATIENT)
        patient_profile.save()
        transaction.savepoint_commit(sid)
        return user
    except (IntegrityError) as e:
        transaction.savepoint_rollback(sid)



