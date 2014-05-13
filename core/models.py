from django.db import models
from django.contrib.auth.models import User

class WaitingRoom(models.Model):
    manager = models.ForeignKey(User, unique=True)



class DoctorOnlineCall(models.Model):
    doctor = models.ForeignKey(User, related_name='doctor')
    patient = models.ForeignKey(User, related_name='patient')
    duration = models.IntegerField()
    start_time = models.DateTimeField()


class UserProfile(models.Model):
    DOCTOR = 'DR'
    PATIENT = 'PT'

    USER_TYPE = (
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient'),
    )
    user = models.ForeignKey(User)
    #profile_pic = models.ImageField(upload_to = 'profile_pic/',default = 'img/default_profile.png')
    user_type = models.CharField(max_length=2,
                                      choices=USER_TYPE,
                                      default=PATIENT)



class DoctorProfile(UserProfile):
   class Meta:
        permissions = (("can_have_public_profile","User can have a public profile"),
                       ("can_have_waiting_room", "User can host a waiting room"),
                       ("can_accept_payment", "User can accept payment"),
                      )

class PatientProfile(UserProfile):
   class Meta:
        permissions = (("can_make_payment","User can make a payment"),
                       ("can_join_waiting_room", "User can join a waiting room")
                      )



class UserConnection(models.Model):
    user_a = models.ForeignKey(User, related_name='user_a')
    user_b = models.ForeignKey(User, related_name='user_b')
    user_a_requested_date = models.DateTimeField()
    user_b_accepted_date = models.DateTimeField(blank=True, null=True)
    invite_sent = models.BooleanField()

    class Meta:
        unique_together = (("user_a","user_b"),)



