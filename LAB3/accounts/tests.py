from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import *


class LoginPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('login')
        self.response = self.client.get(url)

    def test_login_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_login_template(self):
        self.assertTemplateUsed(self.response, 'login.html')

    def test_login_contains_correct_html(self):
        self.assertContains(self.response, 'login')

    def test_login_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')


class RegisterPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('register')
        self.response = self.client.get(url)

    def test_register_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_register_template(self):
        self.assertTemplateUsed(self.response, 'register.html')

    def test_register_contains_correct_html(self):
        self.assertContains(self.response, 'register')

    def test_registerpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')


class UserPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('user-page')
        self.response = self.client.get(url)

    def test_user_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_user_template(self):
        self.assertTemplateUsed(self.response, 'register.html')

    def test_user_contains_correct_html(self):
        self.assertContains(self.response, 'user-page')

    def test_userpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')


class AccountSettingsPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('account')
        self.response = self.client.get(url)

    def test_account_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_account_template(self):
        self.assertTemplateUsed(self.response, 'account-settings.html')

    def test_account_contains_correct_html(self):
        self.assertContains(self.response, 'account')

    def test_account_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')
