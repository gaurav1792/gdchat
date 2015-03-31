from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from chat.forms import Login, SignUp, MessageForm
from chat.models import Message
from chat.models import Login_status
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
import datetime
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import json
import uuid
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .functions import *
from django.db.models import Max
from datetime import datetime
from django.utils.timezone import now as utcnow
from django.utils.safestring import mark_safe
from .forms import MessageForm, ImageForm

import json
from django.utils.safestring import mark_safe
# Create your views here.


def static_var(varname, value):
   def decorate(func):
     setattr(func, varname, value)
     return func
   return decorate

@static_var('counter',0)
def setcounter(request,u_id=0):
    test12.counter =0
    test11.counter =0
    return HttpResponse(test11.counter)

def index(request, auth_form=None, user_form=None):
    # User is logged in
    if request.user.is_authenticated():
        user = User.objects.all()
        status = Login_status.objects.all()
        return render(request, 'index.html', {'cur_user': request.user})



    else:
        # User is not logged in
        auth_form = auth_form or Login()
        user_form = user_form or SignUp()

        return render(request,
                      'home.html',
                      {'auth_form': auth_form, 'user_form': user_form, })


def chkstatus(request):
    user = User.objects.all()
    status = Login_status.objects.all()
    return render(request, 'alluser.html', {'users': user, 'status': status, 'cur_user': request.user})

def login_view(request):
    if request.method == 'POST':
        form = Login(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            t = Login_status.objects.get(user=request.user)
            t.is_online = 1
            t.save()
            # Success
            return redirect('/')
        else:
            # Failure
            return index(request, auth_form=form)
    return redirect('/')


def logout_view(request):
    t = Login_status.objects.get(user=request.user)
    t.is_online = 0
    t.save()
    logout(request)
    return redirect('/')

def set_offline(request):
    set_offline()


def set_online(request,u_id=0):

    t = Login_status.objects.get(user=request.user)
    t.is_online = 1
    t.last_seen=datetime.now()
    t.save()
    return HttpResponse('  ')



def signup(request):
    user_form = SignUp(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            p = Login_status(
                user=username,
                is_online=1,
            )
            p.save()
            return redirect('/')
        else:
            return index(request, user_form=user_form)
    return redirect('/')


@login_required
def user(request, u_id):
    user = User.objects.get(id=u_id)
    form = MessageForm()
    d = 0
    if request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            p = Message(
                to_user=user,
                from_user=request.user,
                msg_type='text',
                msg=request.POST['message'],
            )
            p.save()
            d = 1
            return render(request, 'user.html', {'user': user, 'd': d,'form': form,'cur_user':request.user})
    else:
        form = MessageForm()

    # return render_to_response('user.html',locals(),context_instance=RequestContext(request))
    return render(request, 'user.html', {'user': user, 'd': d, 'form': form,'cur_user':request.user})

from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_exempt
def create_post(request, u_id):
    user = User.objects.get(id=u_id)
    if request.method == 'GET':
        post_data = request.GET['message']
        form = MessageForm(request.GET)
        if form.is_valid():
            p = Message(
            to_user=user,
            from_user=request.user,
            msg_type='text',
            msg=post_data,
            )
            p.save()
            return HttpResponse(
                json.dumps("done")
            )
    return HttpResponse(
            json.dumps("notdone")
    )


@csrf_exempt
def mailuser(request, u_id):
    user = User.objects.get(id=u_id)
    if request.method == 'GET':
        post_data = request.GET['message']
        form = MessageForm(request.GET)
        if form.is_valid():
            sub = "Message from: " + request.user.username
            mail_msg = request.GET['message']
            from_email = settings.EMAIL_HOST_USER
            send_mail(sub, mail_msg, from_email, [user.username], fail_silently=False)
            p = Message(
            to_user=user,
            from_user=request.user,
            msg_type='text',
            msg=post_data,
            )
            p.save()
            return HttpResponse(
                json.dumps("done")
            )
    return HttpResponse(
            json.dumps("notdone")
    )


@login_required
def mailuser1(request, u_id):
    user = User.objects.get(id=u_id)
    form = MessageForm()
    d = 0
    if request.POST:
        form = MessageForm(request.POST)
        if (form.is_valid):
            sub = "Message from: " + request.user.username
            mail_msg = request.POST['message']
            from_email = settings.EMAIL_HOST_USER
            send_mail(sub, mail_msg, from_email, [user.username], fail_silently=False)
            p = Message(
                to_user=user,
                from_user=request.user,
                msg_type='text',
                msg=request.POST['message'],
            )
            p.save()
            d = 2
            return render(request, 'user.html', {'user': user, 'd': d,'cur_user':request.user})
    else:
        form = MessageForm()

    # return render_to_response('user.html',locals(),context_instance=RequestContext(request))
    return render(request, 'user.html', {'user': user, 'd': d, 'form': form,'cur_user':request.user})


@login_required
def chat(request):
    r = Message.objects.all()
    return render(request, 'chat.html', {'msgs': r, 'cur_user': request.user})


@login_required
def test(request):
    return render(request, 'test.html')


@login_required
@static_var('counter',0)
def test11(request, u_id):
    p = User.objects.get(id=u_id)
    r = Message.objects.filter(Q(Q(to_user=request.user.username, from_user=p.username) | Q(from_user=request.user.username, to_user=p.username))&Q(id__gt=test11.counter))
    for q in r:
        if q.id>test11.counter:
            test11.counter=q.id
    return render(request, 'chat.html', {'msgs': r, 'cur_user':request.user})




@login_required
@static_var('counter',0)
def test12(request):
    r=Message.objects.filter(Q(to_user=request.user.username)&Q(id__gt=test12.counter))
    for q in r:
        if q.id>test12.counter:
            test12.counter=q.id
    return render(request, 'recieved_chat.html', {'msgs': r})


def test13(request):
    r = Message.objects.filter(from_user=request.user.username)
    return render(request, 'sent_chat.html', {'msgs': r})


def send_message(request, u_id):
    user = User.objects.get(id=u_id)
    if request.method == "POST":
        form = MessageForm(request.POST, request.POST['message'])
        if form.is_valid():
            msg_text = request.POST['message']
            p = Message(
                to_user=user,
                from_user=request.user,
                msg_type='text',
                msg=msg_text,
            )
            p.save()
    return ('/')


@csrf_exempt
def upload(request, u_id):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            save_file(request,request.FILES['image'],u_id)
            return HttpResponse('Thanks for uploading the image')
        else:
            return HttpResponse('form not valid')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})


def save_file(request,f,u_id):
    u=uuid.uuid1()
    uid_str = u.urn
    str = uid_str[9:]
    l1='chat/static/'
    l2='uploads/'+str+'.jpeg'
    location=l1+l2
    with open(location, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    user = User.objects.get(id=u_id)
    p = Message(
                to_user=user,
                from_user=request.user,
                msg_type='image',
                msg=l2,
            )
    p.save()