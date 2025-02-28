from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomerUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='giorgi',
            email='',
            password='giorgi12345'
        )
        self.assertEqual(user.username, 'giorgi')
        self.assertEqual(user.email, '')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='vasiko',
            email='',
            password='vasiko12345'
        )
        self.assertEqual(admin_user.username, 'vasiko')
        self.assertEqual(admin_user.email, '')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
    