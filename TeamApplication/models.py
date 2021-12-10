from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

import re

phone_regex = re.compile(r'[0-9]{3}-[0-9]{3}-[0-9]{4}$')

User = get_user_model()


class TeamMemberRoles(models.TextChoices):
    REGULAR = "regular", _('Regular - Can\'t delete members')
    ADMIN = "admin", _('Admin - Can delete members')


def validate_phone_number(value):
    if phone_regex.fullmatch(value) is None:
        raise ValidationError(
            _('%(value)s is not a phone number'),
            params={'value': value},
        )


class TeamMember(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_id = models.EmailField(max_length=64)
    mobile_number = models.CharField(
        max_length=15,
        help_text="Please use the following format: <em>XXX-XXX-XXXX</em>.",
        validators=[validate_phone_number]
    )
    role = models.CharField(max_length=10, choices=TeamMemberRoles.choices, default=TeamMemberRoles.REGULAR)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def is_admin(self):
        return self.role == TeamMemberRoles.ADMIN
