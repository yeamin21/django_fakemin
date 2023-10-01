=====
dj-fakemin
=====

dj-fakemin is a minimal fake data seeder for django which probably does need the simplest configuration.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "fakemin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "fakemin",
    ]
2. Create factory.py or other .py file in any app and import the .
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
2. Include the fakemin factory list in the settings.FAKEMIN_CONFIG in order::
    FAKEMIN_CONFIG = {
        'factories':[
            'user.factory.UserFactory',
            'user.factory.RoomFactory'
        ]
    }

3. Run ``python manage.py fakemin`` to create fake data.
