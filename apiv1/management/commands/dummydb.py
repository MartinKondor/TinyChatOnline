import random
import string

from django.core.management.base import BaseCommand
from model_bakery import baker
from tqdm import tqdm

from ...models import User, Message


class Command(BaseCommand):
    help = 'Initialize a dummy database'

    @staticmethod
    def get_random_str(length):
        return ''.join(random.choice(string.ascii_letters + " ") for _ in range(length))

    def handle(self, *args, **options):

        # Create 10 users
        users = [baker.make(User) for i in range(10)]
        user_ids = [user.id for user in users]

        # Set a password for each user
        for user in tqdm(users, desc="Creating user passwords"):
            user.password_hash = User.make_password("test")
            user.save()

        # Choose pairs to create messages
        message_id_pairs = []
        for i, j in zip(user_ids, user_ids[::-1]):
            if i == j:
                continue
            if (i, j) in message_id_pairs or (j, i) in message_id_pairs:
                continue

            message_id_pairs.append((i, j))  # Message from a to b
            message_id_pairs.append((i, j))  # Message from a to b
            message_id_pairs.append((j, i))  # Message from b to a
            message_id_pairs.append((i, j))  # Message from a to b
            message_id_pairs.append((j, i))  # Message from b to a
            message_id_pairs.append((i, j))  # Message from a to b

        for id_a, id_b in message_id_pairs:
            msg = Message()
            msg.text = Command.get_random_str(64)
            msg.from_user_id = id_a
            msg.to_user_id = id_b
            msg.save()

        self.stdout.write('Dummy data saved successfully!')
