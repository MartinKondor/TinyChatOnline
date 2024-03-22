from rest_framework import serializers
from .models import UserSettings


class UserSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSettings
        fields = [
            'receive_message_notifications',
            'receive_mention_notifications',
            'receive_friend_request_notifications',
            'notification_delivery_method',
            'profile_visibility',
            'allow_friend_requests',
            'allow_messages_from',
            'display_online_status',
            'theme_preference',
            'font_size',
            'font_style',
            'display_language',
            'message_notification_sound',
            'event_notification_sound',
            'two_factor_authentication',
            'mute_group_chat_notifications',
            'leave_group_on_exit',
            'enable_read_receipts',
            'enable_typing_indicators',
            'auto_archive_chats',
            'auto_archive_period',
            'auto_download_media',
            'media_quality_preference',
            'backup_chat_history',
            'created_date',
            'blocked_words',
            'block_users'
        ]
        extra_kwargs = {
            'blocked_words': {'required': False},
            'block_users': {'required': False}
        }

