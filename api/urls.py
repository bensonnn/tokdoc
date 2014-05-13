from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'validate_session_token/', 'api.auth.validate_session_token', name='validate_session_token'),
    url(r'get_doctors/', 'api.doctor.get_doctors', name='get_doctors'),
)
