from django.db import models
from django.contrib.auth.models import User
import random
import string
import random

# Function to generate a unique 6-character ID
# def generate_unique_id():
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# class User(models.Model):
#     id = models.CharField(max_length=6, primary_key=True, default=generate_unique_id, editable=False)
#     birth_date = models.DateField()
#     password = models.CharField(max_length=128)  # Use appropriate hashing for passwords in practice
#     user_wisdom = models.ManyToManyField('Wisdom', related_name='users', blank=True)

#     def __str__(self):
#         return self.id

class Wisdom(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted')
    text = models.TextField(max_length=1000, verbose_name='text')
    report = models.PositiveIntegerField(default=0, verbose_name='report')
    accepted = models.ManyToManyField(User, related_name='accepted')
    reply = models.BooleanField(default=True)

    @classmethod
    def wisdome_choice(cls):
        count = cls.objects.count()
        if count == 0:
            return None
        random_index = random.randint(0, count - 1)
        return cls.objects.all()[random_index]

