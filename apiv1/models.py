from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

from .interfaces import JsonInterface


class User(models.Model, JsonInterface):
    email = models.EmailField(max_length=200)
    password_hash = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(default=timezone.now, null=True)
    last_login = models.DateTimeField(default=timezone.now, null=True)

    @staticmethod
    def signup(email, password):
        user = User()
        user.email = email
        user.password_hash = User.make_password(password)
        user.save()
        return user

    @staticmethod
    def make_password(password, *args, **kwargs) -> str:
        return make_password(password, *args, **kwargs)

    @staticmethod
    def check_password(*args, **kwargs) -> bool:
        return check_password(*args, **kwargs)


class UserSettings(models.Model, JsonInterface):
    user_id = models.IntegerField()  # Foreign key

    # Notification Settings
    receive_message_notifications = models.BooleanField(default=True)
    receive_mention_notifications = models.BooleanField(default=True)
    receive_friend_request_notifications = models.BooleanField(default=True)
    notification_delivery_method = models.CharField(max_length=50,
                                                    choices=[('push', 'Push Notifications'), ('email', 'Email'),
                                                             ('sms', 'SMS')], default='push')

    # Privacy Settings
    profile_visibility = models.CharField(max_length=50, choices=[('public', 'Public'), ('private', 'Private'),
                                                                  ('friends_only', 'Friends Only')], default='public')
    allow_friend_requests = models.BooleanField(default=True)
    allow_messages_from = models.CharField(max_length=50,
                                           choices=[('everyone', 'Everyone'), ('friends_only', 'Friends Only'),
                                                    ('no_one', 'No One')], default='everyone')
    display_online_status = models.BooleanField(default=True)

    # Appearance Settings
    theme_preference = models.CharField(max_length=50,
                                        choices=[('light', 'Light'), ('dark', 'Dark'), ('custom', 'Custom')],
                                        default='light')
    font_size = models.CharField(max_length=20, default='medium')
    font_style = models.CharField(max_length=20, default='normal')
    display_language = models.CharField(max_length=50, default='English')

    # Sound Settings
    message_notification_sound = models.CharField(max_length=100, default='default')
    event_notification_sound = models.CharField(max_length=100, default='default')

    # Security Settings
    two_factor_authentication = models.BooleanField(default=False)

    # Chat Settings
    mute_group_chat_notifications = models.BooleanField(default=False)
    leave_group_on_exit = models.BooleanField(default=False)
    enable_read_receipts = models.BooleanField(default=True)
    enable_typing_indicators = models.BooleanField(default=True)

    # Archive Settings
    auto_archive_chats = models.BooleanField(default=False)
    auto_archive_period = models.IntegerField(default=30)  # in days

    # Media Settings
    auto_download_media = models.BooleanField(default=True)
    media_quality_preference = models.CharField(max_length=20,
                                                choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
                                                default='medium')

    # Backup & Sync Settings
    backup_chat_history = models.BooleanField(default=True)

    # Blocking Settings
    # ids separated by ,
    block_users = models.CharField(default='')
    # words separated by ,
    blocked_words = models.CharField(default='')

    # Timestamps
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)


class Message(models.Model, JsonInterface):
    text = models.TextField()
    from_user_id = models.IntegerField()  # Foreign key
    to_user_id = models.IntegerField()  # Foreign key
    created_date = models.DateTimeField(default=timezone.now)
