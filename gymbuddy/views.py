from django.shortcuts import render
from django.http import HttpResponse
from gymbuddy.models import Gym
from gymbuddy.forms import UserForm, ProfileForm, EditForm, CommentForm, PictureForm
from gymbuddy.models import Profile
from gymbuddy.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

from gymbuddy.models import ProgressPics
from gymbuddy.models import Comments

def index(request):
    gym_list = Gym.objects.all()
    context_dict = {"Gyms": gym_list}
    return render(request, 'gymbuddy/index.html', context_dict)

def about(request):
    return render(request, 'gymbuddy/about.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your GymBuddy account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'gymbuddy/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'ProfilePicture' in request.FILES:
                print("Picture Present")
                profile.ProfilePicture = request.FILES['ProfilePicture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request,
                  'gymbuddy/signup.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})
				   
def contactus(request):
    return render(request, 'gymbuddy/contactus.html')

def gymprofile(request, gym_slug):
    context_dict = {}
    try:
        gym = Gym.objects.get(slug=gym_slug)
        context_dict["Gym"] = gym
        gym_id = gym.id
        people = Profile.objects.filter(GymID=gym_id)
        context_dict["People"] = people
    except Gym.DoesNotExist:
        context_dict["Gym"] = None
    try:
        profile = Profile.objects.get(user=User.objects.get(username=request.user.username))
        context_dict["Profile"] = profile
    except User.DoesNotExist:
        context_dict["Profile"] = None
    return render(request, 'gymbuddy/gymprofile.html', context=context_dict)

def userprofile(request, user_name):
    context_dict = {}
    try:
        people = Profile.objects.get(user=(User.objects.get(username=user_name)))
        context_dict["Person"] = people
        followingpeople = people.Following
        context_dict["Following"] = followingpeople
    except User.DoesNotExist:
        context_dict["Person"] = None

    try:
        pics = ProgressPics.objects.filter(UserName=(Profile.objects.get(user=(User.objects.get(username=user_name)))))
        context_dict["Pics"] = pics
    except ProgressPics.DoesNotExist:
        context_dict["Pics"] = None

    try:
        user_comments = []
        comments = Comments.objects.all()
        for comment in comments:
            if comment.OnPic in pics:
                user_comments.append(comment)
        context_dict["Comments"] = user_comments
    except Comments.DoesNotExist:
        context_dict["Comments"] = None

    return render(request, 'gymbuddy/userprofile.html', context=context_dict)

@login_required
def edit_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('index')

    if request.method == 'POST':
        edit_form = EditForm(data=request.POST, instance=profile)
        
        if edit_form.is_valid():
            profile = edit_form.save(commit=True)
            return HttpResponseRedirect(reverse('index'))
        else:
            print(edit_form.errors)
    else:
        edit_form = EditForm()

    return render(request,
                  'gymbuddy/edit_profile.html',
                  {'Profile':profile,
                   'edit_form': edit_form})

def add_comment(request, user_name, onphoto):
    try:
        poster = Profile.objects.get(user=User.objects.get(username=user_name))
        image = onphoto
    except Profile.DoesNotExist or ProgressPics.DoesNotExist:
        poster = None
        image = None
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Poster = poster
            comment.OnPic = image
            comment.save(commit=True)
            return userprofile(request, user_name)
        else:
            print(form.errors)
    return render(request, 'gymbuddy/add_comment.html', {'form': form})

def add_progresspic(request, user_name):
    try:
        poster = Profile.objects.get(user=User.objects.get(username=user_name))
    except Profile.DoesNotExist:
        poster = None
    form = PictureForm()
    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            if poster:
                picture = form.save(commit=False)
                picture.UserName = poster
                picture.Likes = 0
                if 'Photo' in request.FILES:
                    print("Picture Present")
                    picture.Photo = request.FILES['Photo']
                
                picture.save()
                return userprofile(request, user_name)
        else:
            print(form.errors)
    context_dict = {'form':form, 'UserName': poster }
    return render(request, 'gymbuddy/add_progresspic.html', context_dict)

def test(request):
    return render(request, 'gymbuddy/tester.html')

def home_gym(request, gym_slug, user):
    context_dict = {}
    try:
        gym = Gym.objects.get(slug=gym_slug)
        context_dict["Gym"] = gym
        gym_id = gym.id
        people = Profile.objects.filter(GymID=gym_id)
        context_dict["People"] = people
    except Gym.DoesNotExist:
        context_dict["Gym"] = None
    try:
        Profile.objects.filter(user=User.objects.get(username=user)).update(GymID=gym)
        profile = Profile.objects.get(user=User.objects.get(username=request.user.username))
        context_dict["Profile"] = profile
    except User.DoesNotExist:
        context_dict["Profile"] = None
    return render(request, 'gymbuddy/gymprofile.html', context=context_dict)