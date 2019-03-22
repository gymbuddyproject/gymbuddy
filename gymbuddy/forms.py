from django import forms
from django.contrib.auth.models import User
from gymbuddy.models import Comments, ProgressPics, Profile
from django.contrib.auth.forms import UserChangeForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    ProfilePicture = forms.ImageField(required=False)
    DoB = forms.DateField(help_text="Please Enter your Date of Birth")
    GymID = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    Following = forms.CharField(widget=forms.HiddenInput(), initial=" ", required=False)
    class Meta:
        model = Profile
        fields = ('AboutMe', 'ProfilePicture', 'Height', 'Weight', 'DoB', 'Experience')

class EditForm(UserChangeForm):
    ProfilePicture = forms.ImageField(required=False)
    AboutMe = forms.CharField(widget=forms.Textarea, max_length=300, required=False, )
    Height = forms.IntegerField(help_text="Please Enter your Height(cm)", required=False)
    Weight = forms.IntegerField(help_text="Please Enter your Weight(kg)", required=False)
    password = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Profile
        fields = ('ProfilePicture', 'AboutMe', 'Height', 'Weight', 'Experience')
    
    def clean_password(self):
        return ""

class CommentForm(forms.ModelForm):
    Comment = forms.CharField(widget=forms.Textarea, max_length=200, required=False)
    class Meta:
        model = Comments
        fields = ['Comment']

class PictureForm(forms.ModelForm):
    Photo = forms.ImageField(required=False)
    class Meta:
        model = ProgressPics
        fields = ['Photo']

