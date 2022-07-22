from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def adminclick(request):
    return render(request, 'adminclick.html')

def studentclick(request):
    return render(request, 'studentclick.html')


def admin_signup(request):
    if request.method == 'POST':
        form = SignupFormAdmin(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_login')
    else:
        form = SignupFormAdmin()
    return render(request, 'admin_signup.html', {'form':form}, locals())


def student_signup(request):
    if request.method == 'POST':
        form = SignupFormStudent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_login')
    else:
        form = SignupFormStudent()
    return render(request, 'student_signup.html', {'form':form}, locals())

def admin_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user and user.is_admin:
                    login(request,user)
                    # messages.success(request,'Logged in successfully!!!')
                    return redirect('/admin_profile/')
                # elif user and user.is_student:
                #     login(request,user)
                #     # messages.success(request,'Logged in successfully!!!')
                #     return redirect('/user_student/')
                else:
                    # messages.success(request,'Invalid Credentials!')
                    return redirect('/')
        else:
            fm = LoginForm()
        return render(request,'admin_login.html',{'form':fm})
    else:
        return redirect('/')


def student_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user and user.is_student:
                    login(request,user)
                    # messages.success(request,'Logged in successfully!!!')
                    return redirect('/student_profile/')
                # elif user and user.is_student:
                #     login(request,user)
                #     # messages.success(request,'Logged in successfully!!!')
                #     return redirect('/user_student/')
                else:
                    # messages.success(request,'Invalid Credentials!')
                    return redirect('/')
        else:
            fm = LoginForm()
        return render(request,'student_login.html',{'form':fm})
    else:
        return redirect('/')


def admin_profile(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    else:
        return render(request, 'admin_profile.html')


def student_profile(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    else:
        return render(request, 'student_profile.html')

def user_logout(request):
    logout(request)
    return redirect('/')


def about_us(request):
    return render(request, 'about_us.html')


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = ContactUs(name=name, email=email, subject=subject, message=message)
        contact.save()

    return render(request, 'contact_us.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = request.user
    adm = AdminProfile.objects.get(user=user)
    # if request.method == "POST":
    #     form = AdminProfileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         obj = form.save(commit=False)
    #         obj.user = request.user
    #         obj.save()
    #         return redirect('profile')

    # else:
    #     form = AdminProfileForm()
    
    return render(request, 'profile.html', locals())

# def edit_profile(request):
#     edit_pro = AdminProfile.objects.all 
#     return render(request, 'profile.html', locals())


def add_book(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_profile')
        else:
            return redirect('add_book')
    else:
        form = AddBookForm()
    return render(request, 'add_book.html', locals())

def view_book(request):
    books = AddBook.objects.all()
    return render(request, 'view_book.html', locals())
            