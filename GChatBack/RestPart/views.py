from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

def login(request):
	if 'login' in request.POST and 'password' in request.POST and request.POST['login']!='' and request.POST['password']!='':
		login = request.POST['login']
		password = request.POST['password']
		user = auth.authenticate(username = login,password =password)
		if user is not None and user.is_active:
			auth.login(request, user)
			getID = User.objects.get(username = login)
			return JsonResponse({'id_client':getID.id,'error':'0'})
		else:
			return JsonResponse({'error':'1','error_message':'no user'})
	else:
		return JsonResponse({'error':'2','error_message':'incorect request'})

def registration(request):
	if 'login' in request.POST and 'password' in request.POST and 'email' in request.POST and request.POST['login']!='' and request.POST['password']!='' and request.POST['email']!='':
		login = request.POST['login']
		password = request.POST['password']
		email = request.POST['email']
		if User.objects.get(username = login):
			return JsonResponse({'error':'3','error_message':'login take'})
		else:
			user =User.objects.create_user(username=login, password = password, email =email)
			user.is_active = True
			user.save()
			getID = User.objects.get(username = login)
			return JsonResponse({'id_client':getID.id,'error':'0'})
	else:
		return JsonResponse({'error':'2','error_message':'incorect request'})

def getProfile(request):
	if 'id_client' in request.POST and request.POST['id_client']!='':
		idClient = request.POST['id_client']
		if User.objects.get(id = idClient):
			user = User.objects.get(id = idClient)
			return JsonResponse({'first_name':user.first_name,'last_name':user.last_name,'email':user.email,'login':user.username})
		else:
			return JsonResponse({'error':'1','error_message':'no user'})
	else:
		return JsonResponse({'error':'2','error_message':'incorect request'})

"""def setProfile(request):
	if 'id_client' in request.POST and request.POST['id_client']!='':
		idClient = request.POST['id_client']
		if 'first_name' in request.POST and request.POST['']:
			pass"""
# Create your views here.
