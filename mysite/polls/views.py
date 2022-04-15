from django.shortcuts import render
from django.http import HttpResponse

def index(request, name=''):
	if (name == ''):
		name = 'World'
	return HttpResponse('Hello %s!' % name)

