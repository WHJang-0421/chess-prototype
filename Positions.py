import config

class Pair(list):
    def __init__(self, first, second):
        self.append(first)
        self.append(second)

    def __add__(self, other):
        return Pair(self[0] + other[0], self[1] + other[1])
    
    def __div__(self, number):
        return Pair(self[0] / number, self[1] / number)
    
    def __divmod__(self, number):
        return (Pair(self[0]//number, self[1]/number), Pair(self[0]%number, self[1]%number))
    
class PointPosition(Pair):
    pass

class TilePosition:
    # initializers and factory methods
    def __init__(self, row, col):
        self.row = row
        self.col = col

    @staticmethod
    def from_position(x, y):
        return TilePosition(y // config.TILE_SIZE[1], x // config.TILE_SIZE[0])

    @staticmethod
    def from_position(point):
        return TilePosition.from_position(point.x, point.y)
    
    @staticmethod
    def from_string(position_str):
        return TilePosition(8 - int(position_str[1]), ord(position_str[0]) - ord('a'))
    
    @staticmethod
    def from_pair(pair):
        return TilePosition(pair.first, pair.second)

    # utility functions
    def __str__(self):
        return 'abcdefgh'[self.col] + str(8-self.row)
    
    # properties
    @property
    def color(self):
        return 'white' if (self.row + self.col) % 2 == 0 else 'black'

    @property
    def top_left_point(self):
        return PointPosition(self.col * config.TILE_SIZE[1], self.row * config.TILE_SIZE[0])
    
    @property
    def center_point(self):
        return PointPosition(self.top_left_point[1] + config.TILE_SIZE[1]/2, self.top_left_point[0] + config.TILE_SIZE[0]/2)