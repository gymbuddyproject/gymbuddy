from django.conf.urls import url
from django.contrib import admin
from gymbuddy import views

app_name = "gymbuddy"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^test/', views.test, name='test'),
    url(r'^admin/', admin.site.urls),

]
