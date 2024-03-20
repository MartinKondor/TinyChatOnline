from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout
)
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def login(request):
    """
    Log in the user if the password is correct
    """
    if request.method == "POST":
        pass
    return Response({'message': 'login'})


def signup(request):
    """
    Register the user if the given email is not
    already in use
    """
    if request.method == "POST":
        pass
    return HttpResponse("signup")


def logout(request):
    """
    Log out the user
    """
    return HttpResponse("logout")


def settings(request):
    """
    The user is able to set it's email, and can delete itself
    """
    if request.method == "POST":
        pass
    return HttpResponse("settings")


def index(request):
    """
    The user can search for other users in the database
    by their emails
    """
    return HttpResponse("index")


def chat(request, id_or_email):
    """
    Chat with the other person based on its id_or_email
    """
    if request.method == "POST":
        pass
    return HttpResponse("chat_by_email")
