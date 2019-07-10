from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# from backEnd.account.api.serializers import FileSerializer
from django.contrib.auth import (
    authenticate,
    login,
    logout,

)
from django.shortcuts import render, redirect

from account.api.serializers import FileSerializer
from .forms import UserLoginForm, UserRegisterForm

import django.http
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegisterForm


# Create your views here.

def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "form.html", {"form": form, "title": title})
