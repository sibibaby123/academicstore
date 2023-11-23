from django.contrib import auth , messages
from django.contrib.auth import authenticate , login
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Department,Purpose, UserExtra, Course
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
import uuid, json
import re
# Create your views here.

def register(request):
    if request.method == "GET":
        return  render(request, "registration.html")
    elif request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('cpassword')
        user = User.objects.filter(username = username)
        if(len(user)!=0):
            error = "Username already exist!"
            return render(request ,"registration.html",{"error" : error})
        user = User.objects.filter(email = email)
        if (len(user)!= 0):
            error = "Email already exist!"
            return render(request ,"registration.html",{"error" : error})
        if password == c_password:
            user = User(first_name=first_name,last_name=last_name,username=username,email=email)
            user.set_password(password)

            if re.match( r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])[\w\d@#$%^&+=]{8,}$' , password):
                print("Valid password")
            else :
                print("Password not valid")
                return render(request,"registration.html",{'error':"password not valid"})
            user.save()
            print("user created successfully")
            return redirect('/')
        else:
            error = "Not matching"
            return render(request, "registration.html", {"error": error})

def login_page(request):
    if request.method == 'GET':
        context={}
        return render(request,'login.html',context)
    else:
        if request.method == 'POST':
           username=request.POST['username']
           password=request.POST['password']
           myuser=authenticate(request,username=username,password=password)
           if myuser is not None:
              login(request,myuser)
              return redirect("studentform/")
           else:
                context= {
                    'error':"invalid username or password"
                         }
                return render(request,"login.html",context)
def studentform(request):
    if request.method == 'GET':
        context ={}
        return render(request,'studentform.html',context)
def logout(request):
    auth.logout(request)
    return redirect('/')
def dataform(request):
    if request.method == "GET":
        context ={'department':Department.objects.all()}
        return render( request , "dataform.html", context)
    elif request.method == "POST":
        date=request.POST.get('date')
        age=request.POST.get('age')
        gender = request.POST.get('inlineRadioOptions')
        number = request.POST.get('number')
        addr = request.POST.get('address')
        course=request.POST.get('course') 
        purpose=request.POST.get('purpose')
        exampaper=request.POST.get('exampaper')
        pen=request.POST.get('pen')
        studymaterial=request.POST.get('studymaterial')
        books=request.POST.get('books')
        newspaper=request.POST.get('newspaper')
        userextra = UserExtra(
                user = request.user,
                age = age,
                dateofbirth = date,
                gender = gender,
                phonenumber = number,
                address = addr,
                course_id=course,
                purpose=purpose,
                exampaper=exampaper,
                pen=pen,
                material=studymaterial,
                books=books,
                newspaper=newspaper
                )
        userextra.save()
        return render(request,"success.html",{'userextra':userextra})

def allCourse(request):
    links=Department.objects.all()
    return render(request,"home.html",{'links':links})


def department(request,slug):
    department=Department.objects.get(slug=slug)
    print(department)
    return render(request,"department.html",{'department':department})


def get_course_by_id(request):
    if request.method == "GET":
        department_id = request.GET.get("dept_id")
        data = Course.objects.filter(department_id=department_id).values()
        return JsonResponse(json.dumps(list(data)), safe=False)
    





