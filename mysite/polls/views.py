from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request, name=''):
	if (name == ''):
		name = 'World'
	template = loader.get_template('polls/index.html')
	message = ('Hello %s!' % name)
	context = {
		'message': message
	}
	return HttpResponse(template.render(context, request))

