from django.db import models
from django.contrib import auth


class User(auth.models.User, auth.models.PermissionsMixin):
    name = auth.models.User

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name', 'last_name']