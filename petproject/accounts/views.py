from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .forms import LocationForm, ProfileCreationForm, PlusPhotoForm
from .models import UserLocation, RegiProfile, PlusPhoto
from django.contrib.auth import login as pet_login
from django.contrib.auth.models import User
# Create your views here.


def startpage(request):
    return render(request, 'registration/startpage.html')

def register(request):
    if request.method == "POST":
        register_form = UserCreationForm(request.POST)
        # request.POST안에 담긴 정보들을 UserCreateForm에 담고,
        com_location_form = LocationForm(request.POST['ispermit'])

        if register_form.is_valid():
            register_form.save()
            user = User.objects.get(username = register_form.cleaned_data['username'])

            pet_login(request, user)
            return redirect('regi_profile')
        else:
           return redirect('register')     #redirect: 다시 회원가입 요청
    register_form = UserCreationForm()      #유저생성폼을 만든다
    location_form = LocationForm()
    return render(request, 'registration/register.html', {'register_form':register_form},{'location_form':location_form})


def regi_profile(request):
    my_pet = RegiProfile.objects.get(user=request.user)
    if request.method == "POST":
        regi_profile_form = ProfileCreationForm(request.POST, instance=my_pet)
        if regi_profile_form.is_valid:
            regi_profile_form.save()
            return redirect('myprofile')        #myprofile로 가게 해주세요
        else:
           return redirect('regi_profile')  
    regi_profile_form = ProfileCreationForm(instance=my_pet)

    return render(request, 'registration/regi_profile.html', {'regi_profile_form':regi_profile_form})

def login(request):
    return render(request, 'registration/login.html')

def myprofile(request):
    all_pet = RegiProfile.objects.all()
    myprofile = RegiProfile.objects.get(user=request.user)
    return render(request, 'registration/myprofile.html', {'myprofile':myprofile}, {'all_pet':all_pet})

#myform.post =jss_id    #댓글이 달릴 글의 ID는 넘어오는 jss_id로 해주자.

def photoplus(request):
    photo_plus = RegiProfile.objects.get(user=request.user)
    if request.method == "POST":
        plusphoto_form = PlusPhotoForm(request.POST['plus_image'], instance= photo_plus)
        if plusphoto_form.is_valid:
            plusphoto_form.save()
            return redirect('myprofile') 
        else:
           return redirect('photoplus')  
    plusphoto_form = PlusPhotoForm(instance=photo_plus)

    return render(request, 'registration/photoplus.html', {'photo_plus':photo_plus}, {'plusphoto_form':plusphoto_form})



def profileinform(request):
    all_pet = RegiProfile.objects.all()
    myprofile = RegiProfile.objects.get(user=request.user)

    return render(request, 'registration/profileinform.html',{'myprofile':myprofile}, {'all_pet':all_pet})