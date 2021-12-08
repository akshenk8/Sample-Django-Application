from django.forms import ModelForm
from . import models


class TeamMemberForm(ModelForm):
    class Meta:
        model = models.TeamMember
        exclude = ('user', )
