from django.test import TestCase

# Create your tests here.
from django.urls import reverse, resolve

from .models import Teams
from .views import display_teams, team_page


class TeamTests(TestCase):

    def setUp(self):
        Teams.objects.create(team_number=2073)

    # Teams Display
    def test_teams_view_success_status_code(self):
        url = reverse('teams')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_teams_url_resolves_teams_view(self):
        view = resolve('/teams/')
        self.assertEquals(view.func, display_teams)

    # Teams Page
    def test_team_page_view_success_status_code(self):
        url = reverse('team_page', kwargs={'team_number': 2073})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_team_page_view_not_found_status_code(self):
        url = reverse('team_page', kwargs={'team_number': 0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_team_page_url_resolves_teams_page_view(self):
        view = resolve('/teams/2073')
        self.assertEquals(view.func, team_page)
