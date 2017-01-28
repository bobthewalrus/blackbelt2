from django.shortcuts import render, HttpResponse, redirect
from models import User
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def index(request):

    return render(request, "login_registration/index.html")

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request,messages.INFO, message)

def loginvalidate(request):
    if request.method == "POST":
        print 'here'
        print request.POST['email']
        result = User.objects.loginvalidation(request.POST)
        print result

        if result[0] == False:
            print_messages(request, result[1])
            return redirect(reverse('index'))
        return login(request, result[1])
    return redirect('/')

def login(request, user):
    print "Here at Login"
    request.session['user'] = {
    'id': user.id,
    'first_name' : user.firstname,
    'last_name' : user.lastname,
    'email' : user.email,
    }

def registervalidate(request):
    result= User.objects.registervalidation(request.POST)

    if not result[0]:
        print_messages(request, result[1])
        return redirect('/')

    return login(request, result[1])

def success(request):
    if not 'user' in request.session:
        return redirect('/')
    return render(request, 'login_registration/success.html')



    return redirect('/success')
def logout(request):
    request.session.clear()
    # request.session.pop('user')
    return redirect('/')