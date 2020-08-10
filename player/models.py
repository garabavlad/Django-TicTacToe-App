from django.contrib.auth.models import User
from django.db import models


class Invitation(models.Model):


    def __str__(self):
        return "{0} => {1} :: {2}".format(
            self.from_user.username,
            self.to_user.username,
            self.message
        )

    from_user = models.ForeignKey(User, related_name="invitations_sent", on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User,
        related_name="invitations_received",
        on_delete=models.CASCADE,
        verbose_name="User to invite",
        help_text="Please select the user you want to invite"
    )
    message = models.CharField(
        max_length=300,
        verbose_name="Optional Message",
        help_text="Some challenging message to the opponent?"
    )
    timestamp = models.DateTimeField(auto_now_add=True)