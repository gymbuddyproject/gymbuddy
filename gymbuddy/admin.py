from django.contrib import admin
from gymbuddy.models import Gym 
from gymbuddy.models import Profile
from gymbuddy.models import ProgressPics
from gymbuddy.models import Comments

# Register your models here.
admin.site.register(Gym)
admin.site.register(Profile)
admin.site.register(ProgressPics)
admin.site.register(Comments)
