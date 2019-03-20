from django import forms
from django.contrib.auth.models import User
from gymbuddy.models import Comments, ProgressPics, Profile

'''
class ProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Gym
        fields = ('GymName',)
 
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the page.")
    views= forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data
'''

'''
ADD IMAGE


ADD COMMENT


'''

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    AboutMe = forms.CharField(widget=forms.Textarea, max_length=300, required=False)
    ProfilePicture = forms.ImageField(required=False)
    Height = forms.IntegerField(help_text="Please Enter your Height(cm)", required=False)
    Weight = forms.IntegerField(help_text="Please Enter your Weight(kg)", required=False)
    DoB = forms.DateField(help_text="Please Enter your Date of Birth")
    GymID = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    Following = forms.CharField(widget=forms.HiddenInput(), initial=" ", required=False)
    class Meta:
        model = Profile
        fields = ('AboutMe', 'ProfilePicture', 'Height', 'Weight', 'DoB', 'Experience') 
