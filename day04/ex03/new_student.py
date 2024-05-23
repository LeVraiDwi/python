import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

def check(func) -> object:

    def wrap(*args: any, **kwargs: any) -> object:
        """Wrapper!! he wrapp like swoop dog"""
        for _, value in kwargs.items():
            if not isinstance(value, str):
                print(f"invalid input: {value}")
                return None
            return func(*args, **kwargs)
    return wrap

@check
@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login = self.name[0] + self.surname.lower()
        self.login = self.login[:8]