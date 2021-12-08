from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

User = get_user_model()


class TeamMemberRoles(models.TextChoices):
    REGULAR = "regular", _('Regular - Can\'t delete members')
    ADMIN = "admin", _('Admin - Can delete members')


class TeamMember(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_id = models.CharField(max_length=64, validators=[validators.EmailValidator])
    mobile_number = models.CharField(max_length=15, help_text="Please use the following format: <em>XXX-XXX-XXXX</em>.")
    role = models.CharField(max_length=10, choices=TeamMemberRoles.choices, default=TeamMemberRoles.REGULAR)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
