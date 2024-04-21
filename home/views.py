
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate,login
from django.http import JsonResponse
import random

#from .models import User
from .models import Index, Contact,Guide_detail,Customer_detail
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    Indexs=Index.objects.all()
    n=len(Indexs)
    params={ 'Index':Indexs}
    return render(request, 'index.html', params)

def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method=="POST":
        print(request)
        name=request.POST.get('name','')
        print(name)
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,"contact.html")

def about(request, myid):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    about = Index.objects.filter(id=myid)
    print(about)


    return render(request, 'about.html', {'about':about[0]})

def services(request, myid):
    if request.user.is_anonymous:
        return redirect("/login")
    service = Index.objects.filter(id=myid)
    print(service)
    return render(request,"services.html", {'service':service[0]})

def loginUser(request):
    if request.method=="GET":
      return render(request,"login.html")

    if request.method=="POST":
        print("Hiiiiiiiiiiiii")
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username)
        print("Hiiiiiiiiiiiii")
        print(password)
        user = authenticate(username=username, password=password)
        print(username, password)

        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            messages.success(request, "You have logged in successfully!")
            return redirect('index')
        else:
            return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")
def sign(request):
    if request.method=="GET":
      return render(request,"sign_in.html")
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        print("hiiiiiiiiii")
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            return HttpResponse("incorrect password")
        else:
            my_user=User.objects.create_user(username,email,password1)
            my_user.save()
            return redirect('login')
def guide(request):
        guide = list(Guide_detail.objects.all())

        if not guide:
            return JsonResponse({'error': 'No delivery boys available'})

        # Select a random delivery boy
        else:
            guide = random.choice(guide)
        return render(request, 'HISTORY.html',{'guide':guide})
def customer(request):
        if request.method=="POST":
            name=request.POST.get('name','')
            print(name)
            phone=request.POST.get('num','')
            placename=request.POST.get('placename','')

            customer = Customer_detail(name=name, phone=phone,placename=placename)
            customer.save()
        return redirect('guide')