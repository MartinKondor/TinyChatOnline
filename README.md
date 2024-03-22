
<p align="center">
</p>

# TinyChatOnline

🐍Django, ❄️React, 🐘PostgreSQL chat web service with simple authentication.

This is the online and modernized version of [TinyChat](https://github.com/MartinKondor/TinyChat).

## How to run

Install dependencies:
```commandline
py -m pip install -r requirements.txt
cd public
npm i
```

Configure the database in the `TinyChatOnline/settings.py` file then migrate:
```commandline
py manage.py makemigrations
py manage.py migrate
```

Then run the server & react:
```commandline
py manage.py runserver 127.0.0.1:8080
cd public
npm start
```

## Custom Commands

### Test/Dummy Database

To test the application with example data, you can run the command:
```commandline
py manage.py dummydb
```
Which will create some dummy data in the database.

### Clear Database

To delete every row from the database, you can run the following command:
```commandline
py manage.py cleardb
```

## Testing

You can use the shared [Postman](https://api.postman.com/collections/33777629-ad8e9320-a943-4377-9668-5d8aff884cf2?access_key=PMAT-01HSJKKTN8D4AB36Z5DT1KWG05) collection.

## Features

* Log-In/Sign-Up with email/username
* Chat with others using a chat interface
* Set profile image and nicknames in chats

## Authors

* [MartinKondor](https://github.com/MartinKondor)
