import random
from typing import Callable, Optional
import faker

class FakeInput:
    def __init__(
        self,
        type: str,
        post_process_func: Optional[Callable] = None,
    ) -> None:
        self.input_type = type
        self.post_process_func = post_process_func
        self._faker = faker.Faker()

    def get_value(self):
        val = getattr(self._faker, self.input_type)()
        if self.post_process_func:
            val = self.post_process_func(val)
        return val


class FakeChoiceInput(FakeInput):
    def __init__(
        self,
        choices,
        type=...,
    ) -> None:
        super().__init__(type)
        self.choices = choices

    def get_value(self):
        return random.choice(self.choices)