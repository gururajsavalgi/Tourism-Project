
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login
from django.http import JsonResponse
import random
from django.db.models import Case, When
#from .models import User
from .models import Index, Contact,Guide_detail,Customer_detail
from itertools import chain

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.user.is_authenticated:
        username = request.user.username
    Indexs=Index.objects.all()
    n=len(Indexs)
    params={ 'Index':Indexs,'username': username}
    return render(request, 'index.html', params)

def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method=="POST":
        name=request.POST.get('name','')
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
    about = Index.objects.filter(msg_id=myid)


    return render(request, 'about.html', {'about':about[0]})

def services(request, myid):
    if request.user.is_anonymous:
        return redirect("/login")
    service = Index.objects.filter(msg_id=myid)
    return render(request,"services.html", {'service':service[0]})

def loginUser(request):
    if request.method=="GET":
      return render(request,"login.html")

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username, password=password)

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
            user = request.user
            name=request.POST.get('name','')
            phone=request.POST.get('num','')
            msg_id=request.POST.get('msg_id','')

            customer = Customer_detail(name=name, phone=phone,Customer_id=msg_id,user=user)
            customer.save()
            return redirect('guide')
        customer = Customer_detail.objects.filter(user=request.user)
        ids = []
        for i in customer:
            ids.append(i.Customer_id)
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
        index = Index.objects.filter(msg_id__in=ids).order_by(preserved)

        return render(request, 'VisitedPlace.html', {'customer': index,'customern':customer})
def search(request):
    query=request.GET['query']
    if len(query)>80 and len(query)==0:
        allpost=Index.objects.none()
    else:
        placename=Index.objects.filter(placename__icontains=query)
        category=Index.objects.filter(category__icontains=query)
        subcategory=Index.objects.filter(subcategory__icontains=query)
        allpost=list(chain(placename, category,subcategory))
    if len(allpost)==0:
        messages.warning(request,"No search result found.")

    return render(request, 'SEARCH.html',{'allPosts':allpost})


    