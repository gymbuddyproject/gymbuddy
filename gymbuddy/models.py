from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone


class Gym(models.Model):
    GymName = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    X_Coord = models.DecimalField(max_length=10, decimal_places=6, max_digits=9)
    Y_Coord = models.DecimalField(max_length=10, decimal_places=6, max_digits=9)
    Rating = models.DecimalField(max_length=3, decimal_places=2, max_digits=4)
    OpeningHours = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique=True)
    WebsiteURL = models.CharField(max_length=50, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.GymName)
        super(Gym, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Gyms"

    def __str__(self):
        return self.GymName


def profile_directory_path(instance, PhotoID):
    return '{0}/{1}'.format(instance.user.username, PhotoID)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    AboutMe = models.TextField(max_length=300, blank=True)
    ProfilePicture = models.ImageField(upload_to=profile_directory_path, blank=True)
    GymID = models.ForeignKey(Gym, blank=True, null=True)
    Following = models.CharField(max_length=300, blank=True)
    Height = models.DecimalField(max_length=3, decimal_places=2, max_digits=5, null=True)
    Weight = models.IntegerField(null=True)
    DoB = models.DateField()

    experience_choices = (('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'))
    Experience = models.CharField(max_length=12, choices=experience_choices, default='Beginner')

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username


def progress_directory_path(instance, PhotoID):
    return '{0}/progress_pics/{1}'.format(instance.UserName.user.username, PhotoID)


class ProgressPics(models.Model):
    PhotoID = models.AutoField(primary_key=True)
    UserName = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Photo = models.ImageField(upload_to=progress_directory_path)
    Likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "ProgressPics"


class Comments(models.Model):
    CommentID = models.AutoField(primary_key=True)
    Poster = models.ForeignKey(Profile, on_delete=models.CASCADE)
    OnPic = models.ForeignKey(ProgressPics, on_delete=models.CASCADE)
    Date = models.DateTimeField(default=timezone.now)
    Comment = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Comments"
