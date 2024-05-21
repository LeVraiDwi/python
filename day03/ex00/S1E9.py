from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    first_name: str
    is_alive: bool = True

    def __init__(self, name: str, health_state: bool = True) -> None:
        """Your docstring for Constructor"""
        self.first_name = name
        self.is_alive = health_state
        super().__init__()

    @abstractmethod
    def die(self):
        self.is_alive = False


class Stark(Character):
    """Your docstring for Class"""
    def die(self):
        """Your docstring for Method"""
        return super().die()
