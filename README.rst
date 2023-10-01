=====
dj-fakemin
=====

dj-fakemin is a minimal fake data seeder for django which probably does need the simplest configuration.

Detailed documentation is in the "docs" directory.

Quick start
-----------
1. download the build package from the github releases or from the project dist folder [django-fakemin-0.1.tar.gz]
2. install using `pip install --user [DOWNLOAD LOCATION]/django-fakemin-0.1.tar.gz`.  
2. Add "fakemin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "fakemin",
    ]
3. Create factory.py or other .py file in any app and import the .
    ### users/factory.py
    from fakemin.factory import FakeMinFactory
    from fakemin.inputs import FakeChoiceInput, FakeInput
    from users.models import User, Room
    class UserFactory(FakeMinFactory):
        username = FakeInput('user_name', post_process_func=make_password)
        class Meta:
            model = User # django model to create data against
            count = 10 # no of rows you want
    class RoomFactory(FakeMinFactory):
        user = FakeChoiceInput(choices=User.objects.all())
        capacity = FakeInput('pyint')
        class Meta:
            model = Room
            count = 10
4. Include the fakemin factory list in the settings.FAKEMIN_CONFIG in order::
    FAKEMIN_CONFIG = {
        'factories':[
            'user.factory.UserFactory',
            'user.factory.RoomFactory'
        ]
    }

5. Run ``python manage.py fakemin`` to create fake data.
