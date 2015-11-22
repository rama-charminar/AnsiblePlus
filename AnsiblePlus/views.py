from django.http import HttpResponse
from django.template import Context, loader
from django.views.generic import View
from django.shortcuts import render
import sqlite3

def Login(request):	
	return render(request, 'login.htm')
def AppMaster(request):		
	return render(request, 'ApplicationMaster.html')
def EnvMaster(request):		
	return render(request, 'EnvironmentMaster.html')
def ServerMaster(request):		
	return render(request, 'ServerMaster.html')
def UserMaster(request):		
	return render(request, 'UserMaster.html')
def index(request):		
	return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')
def login(request):
	message = 'You submitted an empty form.'	
	if 'user' in request.POST:
		name=request.POST['user']
		pwd=request.POST['pwd']
		
		if name=='testuser' and pwd=='testpwd':
			request.session['access_key'] = name
			request.session.set_expiry(600)
			# return render(request, 'Hosts.htm')
			# return HttpResponse('Welcome :'+name)
			# get(request)			
	return home(request)
def SaveAppMaster(request):
	if 'AppName' in request.POST:
		AppName=request.POST['AppName']
		description=request.POST['AppDesc']
		
		sql = "INSERT INTO tblAppMaster (AppName,AppDesc) VALUES ('"+AppName+"','"+description+"' )"
			
		conn = sqlite3.connect('C:/Users/RAMKI/rama.db')
		
		conn.execute(sql);
		conn.commit();
		message = 'Application Name : '+AppName
	else:
		message = 'You submitted an empty form.'
	return home(request)
def SaveEnvMaster(request):
	if 'envName' in request.POST:
		envName=request.POST['envName']
		description=request.POST['envDesc']
		
		sql = "INSERT INTO tblEnvMaster (EnvName,EnvDesc) VALUES ('"+envName+"','"+description+"' )"
			
		conn = sqlite3.connect('C:/Users/RAMKI/rama.db')
		
		conn.execute(sql);
		conn.commit();
		message = 'Environment Name : '+envName
	else:
		message = 'You submitted an empty form.'
	return home(request)
def SaveUserMaster(request):
	if 'UserName' in request.POST:
		UserName=request.POST['UserName']
		UserEmail=request.POST['UserEmail']
		userEID=request.POST['userEID']
		
		sql = "INSERT INTO tblUserMaster (Name,Email,UserEID) VALUES ('"+UserName+"','"+UserEmail+"','"+userEID+"'  )"
			
		conn = sqlite3.connect('C:/Users/RAMKI/rama.db')
		
		conn.execute(sql);
		conn.commit();
		message = 'User Name : '+UserName
	else:
		message = 'You submitted an empty form.'
	return home(request)
def SaveServerMaster(request):
	if 'serverip' in request.POST:
		serverip=request.POST['serverip']
		serverhost=request.POST['serverhost']
		serveruser=request.POST['serveruser']
		serverpwd=request.POST['serverpwd']
		
		sql = "INSERT INTO tblServerMaster (ServerIP,ServerHost,ServerUserName,ServerCredential) VALUES ('"+serverip+"','"+serverhost+"','"+serveruser+"','"+serverpwd+"')"
			
		conn = sqlite3.connect('C:/Users/RAMKI/rama.db')
		
		conn.execute(sql);
		conn.commit();
		message = 'Server IP: '+serverip
	else:
		message = 'You submitted an empty form.'
	return home(request)

			
