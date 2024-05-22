from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """la classe du roi"""
    def __init__(self, name: str, health_state: bool = True) -> None:
        """init king"""
        super().__init__(name, health_state)

    def get_eyes(self):
        """get eyes color"""
        return self.eyes

    def set_eyes(self, eyes):
        """set eyes color"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """set hairs color"""
        self.hairs = hairs

    def get_hairs(self):
        """get hairs color"""
        return self.hairs
