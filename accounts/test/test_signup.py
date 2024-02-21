from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

from accounts.forms import UserRegistrationForm


class AccountCreation(TestCase):
    def test_signup_page_exist(self):
        response = self.client.get(reverse('signup_page'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed('accounts/register.html')
        self.assertContains(response, "Create Your account today")