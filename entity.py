from typing import Tuple

class Entity: 

    #Generic object to represent in game objects
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        #move entity by given amount
        self.x += dx
        self.y += dy