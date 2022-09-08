from django.shortcuts import render, redirect, reverse
from .email_backend import EmailBackend
from django.contrib import messages
from .forms import CustomUserForm
from voting.forms import VoterForm
from django.contrib.auth import login, logout
from time import sleep
from stega.asd import _encode, _decode
from django.conf import settings
import jwt
import base64

# Create your views here.

def account_login(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return redirect(reverse("adminDashboard"))
        else:
            return redirect(reverse("voterDashboard"))

    context = {}
    if request.method == 'POST':
        user = EmailBackend.authenticate(request, username=request.POST.get(
            'email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            if user.user_type == '1':
                return redirect(reverse("adminDashboard"))
            else:
                return redirect(reverse("voterDashboard"))
        else:
            messages.error(request, "Invalid details")
            return redirect("/")

    return render(request, "voting/login.html", context)

def download_image(request, user_type):
    print(request.user.admin.email)
    return HTTPResponse("asas")

# This is used to encrypt our data 
def generate_stega_images(voter):
    token_ = voter.token.split(".")[1]
    print("This the token stored in the file %s" % token_)
    filename_ = base64.b64encode(voter.admin.email.strip().encode()).decode()
    _encode(token_, filename_)
    return ("%s1.png") % filename_

def account_register(request):
    userForm = CustomUserForm(request.POST or None)
    voterForm = VoterForm(request.POST or None)
    context = {
        'form1': userForm,
        'form2': voterForm
    }
    if request.method == 'POST':
        if userForm.is_valid() and voterForm.is_valid():
            user = userForm.save(commit=False)
            voter = voterForm.save(commit=False)
            voter.admin = user

            payload = {"email": user.email}
            token = jwt.encode(payload,settings.SECRET_KEY, "HS256")
            voter.token = token
            voter.path = generate_stega_images(voter)
            
            # genenate an image to be used for voting
            user.save()
            voter.save()
            
            messages.success(request, "Account created. You can login now!")
            return redirect(reverse('account_login'))
        else:
            messages.error(request, "Provided data failed validation")
            # return account_login(request)
    return render(request, "voting/reg.html", context)


def account_logout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        messages.success(request, "Thank you for visiting us!")
    else:
        messages.error(
            request, "You need to be logged in to perform this action")

    return redirect(reverse("account_login"))
