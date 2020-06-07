from django.shortcuts import render
from .forms import addrForm

# Create your views here.

def home(request):
    # all_jss = jss.objects.all()
    return render(request, 'home.html')

def addr(request):
    if request.method == "GET":
        neighborAddr = addrForm(request.GET, request.FILES)
        
        if neighborAddr.is_valid():
            neighborAddr.save()
            return redirect('home')
            