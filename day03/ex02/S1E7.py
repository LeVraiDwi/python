from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, name: str, health_state: bool = True) -> None:
        super().__init__(name, health_state)
        self.family_name: str = "Baratheon"
        self.eyes: str = "brown"
        self.hairs: str = "dark"

    def __str__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """change is_alive to false"""
        return super().die()


class Lannister(Character):
    def __init__(self, name: str, health_state: bool = True) -> None:
        super().__init__(name, health_state)
        self.family_name: str = "Lanister"
        self.eyes: str = "blue"
        self.hairs: str = "light"

    def __str__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """change is_alive to false"""
        return super().die()

    @staticmethod
    def create_lannister(Name: str, is_alive: bool = True):
        return Lannister(Name, is_alive)
