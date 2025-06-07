from django.contrib.auth.models import *
from urllib import request
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from home.models import Transcation
from django.http import JsonResponse
import json
from home.views import *
from datetime import date, datetime


def export_data_as_json(request):
    data = list(Transcation.objects.values())
    print(json.dumps(data))
    a = json.dumps(data)

    return JsonResponse(data, safe=False)


def export_data_as_json_by_id(request, id):
    data = Transcation.objects.values(
        "id", "date_t", "amount_t", "category_t", "description_t"
    ).get(id=id)
    print(json.dumps(data))
    return JsonResponse(data, safe=False)





# def load_json_data(request):
#     json_file_path = 'D:/django_code/core/csvjson.json'
#     with open(json_file_path,'r') as file:
#         data = json.load(file)
#     return JsonResponse(file, safe=False)


def export_data_as_text(request):
    data = list(Transcation.objects.values())
    with open("data.json", "w") as file:
        json.dump(data, file, default=str)
        
    return JsonResponse({"message": "ok"})


def register(request):

    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            messages.info(request, "check password")
            print("password is not matching")
            return redirect("/register/")

        elif User.objects.filter(username=username).exists():
            messages.info(request, "email taken")
            return redirect("/register/")
        else:
            User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=make_password(password),
            )
        return redirect("/login/")

    queryset = User.objects.all()
    context = {"User": queryset}

    return render(request, "register.html", context)


@login_required(login_url="/login/")
def dashboard(request):
    queryset = Transcation.objects.all()
    context = {"Transcation": queryset}

    return render(request, "dashboard.html", context)


def add_transcation(request):
    if request.method == "POST":
        form = request.POST
        date_t = form.get("date_t")
        amount_t = form.get("amount_t")
        category_t = form.get("category_t")
        description_t = form.get("description_t")

        Transcation.objects.create(
            date_t=date_t,
            amount_t=amount_t,
            category_t=category_t,
            description_t=description_t,
        )
        
    
        export_data_as_text(request)
        return redirect("/add_transcation/")

    return render(request, "add_transcation.html")


import json
from django.shortcuts import render
from .models import Transcation  # Make sure this import exists

def view_transcation(request):
    json_file_path = "D:/django_code/core/data.json"
    
    try:
        with open(json_file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    
    search = []  # Initialize search results
    
    if request.method == "POST":
        form = request.POST
        start = form.get("start")
        end = form.get("end")
    
        
        
    return render(request, "view_transcation.html", {
        "data": data,
    })


def login_p(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return redirect("/login/")
        # if not User.objects.filter(password=password).exists():
        #     messages.error(request, "Invalid password")
        #     return redirect("/login/")
        if user is not None:
            login(request, user)
            return redirect("/dashboard/")
            # messages.error(request, "Invalid Password")
            # return redirect("/login/")

        else:
            messages.error(request, "something wrong")
            return redirect("/login/")
            # login(request, user)
            # return redirect("/dashboard/")

    queryset = User.objects.all()
    context = {"User": queryset}
    return render(request, "login.html", context)


def logout(request):
    return render(request, "logout.html")


def home(request):
    return render(request, "home.html")


def forgetPassword(request):
    return render(request, "forgetPassword.html")


def table(request):
    return render(request, "table.html")
