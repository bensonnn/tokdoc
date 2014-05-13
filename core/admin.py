from django.contrib import admin
from core.models import UserConnection, DoctorProfile, PatientProfile, UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username',)
    def username(self, obj):
        return '%s' % obj.user.username

admin.site.register(DoctorProfile, ProfileAdmin)
admin.site.register(PatientProfile, ProfileAdmin)
admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(UserConnection)