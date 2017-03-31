from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Photograph
from .forms import PhotographForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    photographs = Photograph.objects.all()
    form = PhotographForm()
    return render(request, 'index.html', { 'photographs': photographs, 'form': form })

def detail(request, photograph_id):
    photograph = Photograph.objects.get(id=photograph_id)
    return render(request, 'detail.html', { 'photograph': photograph })

def post_photograph(request):
    #request.FILES is needed to access uploaded files
    form = PhotographForm(request.POST, request.FILES) 
    if form.is_valid():
        photograph = form.save(commit = False)
        photograph.user = request.user
        photograph.save()


    return HttpResponseRedirect('/')
                  
def profile(request, username):
    user = User.objects.get(username = username)
    photographs = Photograph.objects.filter(user = user)
    return render(request, 'profile.html', 
                  {'photographs': photographs, 
                   'username': username })

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled")
                    #Code to render disabled user error HTML 
            else:
                print("Incorrect username or password")
                # Code to render incorrect entry error HTML


    else:
        form = LoginForm()
        return render(request, 'login.html', 
                      {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

# ? GET.get ?? 
def like_photograph(request):
    photograph_id = request.GET.get('photograph_id', None) 

    likes = 0
    if (photograph_id):
        photograph = Photograph.objects.get(id=int(photograph_id))
        if photograph is not None:
            likes = photograph.likes + 1
            photograph.likes = likes
            photograph.save()

    return HttpResponse(likes)
