from django.shortcuts import render

def user_list(request):
    return render(request, 'user-list.html') 

def profile(request):
    return(request, 'profile.html')
    