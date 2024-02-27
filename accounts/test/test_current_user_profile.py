from django.urls import reverse
from django.test import TestCase
from http import HTTPStatus


class ProfileTest(TestCase):
    def setUp(self) -> None:
        self.url = reverse('current_user_profile')
        self.template_name = 'accounts/current_user_profile.html'

    def test_current_user_profile_exist(self):
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, self.template_name)
