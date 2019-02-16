from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# def home(request):
# 	return HttpResponse('Hello World! HomePage!')

def home(request):
	context = {
			'title' : 'HomePage',
			'name' : 'Rahul'
		}
	return render(request, 'home.html', context)

def contact(request):
	return HttpResponse('Contact Pages')


