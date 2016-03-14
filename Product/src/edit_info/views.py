#Imports to render pages, redirect and give error404
from django.shortcuts import render, get_object_or_404, redirect

#Login imports
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf

#importing models
from web.models import Project, Counselor

@login_required
def edit_hub(request):
    c = get_object_or_404(Counselor, account_id=request.user.id)
    context = {'counselor': c,}

    print(c.name, "has user id:", request.user.id, "and username:", request.user.username)
    return render(request, "edit_info/edit_hub.html", context)

# Login Views:
#Displays login screen
def login(request):
    context = {"bad_login": False}
    #security stuff
    context.update(csrf(request))
    return render(request, 'edit_info/login.html', context)

#authenticates login request
def auth_login(request):
    #gets user login input from the post request
    username = request.POST['username']
    password = request.POST['password']
    #authenticates user, if not authenticated returns None
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        #login user
        auth.login(request, user)

        #On succesful login redirect to edithub
        return redirect('edit hub')
    else:
        #if user cant be authenticated render invalid login
        return render(request, 'edit_info/login.html', {"bad_login": True})

#logs user out
def logout(request):
    auth.logout(request)
    #after logout redirect to index
    return redirect('index')
