"""
Tests for the Django admin modifications.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Tests for Django admin."""
    def setUp(self):
        """Create user and client."""
        self.client = Client()
        email = 'admin@example.com'
        major = "test"
        birthday = '2000-10-18'
        password = "test123"
        self.admin_user = get_user_model().objects.create_superuser(email, password=password, major=major, birthday=birthday)
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User',
            major = major,
            birthday = birthday
        )

    def test_users_lists(self):
        """Test that users are listed on page."""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res ,self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test the edit user page working"""
        url = reverse('admin:core_user_change' , args=[self.user.id])
        res = self.client.get(url)
        self.assertEquals(res.status_code , 200)

    def test_create_user_page(self):
        """Test the create user page works."""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

