import random
from game.logic.base import BaseLogic
from game.models import Board, GameObject, Position 

class MyBot(BaseLogic):
    def __init__(self):
        self.my_attribute = 0 
        self.DEFAULT_MAX_DIAMONDS_HELD = 5

    def find_closest_diamond(self, bot_position: Position, diamonds: list[GameObject], board: Board) -> Position | None:
        closest_diamond_pos = None
        min_distance = float('inf')

        for diamond in diamonds:
            distance = abs(bot_position.x - diamond.position.x) + \
                       abs(bot_position.y - diamond.position.y)
            
            if distance < min_distance:
                min_distance = distance
                closest_diamond_pos = diamond.position
        
        return closest_diamond_pos

    def get_valid_moves(self, bot_position: Position, board_width: int, board_height: int) -> list[tuple[int, int]]:
        possible_deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        valid_moves = []
        for dx, dy in possible_deltas:
            next_x, next_y = bot_position.x + dx, bot_position.y + dy
            if 0 <= next_x < board_width and 0 <= next_y < board_height:
                valid_moves.append((dx, dy))
        return valid_moves

    def _move_towards(self, current_pos: Position, target_pos: Position) -> tuple[int, int]:
        delta_x, delta_y = 0, 0
        if target_pos.x > current_pos.x:
            delta_x = 1
        elif target_pos.x < current_pos.x:
            delta_x = -1
        
        if delta_x == 0:
            if target_pos.y > current_pos.y:
                delta_y = 1
            elif target_pos.y < current_pos.y:
                delta_y = -1
        return delta_x, delta_y

    def next_move(self, board_bot: GameObject, board: Board):
        current_pos = board_bot.position
        delta_x, delta_y = 0, 0

        board_width = board.width 
        board_height = board.height 
        
        current_diamonds_held = 0
        if hasattr(board_bot.properties, "diamonds"):
            current_diamonds_held = board_bot.properties.diamonds
        
        inventory_size = self.DEFAULT_MAX_DIAMONDS_HELD
        if hasattr(board_bot.properties, "inventory_size"):
            inventory_size = board_bot.properties.inventory_size
        
        base_pos_data = None
        if hasattr(board_bot.properties, "base"):
            base_pos_data = board_bot.properties.base
            
        base_position: Position | None = None
        if isinstance(base_pos_data, Position):
            base_position = base_pos_data
        elif isinstance(base_pos_data, dict) and "x" in base_pos_data and "y" in base_pos_data:
            base_position = Position(base_pos_data["x"], base_pos_data["y"])
        elif isinstance(base_pos_data, (list, tuple)) and len(base_pos_data) == 2:
            base_position = Position(base_pos_data[0], base_pos_data[1])

        target_pos: Position | None = None

        if base_position and current_diamonds_held >= inventory_size:
            target_pos = base_position
        else:
            all_game_objects = board.game_objects
            
            red_diamonds = [obj for obj in all_game_objects if obj.type == "RedDiamondGameObject"]
            blue_diamonds = [obj for obj in all_game_objects if obj.type == "DiamondGameObject"]

            closest_red_pos = self.find_closest_diamond(current_pos, red_diamonds, board)
            closest_blue_pos = self.find_closest_diamond(current_pos, blue_diamonds, board)

            if closest_red_pos:
                dist_red = abs(current_pos.x - closest_red_pos.x) + abs(current_pos.y - closest_red_pos.y)
                if closest_blue_pos:
                    dist_blue = abs(current_pos.x - closest_blue_pos.x) + abs(current_pos.y - closest_blue_pos.y)
                    if dist_red <= dist_blue: 
                        target_pos = closest_red_pos
                    else:
                        target_pos = closest_blue_pos
                else: 
                    target_pos = closest_red_pos
            elif closest_blue_pos: 
                target_pos = closest_blue_pos
        
        if target_pos:
            delta_x, delta_y = self._move_towards(current_pos, target_pos)

        next_check_x, next_check_y = current_pos.x + delta_x, current_pos.y + delta_y
        if not (0 <= next_check_x < board_width and 0 <= next_check_y < board_height):
            delta_x = 0 
            delta_y = 0
            
        if delta_x == 0 and delta_y == 0:
            valid_moves = self.get_valid_moves(current_pos, board_width, board_height)
            if valid_moves:
                delta_x, delta_y = random.choice(valid_moves)

        return delta_x, delta_y