from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

 

# Create your views here.
def home(request):
    return render(request , 'BogiBlog/home.html' , {'title': 'Home'}) 
    #What it does is, it uses a inbult django shortcut which render the file and import it to here from template

@login_required(login_url='bogiblog-login')
def contact(request):
    return render(request , 'BogiBlog/cv_temp.html' , {'title': 'Contact'})


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('bogiblog-home')
        else:
            messages.info(request, 'Username OR Password is incorrect.')
    return render(request , 'BogiBlog/login.html' , {'title': 'login'})

def logoutUser(request):
    logout(request)
    return redirect('bogiblog-login')