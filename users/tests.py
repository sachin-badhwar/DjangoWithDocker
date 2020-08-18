from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class CustomUserTest(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user=User.objects.create_user(
            username='sachin',
            password=1234,
            email='sachin@email.com'
        )
        self.assertEqual(user.username,'sachin')
        self.assertEqual(user.email,'sachin@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = get_user_model()    
        adminUser = user.objects.create_superuser(
            username = 'superadmin',
            password = '1234',
            email = 'superadmin@email.com'
        )  
        self.assertEqual(adminUser.username,'superadmin')
        self.assertEqual(adminUser.email,'superadmin@email.com')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)