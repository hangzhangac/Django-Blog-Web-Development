from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Follow(models.Model):
    followed = models.ForeignKey(
        User, related_name="followed_user", on_delete=models.CASCADE)
    fan = models.ForeignKey(
        User, related_name="fan_user", on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} has followed {}".format(self.fan, self.followed)
