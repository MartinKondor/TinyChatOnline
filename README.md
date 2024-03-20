
<p align="center">
</p>

# TinyChatOnline

🐍Django, ❄️React, 🐘PostgreSQL chat web service with simple authentication.

This is the online and modernized version of [TinyChat](https://github.com/MartinKondor/TinyChat).

## How to run

Install dependencies:
```commandline
py -m pip install -r requirements.txt
```

Configure the database in the `TinyChatOnline/settings.py` file then migrate:
```commandline
py manage.py makemigrations
py manage.py migrate
```

Then run the server wit your `HOST` and `PORT`:
```commandline
py manage.py runserver <HOST>:<PORT>
```

## Features

* Log-In/Sign-Up with email/username
* Chat with others using a chat interface
* Set profile image and nicknames in chats

## Authors

* [MartinKondor](https://github.com/MartinKondor)
