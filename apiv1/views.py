import json
from datetime import datetime

from django.shortcuts import redirect
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
        return redirect("index")

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

    # Save last login
    user.last_login = datetime.now().isoformat()

    request.session["current_user"] = user
    return Response({'status': '1', 'current_user': user})


@api_view(['GET'])
def current_user(request):
    try:
        current_user = request.session.get('current_user')
        if current_user is not None:
            return Response({'status': '1', 'current_user': current_user})
    except Exception as e:
        print(e)
    return Response({'status': '0', 'user': None})


@api_view(['POST'])
def signup(request):
    """
    Register the user if the given email is not
    already in use
    """
    current_user = request.session.get('current_user')
    if current_user is not None:
        return redirect("index")

    # Data validation
    try:
        body = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return Response({'status': '0', 'msg': 'Bad request (1.)'})

    email = body.get("email")
    password = body.get("password")
    password_again = body.get("password_again")

    is_input_valid = lambda input: input is not None and\
       str(input).lower().strip() != 'none' and\
       len(str(input).strip()) != 0

    if not is_input_valid(email):
        return Response({'status': '0', 'msg': 'No email given'})
    if not is_input_valid(password):
        return Response({'status': '0', 'msg': 'No password given'})
    if not is_input_valid(password_again):
        return Response({'status': '0', 'msg': 'You must type the password again'})

    is_password_valid = lambda password: len(str(password)) > 2
    if not is_password_valid(password):
        return Response({'status': '0', 'msg': 'The password must be at least 3 characters long'})

    if password != password_again:
        return Response({'status': '0', 'msg': 'Passwords doesn\'t match'})

    try:
        user = User.signup(email, password)
        request.session['current_user'] = user
        return Response({'status': '1', 'current_user': user})
    except:
        return Response({'status': '0', 'msg': 'Server error, please try again later'})


@api_view(['PUT'])
def logout(request):
    """
    Log out the user
    """
    request.session['current_user'] = None
    return Response({'status': '1', 'current_user': request.session['current_user']})


@api_view(['GET', 'POST'])
def settings(request):
    """
    The user is able to set it's email, and can delete itself
    """
    current_user = request.session.get('current_user')
    if current_user is None:
        return redirect("login")

    if request.method == "POST":
        return Response({'status': '0'})
    return Response({'status': '1'})


@api_view(['GET'])
def index(request):
    """
    The user can search for other users in the database
    by their emails
    """
    current_user = request.session.get('current_user')
    context = {'status': '1', 'current_user': current_user}

    # Different context, depending on the user
    if current_user is None:
        pass
    else:
        pass

    # For now, just the same context for everyone
    context["users"] = User.objects.all()
    return Response(context)


@api_view(['GET', 'POST'])
def chat(request, id_or_email):
    """
    Chat with the other person based on its id_or_email
    """
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        return Response({'status': '0'})
    return Response({'status': '1'})
