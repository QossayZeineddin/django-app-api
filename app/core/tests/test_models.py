"""
testing the models in the project
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal
from .. import models


class ModelTests(TestCase):
    def test_create_user_with_email_successfully(self):
        email = "testing@example.com"
        password = "test123"
        major = "tests"
        birthday = '2000-10-18'

        try:
            user = get_user_model().objects.create_user(
                email=email,
                password=password,
                major=major,
                birthday=birthday,
            )
            self.assertEquals(user.email, email)
            self.assertTrue(user.check_password(password))

        except Exception as e:
            self.fail(f'Error in creating the user: {str(e)}')

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        major = "tests"
        birthday = '2000-10-18'
        password = "test123"
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, password=password, major=major, birthday=birthday)
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        major = "tests"
        birthday = '2000-10-18'
        password = "test123"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', password=password, major=major, birthday=birthday, )

    def test_create_superuser(self):
        """Test creating a superuser."""
        email = "testing@example.com"
        major = "tests"
        birthday = '2000-10-18'
        password = "test123"
        user = get_user_model().objects.create_superuser(email, password=password, major=major, birthday=birthday)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """TEst create a recipe obj secss"""
        email = "testing@example.com"
        major = "tests"
        birthday = '2000-10-18'
        password = "test123"
        user = get_user_model().objects.create_superuser(email, password=password, major=major, birthday=birthday)
        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description.',
        )

        self.assertEqual(str(recipe), recipe.title)
