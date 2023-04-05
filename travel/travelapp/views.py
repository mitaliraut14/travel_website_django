from django.shortcuts import render,redirect
from travelapp.models import Places,Book
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from travelapp.forms import UserReg
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.

def index(request):
    p=Places.objects.all()
    content={}
    content['data']=p
    return render(request,'index.html',content)

def signup(request):
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')

def about(request):
    return render(request,'about.html')

def userreg(request):
    if request.method=="POST":
        content={}
        fmdata=UserReg(request.POST)
        print(fmdata)
        print(fmdata.is_valid())
        content['regdata']=UserReg()
        if fmdata.is_valid():
            fmdata.save()
            content['msg']="User Created Sccessfully, Please Login"
        else:
            content['msg']="Fail to Create User!!!"
        return render(request,'userreg.html',content)
    else:
        # fm=UserCreationForm()
        fm=UserReg()
        print(fm)
        content={}
        content['regdata']=fm
        # return HttpResponse('Object displayed on terminal')
        return render(request,'userreg.html',content)
    
def userlogin(request):
    content={}
    content['logfmdata']=AuthenticationForm()
    if request.method=="POST":
        fmdata=AuthenticationForm(request=request,data=request.POST)
        # print(fmdata)
        if fmdata.is_valid():
            uname=fmdata.cleaned_data['username']
            upass=fmdata.cleaned_data['password']
            u=authenticate(username=uname,password=upass)
            # print(u)
            if u is not None:
                login(request,u)#login function stores userid in session
                return redirect('/')
            else:
                content['msg']="Invlaid Username or Password!!!"
    else:
        return render(request,'userlogin.html',content)
    
def placedetail(request,rid):
    p=Places.objects.filter(id=rid)
    content={}
    content['data']=p
    return render(request,'placedetail.html',content)


def book(request,rid):
    print(request.method)
    if request.method=="POST":
        pid=rid
        userid=request.user.id
        phn=request.POST['phn']
        tpass=request.POST['tp']
        # userid=request.session['user_id']
        
        p=Book.objects.create(pid=pid,uid=userid,phn_no=phn,passenger=tpass,book_date=datetime.datetime.now())
        print(p)
        p.save()
        return redirect('/udash')

    else:
        # print("In else part")    
        # print("Logged in User Id:" , request.session['user_id'])
        uid=User.objects.filter(id=request.user.id)
        pid=Places.objects.filter(id=rid)
        content={}
        content['data']=uid
        content['places']=pid
        return render(request,'book.html',content)

def userlogout(request):
    logout(request)
    return redirect('/userlogin')

def dashboard(request):
    # if request.session.get('user_id'):
    print(request.user.id)
    if request.user.id:
        # userid=request.session['user_id']
        userid=request.user.id
        p=Places.objects.filter(id=userid)
        a=Book.objects.filter(uid=userid)
        b=User.objects.filter(id=userid)
        # print(p)
        content={}
        content['data']=p
        content['book']=a
        content['user']=b
        return render(request,'dashboard.html',content)
    else:
        return render(request,'userlogin.html')
    
def delete(request,rid):
    p=Book.objects.get(id=rid)#select * from blogapp_post where id=rid
    p.delete()
    return redirect('/udash')


