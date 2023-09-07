import config

def position(row, col):
    return (col * config.TILE_SIZE[1], row * config.TILE_SIZE[0])

def center_position(row, col):
    return (position(row, col)[1] + config.TILE_SIZE[1]/2, position(row, col)[0] + config.TILE_SIZE[0]/2)

def tile_row_col(pos_x, pos_y):
    return (pos_y // config.TILE_SIZE[1], pos_x // config.TILE_SIZE[0])

def position_str(row, col):
    return 'abcdefgh'[col] + str(8-row)

def position_str_to_rowcol(position_str):
    return (8 - int(position_str[1]), ord(position_str[0]) - ord('a'))