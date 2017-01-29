from django.shortcuts import render, HttpResponse, redirect
from models import User, Appointment
from django.contrib import messages
from django.urls import reverse
from datetime import *

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
        print "Login validation complete"
        # print result

        if result[0] == False:
            print_messages(request, result[1])
            return redirect(reverse('index'))
        # print request
        print result[1]
        print "Passing to the login function"
        return login(request, result[1])
    else:
        print "Method's not even post for loginvalidate"
        return redirect('/')

def login(request, user):
    print "Here at Login"
    request.session['user'] = {
    'id': user.id,
    'firstname' : user.firstname,
    'lastname' : user.lastname,
    'email' : user.email,
    'dob' : user.dob,
    }
    return redirect('success')

def registervalidate(request):
    result= User.objects.registervalidation(request.POST)

    if not result[0]:
        print_messages(request, result[1])
        return redirect('/')

    return login(request, result[1])

def success(request):
    if not 'user' in request.session:
        return redirect('/')
    t = datetime.now()
    time = ("%s/%s/%s" % (t.month, t.day, t.year))+ (" %s:%s:%s" % (t.hour, t.minute, t.second))
    print t.date
    today= Appointment.objects.filter(date=date.today(), user=request.session['user']['id']).order_by('time')
    future= Appointment.objects.filter(date__range=[date.today(),"9999-12-31"]).exclude(date=date.today()).filter(user=request.session['user']['id'])
    context = {
    "todaylist":today,
    "apptlist":future,
    "timekey":time
    }
    return render(request, 'login_registration/success.html', context)
def addappt(request):
    if request.method =='POST':
        result = Appointment.objects.apptvalidation(request.POST, request.session['user']['id'])
        print result
        if not result[0]:
            print_messages(request, result[1])
            return redirect(reverse('success'))
    return redirect('/success')
def editappt(request,id):
    if request.method == 'POST':
        edit_appt=Appointment.objects.filter(id=id)
    context = {
    "todaylist":edit_appt
    }


    return render(request, 'login_registration/editappt.html',context)
def submitedit(request,id):
    if request.method == 'POST':
        toedit = Appointment.objects.filter(id=id).update(tasks=request.POST['appttasks'],date=request.POST['apptdate'], time=request.POST['appttime'])
    return redirect('/success')
def deleteappt(request,id):
    if request.method == "POST":
        delete = Appointment.objects.filter(id=id).delete()
    return redirect('/success')


def logout(request):
    request.session.clear()
    # request.session.pop('user')
    return redirect('/')
