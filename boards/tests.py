from django.test import TestCase
from django.core.urlresolvers import reverse
from .views import home
# Create your tests here.



class HomeTests(TestCase):

    def test_home_view_status_code(self):

        url = reverse('boards:home')

        response = self.client.get(url)

        self.assertEqual(response.status_code,200)

    def test_home_url_resolves_home_view(self):

        view = reverse('boards:/')

        self.assertEqual(view.func,home)