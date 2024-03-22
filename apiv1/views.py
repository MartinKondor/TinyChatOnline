import json
from datetime import datetime

from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User, Message, UserSettings
from .serializers import UserSettingsSerializer


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
    current_user = request.session.get('current_user')
    if current_user is not None:
        return Response({'status': '0', 'msg': 'User is authenticated'})

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
        return Response({'status': '0', 'msg': 'User is authenticated'})

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


@api_view(['GET', 'PUT'])
def settings(request):
    """
    The user is able to set its email, and can delete itself
    """
    current_user = request.session.get('current_user', request.data.get('current_user'))
    if current_user is None:
        return Response({'status': '0', 'msg': 'User is not authenticated'})

    try:
        user_settings = UserSettings.objects.get(user_id=current_user['id'])
    except UserSettings.DoesNotExist:
        user_settings = UserSettings.objects.create(user_id=current_user['id'])

    if request.method == "PUT":
        serializer = UserSettingsSerializer(user_settings, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': '1',
                'current_user': current_user,
                'user_settings': serializer.data
            })
        return Response({'status': '0', 'msg': serializer.errors})

    return Response({
        'status': '1',
        'current_user': current_user,
        'user_settings': user_settings
    })


@api_view(['GET'])
def index(request):
    """
    The user can search for other users in the database
    by their emails
    """
    current_user = request.session.get('current_user')
    context = {'status': '1', 'current_user': current_user}

    # Different context, depending on the user
    users = User.objects.all()
    if current_user is None:
        context["users"] = users
    else:
        context["users"] = [u for u in users if u.id != current_user['id']]

    # Pagination
    paginator = PageNumberPagination()
    paginator.page_size = 5  # Number of users per page
    paginated_users = paginator.paginate_queryset(context["users"], request)

    context["users"] = sorted(paginated_users, key=lambda u: u.last_login, reverse=True)
    return Response(context)


@api_view(['GET', 'POST'])
def chat(request, id):
    """
    Chat with the other person based on its id_or_email
    """
    current_user = request.session.get('current_user')
    if current_user is None:
        return Response({'status': '0', 'msg': 'User is not authenticated'})

    if id == current_user['id']:
        return Response({'status': '0', 'msg': 'Not allowed to message yourself'})

    # Find the other user
    try:
        other_user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({'status': '0', 'msg': f'Cannot find the other user: {id}'})

    if request.method == "POST":
        text = request.data['text']

        # Validation of user input
        is_valid_text = lambda text: len(str(text)) > 0 and text is not None and text != 'None'
        if not is_valid_text(text):
            return Response({'status': '0', 'msg': 'Nothing to send'})
        else:
            message = Message.send(
                text=text,
                from_user_id=current_user['id'],
                to_user_id=id
            )
            return Response({'status': '1', 'msg': 'Message sent', 'sent_message': message})

    messages = Message.objects.filter(from_user_id=current_user['id'], to_user_id=other_user.id)
    messages = sorted(messages, key=lambda m: m.created_date, reverse=False)
    return Response({
        'status': '1',
        'current_user': current_user,
        'other_user': other_user,
        'messages': messages
    })
