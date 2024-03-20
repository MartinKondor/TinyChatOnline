from django.shortcuts import render
from django.http import HttpResponse


def login():
    """
    Log in the user if the password is correct
    """
    return HttpResponse("login")


def signup():
    """
    Register the user if the given email is not
    already in use
    """
    return HttpResponse("signup")


def logout():
    """
    Log out the user
    """
    return HttpResponse("logout")


def settings():
    """
    The user is able to set it's email, and can delete itself
    """
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
    return HttpResponse("chat_by_email")
