from django.shortcuts import redirect, render
from .forms import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def adminclick(request):
    return render(request, 'adminclick.html')

def studentclick(request):
    return render(request, 'studentclick.html')

def admin_registration(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'admin_registration.html', locals())

def student_registration(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'student_registration.html', locals())