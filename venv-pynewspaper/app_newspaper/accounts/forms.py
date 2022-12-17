from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
class CustomUseCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model= CustomUser
        fields=(
            'username',
            'email',
            'age',
        )

class CustomUseChangeForm(UserChangeForm):
    class Meta:
        model= CustomUser
        fields=(
            'username',
            'email',
            'age',
        )
