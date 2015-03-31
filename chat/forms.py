__author__ = 'gd'
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags
from chat.models import Message

class SignUp(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Name'}))
    username = forms.CharField(required=True, widget=forms.widgets.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))

    def is_valid(self):
        form = super(SignUp, self).is_valid()
        for f, error in self.errors.items():
            if f != '__all_':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

    class Meta:
        fields = ['first_name', 'username', 'password1',
                  'password2']
        model = User

class Login(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.EmailInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))

    def is_valid(self):
        form = super(Login, self).is_valid()
        for f, error in self.errors.items():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

class MessageForm(forms.Form):
    message = forms.CharField(widget = forms.Textarea(attrs={'id': 'post-text','cols':50,'rows':2}))
    class Meta:
        fields = ['message']
        model = Message

class ImageForm(forms.Form):
    """Image upload form."""
    image = forms.FileField()