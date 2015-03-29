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
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .functions import handle_uploaded_file

import datetime
from django.utils.timezone import now as utcnow
from django.utils.safestring import mark_safe
from .forms import MessageForm, ImageForm

import json
from django.utils.safestring import mark_safe
# Create your views here.


def index(request, auth_form=None, user_form=None):
    # User is logged in
    if request.user.is_authenticated():
        user=User.objects.all()
        status=Login_status.objects.all()
        return render(request,'index.html',{'users':user,'status':status,'cur_user':request.user})



    else:
        # User is not logged in
        auth_form = auth_form or Login()
        user_form = user_form or SignUp()

        return render(request,
                      'home.html',
                      {'auth_form': auth_form, 'user_form': user_form, })

def login_view(request):
    if request.method == 'POST':
        form = Login(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            t=Login_status.objects.get(user=request.user)
            t.is_online=1
            t.save()
            # Success
            return redirect('/')
        else:
            # Failure
            return index(request, auth_form=form)
    return redirect('/')


def logout_view(request):
    t=Login_status.objects.get(user=request.user)
    t.is_online=0
    t.save()
    logout(request)
    return redirect('/')


def signup(request):
    user_form = SignUp(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            p=Login_status(
                user=username,
                is_online=1,
                )
            p.save()
            return redirect('/')
        else:
            return index(request, user_form=user_form)
    return redirect('/')


@login_required
def user(request,u_id):
    user=User.objects.get(id=u_id)
    form = MessageForm()
    d = 0
    if request.POST:
        form=MessageForm(request.POST)
        if(form.is_valid):
            p=Message(
                to_user=user,
                from_user=request.user,
                msg_type = 'text',
                msg=request.POST['message'],
            )
            p.save()
            d=1
            return render(request,'user.html',{'user':user,'d':d})
    else:
        form = MessageForm()

    #return render_to_response('user.html',locals(),context_instance=RequestContext(request))
    return render(request,'user.html',{'user':user, 'd':d, 'form':form})

@login_required
def mailuser(request,u_id):
    user=User.objects.get(id=u_id)
    form = MessageForm()
    d = 0
    if request.POST:
        form=MessageForm(request.POST)
        if(form.is_valid):
            sub = "Message from: "+ request.user.username
            mail_msg =request.POST['message']
            from_email = settings.EMAIL_HOST_USER
            send_mail(sub , mail_msg , from_email ,[user.username] , fail_silently=False)
            p=Message(
                to_user=user,
                from_user=request.user,
                msg_type = 'text',
                msg=request.POST['message'],
            )
            p.save()
            d=2
            return render(request,'user.html',{'user':user,'d':d})
    else:
        form = MessageForm()

    #return render_to_response('user.html',locals(),context_instance=RequestContext(request))
    return render(request,'user.html',{'user':user,'d':d, 'form':form})




@login_required
def chat(request):
	r = Message.objects.all()
	return render(request, 'chat.html', {'msgs':r,'cur_user':request.user})

def test(request):
	return render(request, 'test.html')


@login_required
def test12(request):
	r = Message.objects.filter(to_user=request.user.username)
	return render(request, 'test12.html', {'msgs':r})


def send_message(request):
    #do nothing
    return('/')

def upload_image(request,u_id):
    '''Simple view method for uploading an image

    '''
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES['POST'])
        if form.is_valid():
            save_file(request.FILES['image'])
            return HttpResponse('Thanks for uploading the image')
        else:
            return HttpResponse('Invalid image')
    else:
        form = ImageForm()
    return render (request,'upload.html', {'form': form})

def save_file(file, path=''):
    ''' Little helper to save a file
    '''
    filename = file._get_name()
    fd = open('%s/%s' % (MEDIA_ROOT, str(path) + str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()