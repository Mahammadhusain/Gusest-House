from django.shortcuts import render,redirect,HttpResponse
from .form import userlogin,usercreate,UserEditForm,passchangeForm
from django.contrib.auth import authenticate,login as lo,logout as out,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
# user login
def login(request):
    form = userlogin()
    if request.method == "POST":
        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(username=uname,password=upass)
        if user is None:
            messages.error(request,"🔑 Please Enter Correct Credintial")
            return redirect('/login')
        else:
            lo(request,user)
            # ip = request.META.get('REMOTE_ADDR')
            # request.session['ip'] = ip
            # getip = request.session.get('ip',"No Address Found")
            messages.info(request,"👍 Login Successful")
            return redirect('/dashboard/')
    else:
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        else:
            return render(request,'login.html',{'form':form})
    return render(request,'login.html',{'form':form})


# user register
def register(request):
    form = usercreate() 
    if request.method == 'POST':
        form = usercreate(request.POST)
        if form.is_valid():
            form.save()
            form = usercreate() 
            messages.success(request,"New User Successful Registred")
            return redirect('/register')
    else:
        form = usercreate()
    return render(request, 'register.html', {'form': form})

# Show all user
def edituser(request,id):
    if request.method == 'POST':
        euser = User.objects.get(pk=id)
        form = UserEditForm(request.POST,instance = euser)
        if form.is_valid():
            form.save()
            uname = form.cleaned_data['username']
            messages.info(request,f'{uname} - User Successfully Updated')
            return redirect('/showuser/')
    else:
        euser = User.objects.get(pk=id)
        form = UserEditForm(instance = euser)
    context = {'form':form}
    return render(request,'edituser.html',context)



def showuser(request):
    alluser = User.objects.all()
    context = {'alluser':alluser}
    return render(request,'user.html',context)


# Logout
def logout(request):
    if request.user.is_authenticated:
        out(request)
        messages.info(request,'🙋‍ You are Successfully Logged Out !')
    return redirect('/login')


# Password Change
def reset(request):
    if request.user.is_authenticated:
        if request.method == 'POST': 
            form = passchangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                p =form.user
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,f'{p} - Your Password SuccessFully Changed')
                return redirect('/reset/')
            else:
                form = passchangeForm(user=request.user, data=request.POST)
                return render(request,'reset.html',{'form':form})
        else:
            form = passchangeForm(user=request.user)
        return render(request,'reset.html',{'form':form})
    else:
        messages.info(request, '☹︎ Please Login First')
        return redirect('/login/')
