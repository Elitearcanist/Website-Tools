from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from main import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  path('polls/', include('polls.urls')),
]
