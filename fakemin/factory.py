import time
from django.db import models
import faker
from fakemin.inputs import FakeInput

class FakeMinFactory:
    class Meta:
        count: int
        model: models.Model
        chunk_size: int = 1000

    def __init__(self) -> None:
        self._meta = self.Meta()
        self._model = self._meta.model
        self._model_fields = self._meta.model._meta.get_fields()
        self._declared_fields = self.get_declared_fields()
        self._factory = faker.Factory().create()
        self._chunk_size = self._meta.chunk_size if hasattr(self._meta,'chunk_size') else 500
    def create(self):
        start = time.perf_counter()
        for items in self.generate_items():
            self._model.objects.bulk_create(items, ignore_conflicts=True)
        end = time.perf_counter()
        print('fakemin factory took {} seconds'.format(end-start))
    def get_declared_fields(self):
        return {
            attr: getattr(self, attr)
            for attr in dir(self)
            if isinstance(getattr(self, attr), FakeInput)
        }

    def generate_items(self):
        self.get_must_provide_fields()
        chunk_size = self._chunk_size
        for i in range(0, self._meta.count,chunk_size):
            yield [
                self._model(**self.generate_faker_values(), 
                        **self.generate_declared_values()
                    )
                for _ in range(i, i + chunk_size)
            ]

    def generate_declared_values(self):
        vals = dict()
        for k, v in self._declared_fields.items():
            vals[k] = v.get_value()
        return vals

    def generate_faker_values(self):
        vals = {}
        for field in self._model_fields:
            if field.name not in self._declared_fields.keys() and hasattr(
                self._factory, field.name
            ):
                vals[field.name] = getattr(self._factory, field.name)()
        return vals

    def get_must_provide_fields(self):
        must_provide_fields = []
        for field in self._model_fields:
            if isinstance(field, models.ManyToManyRel):
                ...  # maybe one day
            elif isinstance(field, models.ManyToOneRel):
                ...  # maybe one day
            elif isinstance(field, models.ManyToManyField):
                ...  # maybe one day
            elif (
                field.name not in self._declared_fields.keys()
                and not field.null
                and not field.auto_created
                and not field.has_default()
                and not hasattr(field, "auto_now")
                and not hasattr(self._factory, field.name)
            ):
                must_provide_fields.append(field.name)
        if must_provide_fields:
            raise Exception("Must provide fields: " + ", ".join(must_provide_fields))