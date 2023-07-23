from django.shortcuts import render, redirect
from .models import Prompts , Users, Payment, Delivery
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail
from django.conf import settings

import os
from dotenv import load_dotenv
# Create your views here.

#session = { 
# 'current': #represents from which page user redirected to login page so that after login he can redirected back there. values can be sell buy home
# 'user' : #stores email id of user who has logged in . null if not logged in
# }


def home_view(request):
    request.session.flush()
    request.session['current'] = 'home'
    prompts = Prompts.objects.all()
    context = {
        'prompts' : prompts,
    }

    request.session['user'] = 'null'
    if request.session.get('user')!= 'null':
        context['name'] = request.session.get('email')
    return render(request,'home.html',context)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Users.objects.filter(email=email).exists():
            user = Users.objects.get(email=email)
            if password == user.password :
                request.session['email'] = email
                request.session['user'] = 'logged'
                if request.session.get('current') == 'post':
                    return redirect(reverse('post_form_view'))
                elif request.session.get('current') == 'home':
                    return redirect(reverse('store_view'))
                elif request.session.get('current') == 'buy':
                    return redirect(reverse('prompt_view'))
                elif request.session.get('current') == 'browse':
                    return redirect(reverse('prompt_view'))
                    
            else :
                context = {
                    "error": "Invalid Password",
                }
                if request.session.get('user')!= 'null':
                    context['name'] = request.session.get('email')
                return render(request,'login.html',context)
            
        else :
            context = {
                "error": "Invalid User",
            }
            if request.session.get('user')!= 'null':
                context['name'] = request.session.get('email')
            return render(request,'login.html',context)
        
    if request.session.get('current')=='post':
        context ={
            'message' : 'to Post',
        }
    if request.session.get('current')=='home':
        context ={
            'message' : '',
        }

    if request.session.get('current')=='buy':
        context ={
            'message' : 'to Buy',
        }
    if request.session.get('current')=='browse':
        context ={
            'message' : 'to view the details of the Prompt',
        }
    if request.session.get('user')!= 'null':
        context['name'] = request.session.get('email')
    return render(request,'login.html',context)

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Users.objects.filter(email=email).exists() :
                context = {
                    'error' : 'User Already exists'
                }
                if request.session.get('user')!= 'null':
                    context['name'] = request.session.get('email')
                return render(request,'signup.html',context)
        
        else:
            user = Users()

            user.name = name 
            user.email = email
            user.password = password
            user.save()
            request.session['email'] = email
            request.session['user'] = 'logged'
            if request.session.get('current') == 'post':
                return redirect(reverse('post_form_view'))
            elif request.session.get('current') == 'home':
                return redirect(reverse('store_view'))
            elif request.session.get('current') == 'buy':
                return redirect(reverse('prompt_view'))
            elif request.session.get('current') == 'browse':
                return redirect(reverse('prompt_view'))

            return redirect(reverse('store_view'))
    context = {

    }
    if request.session.get('user')!= 'null':
        context['name'] = request.session.get('email')
    return render(request,'signup.html',context)

def store_view(request):

    if request.method == 'POST':

        title = request.POST.get('thetitle')
        request.session['thetitle'] = title
        return redirect(reverse('prompt_view'))

    prompts = Prompts.objects.all()

    context = {
        'prompts' : prompts
    }
    if request.session.get('user')!= 'null':
        context['name'] = request.session.get('email')
    return render(request,'store.html',context)

