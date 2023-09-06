"""judgeme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from . import spotify_views
from . import spotipy_test
# from . import audio_player

urlpatterns = [
    re_path(r'^generateOptions$', views.generateOptions, name='generateOptions'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('judge/', views.judge, name='judge'),
    path('callback/', views.spotify_callback, name='callback'),
    path('login/', views.login_user, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('spotify/sign-in/', views.sign_in, name='sign-in'),
    path('judge/', views.judge, name='judge'),
    path('judge/result/', views.result, name='result'),
    path('judge/music_tastes', views.music_tastes, name='music_tastes'),
    path('profile/', views.profile, name='profile'),
    path('playlist/', views.playlist, name='playlist'),
    path('judge/bar/', views.bar, name='bar'),
    path('judge/graph/', views.graph, name='graph'),
    path('artist/', views.artist, name='artist'),
    path('homepage/', views.homepage, name='homepage'),
    path('profiledit/', views.profiledit, name='profiledit'),
    path('temp', views.temp, name='temp'),
    path('breakdown/', views.breakdown, name='breakdown'),
    path('test/', views.test, name='test'),
    path('generate/', views.generate, name='generate'),
    path('playlistgenerate/', views.playlistgenerate, name='playlistgenerate'),
    path('base/', views.base, name='base'),
    path('friends/', views.friends, name='friends'),
    path('spotify-test/', spotipy_test.test, name='test'),
    path('goodorbadplaylist/', views.gorb, name='gorb'),
    path('experiment/', views.experiment, name='experiment'),

    path('success/', views.success, name="success"),
    path("__reload__/", include("django_browser_reload.urls")),

    #Added Static part for the urls because this will suppposedly help us reference the url of the uploaded image
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




#added the stattic 