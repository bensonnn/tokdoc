from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^$', 'www.views.home_page', name='home_page'),
    url(r'^login/$', 'www.views.login_user', name='login_user'),
	 url(r'^signup/patient/$', 'www.views.signup_patient', name='signup_patient'),
	url(r'^signup/doctor/$', 'www.views.signup_doctor', name='signup_doctor'),
    url(r'^doctor/(?P<username>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$)', 'www.views.doctor_profile', name='doctor_profile'),

    url('^dan_home/', 'www.views.dan_home', name='dan_home'),
    url('^dan_dashboard/', 'www.views.dan_dashboard', name='dan_dashboard'),
)



"""
    url(r'^doctor/(?P<username>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$)', 'www.views.doctor_profile', name='doctor_profile'),

	url(r'^dashboard/$', 'www.views.dashboard', name='dashboard'),
    url(r'^profile/$', 'www.views.profile', name='profile'),
    url(r'admin_dashboard/$', 'www.views.admin_dashboard', name='admin_dashboard'),
"""