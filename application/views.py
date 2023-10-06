from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.models import User

from django.http import HttpResponse

from django.shortcuts import redirect, render


# Create your views here.



def home(request):

    return render(request,"application/index.html")


def signUp(request):


    if request.method=="POST":

        username=request.POST["username"]      # or you can also write like request.POST.get('username)

        fname=request.POST["fname"]

        lname=request.POST['lname']

        email=request.POST['email']

        pass1=request.POST['pass1']

        pass2=request.POST['pass2']


        myuser=User.objects.create_user(username,email,pass1)

        myuser.first_name=fname

        myuser.last_name=lname


        myuser.save()  

        #the user registered succesfully so now if we want to show a text that user registered succesfully we import message from contrib library

        messages.success(request,'Your Account has been created.')


        return redirect('signIn')   #it will redirect you to signIn page after signUp process


    return render(request,'application/signUp.html')



def signIn(request):

    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        user= authenticate(request, username=username, password=pass1)    #it will check that the password and the user is matches with the pass and user in the database or not
        if user is not None:
            login(request, user) 
            fname=user.first_name
            return render(request,'application\index.html',{'fname':fname})
        else:
            messages.error(request,'Bad Credentials !')
            return redirect('home')
    return render(request,'application/signIn.html')



def signOut(request):
    logout(request)
    messages.success(request,"Logged Out Successfully !")
    return redirect('home')