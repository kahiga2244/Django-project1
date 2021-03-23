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
        self.us1.save_user()
        self.us1.delete_user()
        users = User.objects.all()
        self.assertTrue(len(users) == 0)

    # def test_update_user(self):
    #     self.us1.save_user()
    #     self.us1.objects.filter(user_id = '23232323').update(user_id ='24242424')
    #     self.assertTrue(len(users) == 0)
    #     # Entry.objects.all().filter(pub_date__year=2006)

class PollTestClass(TestCase):
      # Set up method
    def setUp(self):
        self.p1= Poll(president = 'william_ruto',political_party='UDA', votes='0',poll_number=0)
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.p1,Poll))
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.p1,Poll))
        # Testing Save Method
    def test_save_method(self):
        self.p1.save_user()
        polls = Poll.objects.all()
        self.assertTrue(len(polls) > 0)
        #Testing the delete method

    def test_delete_user(self):
        self.p1.save_user()
        self.p1.delete_user()
        polls = Poll.objects.all()
        self.assertTrue(len(polls) == 0)


