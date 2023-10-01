=====
dj-fakemin
=====

dj-fakemin is a minimal fake data seeder for django which probably does need the most straightforward configuration.

Detailed documentation is on the way.

Quick start
-----------
1. Installation:
    a. using git::

        pip install git+https://github.com/yeamin21/django_fakemin.git
     or
    b. local installation::

        1. download the latest version from the releases [django-fakemin-0.1.tar.gz]
        2. pip install --user [DOWNLOAD LOCATION]/django-fakemin-0.1.tar.gz

2. Add "fakemin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "fakemin",
    ]
3. Create ``factory.py`` or other .py file in any app and create a subclass of FakeminFactory::

    ### users/factory.py
    from fakemin.factory import FakeMinFactory
    from fakemin.inputs import FakeChoiceInput, FakeInput
    from django.contrib.auth.hashers import make_password
    from users.models import User, Room
    class UserFactory(FakeMinFactory):
        username = FakeInput('user_name',) # faker data type user_name.
        password = FakeInput('password', post_process_func=make_password) # After generating a password, a post-process function is applied to encrypt that
        class Meta:
            model = User # django model to create data against
            count = 10 # no of rows you want
    class RoomFactory(FakeMinFactory):
        user = FakeChoiceInput(choices=User.objects.all()) # for foreign relationship- pass the objects of the related model
        capacity = FakeInput('pyint') # faker-python data type. i.e: pystr, pyint, etc. 
        class Meta:
            model = Room
            count = 10

4. Include the fakemin factory list in the projects ``settings.FAKEMIN_CONFIG`` in order::

    ## your_project/settings.py
    FAKEMIN_CONFIG = {
        'factories':[
            'user.factory.UserFactory',
            'user.factory.RoomFactory'
        ]
    }

5. Run ``python manage.py fakemin`` to create fake data.
