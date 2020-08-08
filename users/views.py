from django.shortcuts import render

def signup(request):
    return render(request, 'signup.html')

def user_list(request):
    return render(request, 'user-list.html') 

def profile(request, id):

    return(request, 'profile.html')
