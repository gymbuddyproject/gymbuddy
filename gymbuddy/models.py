from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Gym(models.Model):
    GymName = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    X_Coord = models.DecimalField(max_length=10, decimal_places=6, max_digits=9)
    Y_Coord = models.DecimalField(max_length=10, decimal_places=6, max_digits=9)
    Rating = models.DecimalField(max_length=3, decimal_places=2, max_digits=4)
    OpeningHours = models.CharField(max_length=50)
    
    class Meta:
      verbose_name_plural = "Gyms"
      
    def __str__(self):
        return self.GymName 
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    AboutMe = models.TextField(max_length=300)
    Following = models.CharField(max_length = 20)
    ProfilePicture = models.ImageField(upload_to='profile_images', blank=True)
    GymID = models.ForeignKey(Gym)
    Height = models.DecimalField(max_length=3, decimal_places=2, max_digits=5)
    Weight = models.IntegerField()
    DoB = models.DateField()
    experience_choices = (('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'))
    Experience = models.CharField(max_length=12, choices=experience_choices, default='Beginner')

    class Meta:
      verbose_name_plural = "Profiles"

    def __str__(self):
      return self.user.username

class ProgressPics(models.Model):
    PhotoID = models.AutoField(primary_key=True)
    UserName = models.ForeignKey(User)
    Photo = models.ImageField(upload_to='progress_pics', blank=True)
    Likes = models.IntegerField(default=0)
    
    class Meta:
      verbose_name_plural = "ProgressPics"

class Comments(models.Model):
    CommentID = models.AutoField(primary_key=True)
    Poster = models.ForeignKey(Profile)
    OnPic = models.ForeignKey(ProgressPics)
    Date = models.DateField(max_length=128)
    Comment = models.CharField(max_length=200)

    class Meta:
      verbose_name_plural = "Comments"
