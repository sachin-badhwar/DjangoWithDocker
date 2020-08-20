from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm # new
from .views import SignupPageView # new
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

class SignupPageTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
        #print('response print ',self.response)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,'signup.html')
        self.assertContains(self.response,'Sign Up')
        self.assertNotContains(self.response,'Hi there! I should not be on the page.')    

    def test_signup_form(self):
        form = self.response.context.get('form')
        print('form print ',form)
        self.assertIsInstance(form,CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self): # new
        """
        checking which view function is being used
        """
        view = resolve('/accounts/signup/')
        print('view print ',view)
        self.assertEqual(
        view.func.__name__,
        SignupPageView.as_view().__name__
        )
        print('name check ',SignupPageView.as_view().__name__)

