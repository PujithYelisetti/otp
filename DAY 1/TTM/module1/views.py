import string
import random
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<center>Welcome to TTM Homepage</center>")
def newhomepage(request):
    return render(request,'newHomepage.html')

def travelpackage(request):
    return render(request,'travelpackage.html')

def print1(request):
    return render(request,'print_to_console1.html')
def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'Use input:{user_input}')
        #return HttpResponse('From submitted successfully')
        a1 ={'user_input':user_input}
        return render(request,'print_to_console1.html',a1)

def randomcall(request):
        return render(request, 'RandomOTPgenerator.html')

def RandomOTPgenerator(request):
        if request.method == "POST":
            user_input = request.POST['user_input']
            print(f'Use input:{user_input}')
            # return HttpResponse('From submitted successfully')
            a2 =int(user_input)
            ran1 =''.join(random.sample(string.digits,k=a2))

            a1 = {'ran1': ran1}
            return render(request, 'RandomOTPgenerator.html', a1)