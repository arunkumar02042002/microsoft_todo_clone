from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()

class UsersManagersTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
        username="user1",
        email="user1@example.com",
        password="pass1234",
        )
        self.assertEqual(user.username, "user1")
        self.assertEqual(user.email, "user1@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
        username="superuser",
        email="superuser@example.com",
        password="pass1234",
        )
        self.assertEqual(admin_user.username, "superuser")
        self.assertEqual(admin_user.email, "superuser@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)