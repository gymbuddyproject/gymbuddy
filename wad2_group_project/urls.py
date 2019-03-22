from django.conf.urls import url
from django.contrib import admin
from gymbuddy import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "gymbuddy"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^test/', views.test, name='test'),
    url(r'^gym/(?P<gym_slug>[\w\-]+)/$', views.gymprofile, name='gym_profile'),
    url(r'^gym/(?P<gym_slug>[\w\-]+)/(?P<user>[\w\-]+)/$', views.home_gym, name='home_gym'),
    url(r'^user/(?P<user_name>[\w\-]+)/$', views.userprofile, name='user_profile'),
url(r'^user/(?P<other_username>[\w\-]+)/(?P<username>[\w\-]+)/$', views.follow_user, name='follow_user'),
    url(r'^contactus/', views.contactus, name='contactus'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^deactivate/$', views.user_deactivateaccount, name='deactivate'),
    url(r'^edit/(?P<user_name>[\w\-]+)/$', views.edit_profile, name='edit_profile'),
    url(r'^user/(?P<user_name>[\w\-]+)/(?P<pic_id>[\w\-]+)/add_comment/$', views.add_comment, name='add_comment'),
    url(r'^user/(?P<user_name>[\w\-]+)/add_progresspic$', views.add_progresspic, name='add_progresspic'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
