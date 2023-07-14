from django.shortcuts import render, redirect
from .models import Prompts , Users
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home_view(request):
    return render(request,'home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Users.objects.filter(email=email).exists():
            user = Users.objects.get(email=email)
            if password == user.password :
                request.session['email'] = email
                return redirect(reverse('store_view'))
            else :
                context = {
                    "error": "Invalid Password",
                }
                return render(request,'login.html',context)
            
        else :
            context = {
                "error": "Invalid User",
            }
            return render(request,'login.html',context)
    return render(request,'login.html')

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Users.objects.filter(email=email).exists() :
                context = {
                    'error' : 'User Already exists'
                }
                return render(request,'signup.html',context)
        
        else:
            user = Users()

            user.name = name 
            user.email = email
            user.password = password

            user.save()

            return redirect(reverse('store_view'))
    return render(request,'signup.html')

def store_view(request):

    if request.method == 'POST':

        title = request.POST.get('thetitle')
        request.session['thetitle'] = title
        return redirect(reverse('prompt_view'))

    prompts = Prompts.objects.all()

    context = {
        'prompts' : prompts
    }
    return render(request,'store.html',context)

def payment_view(request):

    title = request.session.get('thetitle')

    prompt = Prompts.objects.get(title=title)
    print(prompt)
    context = {
        "prompt" : prompt
    }
    return render(request,'payment.html',context)

def post_view(request):
    return render(request,'post.html')

def prompt_view(request):

    thetitle = request.session.get('thetitle')
    prompt = Prompts.objects.get(title=thetitle)
    context = {
        'prompt' : prompt,
    }
    return render(request,'prompt.html',context)