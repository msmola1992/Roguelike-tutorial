from typing import Iterable, Any

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

from entity import Entity  
from input_handlers import EventHandler
from game_map import GameMap


class Engine:
    def __init__(self, event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.even_handler = event_handler
        self.game_map = game_map
        self.player = player
        self.update_fov()

    def handle_events(self, events: Iterable[any]) -> None:
        for event in events:
            action = self.even_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)

            self.update_fov() # update FOV before the players next action
    
    def update_fov(self) -> None:
        # Recompute visible area based on players point of view

        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"], 
            (self.player.x, self.player.y),
            radius = 8, 
        )
        # if a tile is visible it should be added to explored
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)


        context.present(console)

        console.clear()
