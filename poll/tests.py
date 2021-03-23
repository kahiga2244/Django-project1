from django.test import TestCase
from .models import Poll,User


from django.test import Client
csrf_client = Client(enforce_csrf_checks=True)
# Create your tests here.

class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.us1= User(user_id = '23232323', email ='james@moringaschool.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.us1,User))
        # Testing Save Method
    def test_save_method(self):
        self.us1.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)
        #Testing the delete method
    def test_delete_user(self):
        # self.us1.save_user()
        self.us1.delete_user()
        users = User.objects.all()
        self.assertTrue(len(users) == 0)
    