from django.shortcuts import render,redirect
from .forms import UserLogin
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate


# Create your views here.

class Login(View):
    def get(self,request):
        context = {
            'form' : UserLogin()
        }
        return render(request,'accounts/login.html',context)
    def post(self,request):
        username = request.POST.get('username') 
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('notes')
    
        return redirect('login')
    
def user_logout(request):
    logout(request)
    return redirect('login')