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
        return Response({'status': '0'})
    return Response({'status': '1'})


@api_view(['GET', 'POST'])
def signup(request):
    """
    Register the user if the given email is not
    already in use
    """
    if request.method == "POST":
        return Response({'status': '0'})
    return Response({'status': '1'})


@api_view(['POST'])
def logout(request):
    """
    Log out the user
    """
    if request.method == "POST":
        return Response({'status': '0'})
    return Response({'status': '1'})


@api_view(['GET', 'POST'])
def settings(request):
    """
    The user is able to set it's email, and can delete itself
    """
    if request.method == "POST":
        return Response({'status': '0'})
    return Response({'status': '1'})


@api_view(['GET', 'POST'])
def index(request):
    """
    The user can search for other users in the database
    by their emails
    """
    if request.method == "POST":
        return Response({'status': '0'})
    return Response({'status': '1'})


@api_view(['GET', 'POST'])
def chat(request, id_or_email):
    """
    Chat with the other person based on its id_or_email
    """
    if request.method == "POST":
        return Response({'status': '0'})
    return Response({'status': '1'})
