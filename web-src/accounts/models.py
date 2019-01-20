from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    bio = models.TextField(max_length=500, blank=True, default='')
    profile_image = models.ImageField(null=True, blank=True, upload_to='users/')

    class Meta:
        default_permissions = ()
        permissions = (
            ("add_user", "add user"),
            ("change_user", "update user"),
            ("delete_user", "delete user"),
            ("view_user", "view user"),
        )

    def get_full_name(self):
        # get the full name of the user
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    def __str__(self):
        return self.username + ' | ' + self.get_full_name()

