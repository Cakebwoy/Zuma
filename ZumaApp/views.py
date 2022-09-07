from django.shortcuts import render 
from django.shortcuts import  redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from .models import Signin
from .forms import NameForm


# Create your views here.



# def signin(request):



#     template ="main/signin.html"
#     return render ( request,template)

def signin(request):
    
    if request.method == "POST":
        data = NameForm(request.POST)
        username = data["username"]
        password = data.get("password")

        user_exist = Signin.objects.filter(username=username)
        if len(user_exist) > 0:
            return render(request,"main/signin.html",{"error": "user already exist"} )
        else: 
            new_user = Signin(username = username, password = password)
            new_user.save()
            return render(request, "main/signin.html", {"msg":f'{username}succesfully signed up'})
        return render(request,"main/signi .html",{"name": username})
    return render(request,"main/signin.html")
            


    
    # template ="main/signin.html"

    # return render ( request,template)
    


def index(request):
    template ="main/index.html"

    return render ( request, template)

def buysel(request):
    template ="main/buysel.html"

    return render ( request, template)


