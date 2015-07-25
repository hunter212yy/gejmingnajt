from django.shortcuts import render

def home( request ):
	return render( request, "landing/home.html", {})

def login( request ):
	return render( request, "landing/login.html", {})

def register( request ):
	return render( request, "landing/register.html", {})