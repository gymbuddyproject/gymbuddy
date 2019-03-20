from django.conf.urls import url
from django.contrib import admin
from gymbuddy import views

app_name = "gymbuddy"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^test/', views.test, name='test'),
	url(r'^gym/(?P<gym_slug>[\w\-]+)/$', views.gymprofile, name='gym_profile'),
    url(r'^user/(?P<user_name>[\w\-]+)/$', views.userprofile, name='user_profile'),
    url(r'^contactus/', views.contactus, name='contactus'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.login, name='login'),
    url(r'^admin/', admin.site.urls),
]
