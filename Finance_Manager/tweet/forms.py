from django import forms
from .models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TweetForm(forms.ModelForm):
    
    class Meta:
        model = Tweet
        fields = ['content', 'photo']

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'What\'s happening?',
                'rows': 4,
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 cursor-pointer dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
            }),
        }

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


