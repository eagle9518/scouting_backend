"""scouting_backend URL Configuration

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
from django.urls import path, include
from teams import views as team_views
from scanner import views as scanner_views
from matches import views as matches_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', team_views.home, name='home'),
    path('teams/', team_views.display_teams, name='teams'),
    path('teams/<int:team_number>', team_views.team_page, name='team_page'),
    path('matches/matches_list', matches_views.matches_list, name='matches_list'),
    path('matches/<slug:quantifier>/<int:match_number>/<int:team_number>', matches_views.match_summaries, name='match_summaries'),
    path('scanner/', scanner_views.scanner, name='scanner'),

]
