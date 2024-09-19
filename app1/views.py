from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Workspace
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# @login_required
def home(request):
    return render(request, 'home.html', {'user': request.user})


def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def service(request):
    return render(request,'service.html')


def library(request):
    return render(request,'library.html')

# Page Sign UP
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        
        if password != password2:
            return HttpResponse("Your Password and Confirmed Password are not alike!!")
        
        else:
            try:
                # Check if username already exists
                if User.objects.filter(username=uname).exists():
                    return HttpResponse("Username already exists. Please choose a different one.")
                
                # Create the user if username is unique
                my_user = User.objects.create_user(uname, email, password)
                my_user.save()
                return redirect('signin')
            
            except IntegrityError:
                return HttpResponse("An error occurred while creating the user.")
        

    return render(request,'signup.html')



# Page Sign IN
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'signin.html')




def LogoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='signup')
def ws(request):
    cd = {}
    if request.method == 'POST':
        form_data = request.POST
        if "name" in form_data:
            cd["name"] = form_data["name"]
        if "description" in form_data:
            cd["description"] = form_data["description"]
        if "member1" in form_data:
            cd["member1"] = form_data["member1"]
        if "member2" in form_data:
            cd["member2"] = form_data["member2"]
        if "member3" in form_data:
            cd["member3"] = form_data["member3"]
        if "member4" in form_data:
            cd["member4"] = form_data["member4"]

        # Ajoutez les données à la session
        request.session['ws_data'] = cd

    # Vérifiez s'il y a des données de formulaire dans la session
    if 'ws_data' in request.session:
        cd = request.session['ws_data']

    w = Workspace(
        name=cd.get("name", ""),  # Use .get() method to provide a default value if key is not found
        description=cd.get("description", ""),
        member1=cd.get("member1", ""),
        member2=cd.get("member2", ""),
        member3=cd.get("member3", ""),
        member4=cd.get("member4", "")
    )

    w.save()

    return render(request, 'ws.html', {"cd": cd})


@login_required(login_url='signup')
def ws2(request):
    cd = {}
    if request.method == 'POST':
        form_data = request.POST
        if "name2" in form_data:
            cd["name2"] = form_data["name2"]
        if "description2" in form_data:
            cd["description2"] = form_data["description2"]
        if "member12" in form_data:
            cd["member12"] = form_data["member12"]
        if "member22" in form_data:
            cd["member22"] = form_data["member22"]
        if "member32" in form_data:
            cd["member32"] = form_data["member32"]
        if "member42" in form_data:
            cd["member42"] = form_data["member42"]

        # Ajoutez les données à la session
        request.session['ws_data2'] = cd

    # Vérifiez s'il y a des données de formulaire dans la session
    if 'ws_data2' in request.session:
        cd = request.session['ws_data2']

    w = Workspace(
        name=cd.get("name2", ""),  # Use .get() method to provide a default value if key is not found
        description=cd.get("description2", ""),
        member1=cd.get("member12", ""),
        member2=cd.get("member22", ""),
        member3=cd.get("member32", ""),
        member4=cd.get("member42", "")
    )
    w.save()

    return render(request, 'ws2.html', {"cd": cd})


@login_required(login_url='signup')
def ws3(request):
    cd = {}
    if request.method == 'POST':
        form_data = request.POST
        if "name3" in form_data:
            cd["name3"] = form_data["name3"]
        if "description3" in form_data:
            cd["description3"] = form_data["description3"]
        if "member13" in form_data:
            cd["member13"] = form_data["member13"]
        if "member23" in form_data:
            cd["member23"] = form_data["member23"]
        if "member33" in form_data:
            cd["member33"] = form_data["member33"]
        if "member43" in form_data:
            cd["member43"] = form_data["member43"]

        # Ajoutez les données à la session
        request.session['ws_data3'] = cd

    # Vérifiez s'il y a des données de formulaire dans la session
    if 'ws_data3' in request.session:
        cd = request.session['ws_data3']

    w = Workspace(
        name=cd.get("name3", ""),  # Use .get() method to provide a default value if key is not found
        description=cd.get("description3", ""),
        member1=cd.get("member13", ""),
        member2=cd.get("member23", ""),
        member3=cd.get("member33", ""),
        member4=cd.get("member43", "")
    )
    w.save()

    return render(request, 'ws3.html', {"cd": cd})


@login_required(login_url='signup')
def createws(request):
    return render(request, 'createws.html')

@login_required(login_url='signup')
def createws2(request):
    return render(request, 'createws2.html')

@login_required(login_url='signup')
def createws3(request):
    return render(request, 'createws3.html')