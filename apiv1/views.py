import json

from django.shortcuts import redirect
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout
)
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User, Message


@api_view(['POST'])
def login(request):
    """
    Log in the user if the password is correct

    Example POST request:
    {
        "email": "SIOlchxZie@example.com",
        "password": "test"
    }
    """
    if request.user.is_authenticated:
        return redirect("/")

    try:
        body = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return Response({'status': '0', 'msg': 'Bad request (1.)'})

    email = body.get("email")
    password = body.get("password")

    if email is None or password is None:
        return Response({'status': '0', 'msg': 'Bad request (2.)'})

    user = User.objects.filter(email=email).first()
    if user is None:
        return Response({'status': '0', 'msg': 'Wrong password or email'})

    if User.check_password(user.password_hash, password):
        return Response({'status': '0', 'msg': 'Wrong password or email'})

    request.user = user
    request.user.is_authenticated = True
    return Response({'status': '1'})


@api_view(['GET'])
def current_user(request):
    print(request.session)
    try:
        cu = None
        if request.user.is_authenticated:
            cu = User.objects.filter(email__contains=request.user.username).first().to_dict()
        return Response({'status': '1', 'user': cu})
    except Exception as e:
        print(e)
        return Response({'status': '0', 'user': None})


@api_view(['POST'])
def signup(request):
    """
    Register the user if the given email is not
    already in use
    """
    if request.user.is_authenticated:
        return redirect("/")

    return Response({'status': '0'})


@api_view(['PUT'])
def logout(request):
    """
    Log out the user
    """
    try:
        request.user = None
        django_logout(request)
    except Exception as e:
        print(e)
        return Response({'status': '0'})
    return Response({'status': '1'})


@api_view(['GET', 'POST'])
def settings(request):
    """
    The user is able to set it's email, and can delete itself
    """
    if not request.user.is_authenticated:
        return redirect("/login")

    if request.method == "POST":
        return Response({'status': '0'})
    return Response({'status': '1'})


@api_view(['GET'])
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
    if not request.user.is_authenticated:
        return redirect("/login")

    if request.method == "POST":
        return Response({'status': '0'})
    return Response({'status': '1'})
