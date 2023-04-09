from django.http.response import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout

from django.contrib import messages

from .models import User
from .forms import CustomUserCreationForm,UserForm
from django.db.models import Q
# Create your views here.


"""login"""
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']

            user = User.objects.get(email=email)

            if user:
                user = authenticate(email=email,password=password)
            else:
                messages.info(request," Username or Password is incorrect ")

            if user is not None:
                login(request,user)
                messages.info(request,"logged in succesfully")
                return redirect('home')
        except:
            return render(request,'core/login.html')

    return render(request,'core/login.html')


"""logout"""
@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.info(request,"User logged out successfully")
    return redirect('login')

    #return render(request,'users/login.html')

"""register user"""
def registerUser(request):
    if request.user.is_authenticated:
        return redirect('login')
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            messages.success(request,"User account created successfully")
            return redirect('login')

    context = {'form':form}
    return render(request,'core/register.html',context)

"""home"""
def home(request):
    users = User.objects.all()

    context={'users':users}
    return render(request,'core/user.html',context)

"""update user"""
@login_required(login_url='login')
def updateUser(request,pk):
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)

    if request.method == 'POST':
        print(request.POST,">>>>>>>>>>>>>>>>>>>>>")
        form = UserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            user = form.save()
            if request.user == user:
                login(request,user)
            messages.info(request,"User information updated succesfully")
            return redirect('home')

    context = {'form':form}
    return render(request,'core/user_form.html',context)


@login_required(login_url='login')
def deleteUser(request,pk):
    user = User.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        messages.info(request,"user deleted succesfully")
        return redirect('home')

    context = {'user':user}
    return render(request,'core/delete_user.html',context)


"""search user"""
@login_required(login_url='login')
def search_user(request):
    if request.method == "POST":
        search_item = request.POST['search_item']
        users = User.objects.filter(
            Q(name__icontains=search_item) |
            Q(email__icontains=search_item)
        )

        context={'users':users}
        return render(request,'core/user.html',context)

    return redirect('home')


"""staff user"""
@login_required(login_url='login')
def staff_user(request):
    try:
        users = User.objects.filter(is_staff = True)

        context={'users':users}
        return render(request,'core/user.html',context)
    except:
        return redirect('home')

"""active user"""
@login_required(login_url='login')
def active_user(request):
    try:
        users = User.objects.filter(is_active = True)

        context={'users':users}
        return render(request,'core/user.html',context)
    except:
        return redirect('home')


"""super user"""
@login_required(login_url='login')
def super_user(request):
    try:
        users = User.objects.filter(is_superuser=True)

        context={'users':users}
        return render(request,'core/user.html',context)
    except:
        return redirect('home')