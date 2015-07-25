from django.conf.urls import include, url
from views import home, login, register

urlpatterns = [
	url(r'^$', home, name="landing-url"), 
	url(r'^logowanie/$', login, name="login-url"),
	url(r'^rejestracja/$', register, name="registration-url"),

]
