from django.contrib.auth.hashers import make_password
'''
from fakemin.factory import FakeMinFactory
from fakemin.inputs import FakeChoiceInput, FakeInput

class UserFactory(FakeMinFactory):
    username = FakeInput('user_name', post_process_func=make_password)
    class Meta:
        model = User
        count = 10

class RoomFactory(FakeMinFactory):
    user = FakeChoiceInput(choices=User.objects.all())
    capacity = FakeInput('pyint')
    class Meta:
        model = Room
        count = 10
        
'''