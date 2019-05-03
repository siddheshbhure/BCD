from django.shortcuts import render,redirect

import time


def custom_login_required(function):
	def wrap(request,*args,**kwargs):
		if request.session.has_key('username'):
			return function(request,*args,**kwargs)
		else:
			return redirect('logoutpage')
	wrap.__doc__=function.__doc__
	wrap.__doc__=function.__name__
	return wrap