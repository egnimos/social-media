from django.forms import ModelForm
from .models import SocialProfile

class SocialProfileModalForm(ModelForm):
    class Meta:
        model = SocialProfile
        fields =["first_name", "last_name", 'bio', 'avatar']