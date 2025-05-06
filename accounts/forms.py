from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'w-full px-4 py-2 rounded-md bg-indigo-900/30 text-white border border-indigo-700 focus:outline-none focus:ring-2 focus:ring-blue-400',
            'placeholder': 'Username',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'w-full px-4 py-2 rounded-md bg-indigo-900/30 text-white border border-indigo-700 focus:outline-none focus:ring-2 focus:ring-blue-400',
            'placeholder': 'Password',
        })

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False)
    phone_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'phone_number', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 rounded-md bg-indigo-900/30 text-white border border-indigo-700 focus:outline-none focus:ring-2 focus:ring-blue-400',
            })
