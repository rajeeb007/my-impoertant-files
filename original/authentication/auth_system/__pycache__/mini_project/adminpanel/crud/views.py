
from django.shortcuts import render,redirect
from django.contrib import messages
from authentication.forms import UserSignup

from authentication.views import home
from .models import UserProfile
from .forms import StudentRegistration
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache




# Create your views here.
@never_cache
@user_passes_test(lambda u: u.is_superuser,login_url=home)
@login_required(login_url='signin')
def add_show(request):

    stud = User.objects.all()
    # newuser=UserProfile.objects.all()
    context={
        'stu':stud,
        # 'newuser':newuser
    }
    return render(request, 'crud/addandshow.html', context)
    
@never_cache
@user_passes_test(lambda u: u.is_superuser,login_url=home)
@login_required(login_url='signin')
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        pi.delete()
        messages.info(request, 'Deleted Succefully')
    return redirect('addandshow')
@never_cache
@user_passes_test(lambda u: u.is_superuser,login_url=home)
@login_required(login_url='signin')
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        
        fm = StudentRegistration(request.POST, instance=pi)
        
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Edited Succefully')
        
    else:
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(instance=pi)
        
    return render(request, 'crud/updatestudent.html', {'form' : fm})

@never_cache
@user_passes_test(lambda u: u.is_superuser,login_url=home)
@login_required(login_url='signin')
def search_username(request):
    searched = request.GET['search']
    searchnames = User.objects.filter(username__contains = searched)
    return render(request, 'crud/addandshow.html', {'stu' : searchnames})
@never_cache
@user_passes_test(lambda u: u.is_superuser,login_url=home)
def adminadd(request):
    if request.user.is_authenticated:
     if request.method == 'POST':
        fmsp = UserSignup(request.POST)
        if fmsp.is_valid():
            urnm = fmsp.cleaned_data['username']
            ftnm = fmsp.cleaned_data['first_name']
            ltnm = fmsp.cleaned_data['last_name']
            pw = fmsp.cleaned_data['password']
            pw2 = fmsp.cleaned_data['Confirm_password']
            if pw == pw2:
                if User.objects.filter(username=urnm).exists():
                    messages.info(request, 'Username already exists')
                    return redirect('adminadd')
                else:
                    registration = User.objects.create_user(
                        username=urnm, first_name=ftnm, last_name=ltnm, password=pw)
                    registration.save()
                    messages.info(request, 'Succefully Added your User')
                    return redirect('addandshow')
            else:
                messages.info(request, 'Password not match')
                return redirect('adminadd')
     else:
        fmsp = UserSignup()
    return render(request, 'crud/adminadd.html', {'form': fmsp})

    