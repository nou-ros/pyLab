from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
#for working with flash messages in bootstrap
from django.contrib import messages
from animilog.models import Post   

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    
    # messages.error(request, 'Welcome to Contact')
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            #error have to handle via settings.py file with tags
            messages.error(request, "Please fill the from correctly!")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been sent!")        

    return render(request, 'home/contact.html')

def search(request):
    query=request.GET['query']
    if len(query)>75:
        allPosts = Post.objects.none()
    #title__icontains to match with the search query
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    
    if allPosts.count() == 0:
         messages.warning(request, "No search results found!")

    context = {'allPosts': allPosts,'query':query}
    return render(request, 'home/search.html', context)
    # return HttpResponse("this is search")

def handleSignup(request):
    if request.method == 'POST':
        # get post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for errorneous inputs
        #username should be under 10 characters
        if len(username) > 10:
            messages.error(request, "username must be under 10 characters")
            return redirect('/')
        #username should be alphanumeric
        if not username.isalnum():
            messages.error(request, "username should only contain letters and numbers")
            return redirect('/')
        #password should match
        if pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect('/')

        #create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your animifo account has been successfully created!")
        return redirect('/')

    else:
        return HttpResponse('404 Not found')   


def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpassword)
        
        # when info is wrong then user will be none
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In!")
            return redirect('/blog')
        else:
            messages.error(request, "Invalid Credentials. Please try again!")
            return redirect('home')


    return HttpResponse('404 - Not Found') 


def handleLogout(request):
        logout(request)
        messages.success(request, 'You are logged out!')
        return redirect('home')