def payment_view(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        payment = Payment()
        prompt = request.session.get('thetitle')
        prompt = Prompts.objects.get(title=prompt)
        user = request.session.get('email')
        user = Users.objects.get(email=user)
        payment = Payment.objects.create(
            prompt = prompt,
            user = user,
            image = image,
        )

        payment.save()

        email = request.session.get('email')
        promptname = request.session.get('thetitle')
        send_mail(
            email,
            promptname,
            settings.EMAIL_HOST_USER,
            ['freelancerriyaz29@gmail.com'],
            fail_silently=False
        )

        
        user.pending.add(prompt)
        return redirect(reverse('prompt_view'))
    context = {
    
    }
    if request.session.get('user')!= 'null':
        context['name'] = request.session.get('email')
    return render(request,'payment.html',context)

def process_view(request):
    thetitle = request.session.get('thetitle')
    prompt = Prompts.objects.get(title=thetitle)
    context = {
        'prompt' : prompt,
    }
    if request.session.get('user')!= 'null':
        context['name'] = request.session.get('email')
    return render(request,'process.html',context)

def agreement_view(request):
    if request.method == 'POST':
        return redirect(reverse('payment_view'))
    context = {
    
    }
    if request.session.get('user')!= 'null':
        context['name'] = request.session.get('email')
    return render(request,'agreement.html',context)

def post_view(request):
    request.session['current'] = 'post'
    if request.method == "POST" and request.session.get('user')== 'null':
        return redirect(reverse('login_view'))
    elif request.method == "POST" and request.session.get('user') != 'null':
        return redirect(reverse('post_form_view'))
    else:
        context = {
    
        }
        if request.session.get('user')!= 'null':
            context['name'] = request.session.get('email')
        return render(request,'post.html',context)

def post_form_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        theprompt = request.POST.get('prompt')
        sample_input = request.POST.get('sample_input')
        sample_output = request.POST.get('sample_output')

        prompt = Prompts()

        prompt.title = title
        prompt.description = description
        prompt.prompt = theprompt
        prompt.sample_input = sample_input
        prompt.sample_output = sample_output

        prompt.save()
    context = {
    
    }
    if request.session.get('user')!= 'null':
        context['name'] = request.session.get('email')
    return render(request,'post_form.html',context)


def prompt_view(request):
    request.session['current'] = 'browse'
    if request.session.get('user')== 'null':
        return redirect(reverse('login_view'))
    elif request.session.get('user') != 'null':
        request.session['current'] = 'buy'
        user = request.session.get('email')
        thetitle = request.session.get('thetitle')

        theuser = Users.objects.get(email=user)
        flag = "False"
        for x in theuser.prompts.all():
            if thetitle == x.title:
                flag = "True"
                if flag:
                    break
        if flag =="True":
            return redirect(reverse('seeprompt_view'))
        for x in theuser.pending.all():
            if thetitle == x.title:
                flag = "Pending"
                if flag:
                    break
        
        
        if flag == "Pending":
            return redirect(reverse('process_view'))
        elif flag == "False":
            if request.method == "POST"  and request.session.get('user') != 'null':
                return redirect(reverse('agreement_view'))
            
            elif request.method == "POST" and request.session.get('user') == 'null':
                return redirect(reverse('login_view'))
            else:
                thetitle = request.session.get('thetitle')
                prompt = Prompts.objects.get(title=thetitle)
                context = {
                    'prompt' : prompt,
                }
                if request.session.get('user')!= 'null':
                    context['name'] = request.session.get('email')
                return render(request,'prompt.html',context)


        # send_mail(
        #     'One User Paid',
        #     'user',
        #     settings.EMAIL_HOST_USER,
        #     ['freelancerriyaz29@gmail.com'],
        #     fail_silently=False
        # )

def seeprompt_view(request):
    thetitle = request.session.get('thetitle')
    prompt = Prompts.objects.get(title=thetitle)
    context = {
        'prompt' : prompt,
    }
    if request.session.get('user')!= 'null':
        context['name'] = request.session.get('email')
    return render(request,'seeprompt.html',context)

def my_prompts_view(request):
    if request.method == 'POST':
        title = request.POST.get('thetitle')
        request.session['thetitle'] = title
        return redirect(reverse('prompt_view'))
    email = request.session.get('email') 
    user = Users.objects.get(email=email)
    context = {
        'user' : user,
    }
    if request.session.get('user')!= 'null':
        context['name'] = request.session.get('email')
    return render(request,'my_prompts.html',context)

def delivery_view(request):
    if request.method=="POST":
            p = Delivery.objects.get(id=1)
            if request.POST.get('p') == p.p:
                return redirect(reverse('delivery_form_view'))
    context = {
    
    }
    if request.session.get('user')!= 'null':
        context['name'] = request.session.get('email')
    return render(request,'delivery.html',context)

def delivery_form_view(request):
    
    payments = Payment.objects.all()
    context = {
        'payments' : payments
    }

    if request.method == "POST":
        user = request.POST.get('user')
        prompt = request.POST.get('prompt')

        theuser = Users.objects.get(email=user)
        theprompt = Prompts.objects.get(title=prompt)
        theuser.prompts.add(theprompt)

        payment = Payment.objects.get(user=theuser,prompt=theprompt)
        print(payment.user)
        payment.delivery = "Delivered"
        payment.save()
        print(payment.delivery)
        theuser.save()
    if request.session.get('user')!= 'null':
        context['name'] = request.session.get('email')

    payments = Payment.objects.all()
    context = {
        'payments' : payments
    }

    return render(request,'delivery_form.html',context)

