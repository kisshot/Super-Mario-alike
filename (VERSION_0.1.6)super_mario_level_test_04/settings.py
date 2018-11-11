BLACK = ( 0,  0,  0 )
RED = (255,   0,   0)
SIZE_MULTIPLIER = 2.5


# MARIO
STAND = 'standing'
WALK_RIGHT = 'walk_right'
WALK_LEFT = 'walk_left'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
END_OF_LEVEL_FALL = 'end_of_level_fall'
WALKING_TO_CASTLE = 'walking_to_castle'

# ENEMY
LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'

SHELL_SLIDE = 'shell slide'


class Settings():
    '''
    存储超级马里奥兄弟level01的所有设置
    An attempt to recreate the first level of Super Mario Bros.
    The first level of Super Mario Bros made with Python and Pygame.
    '''
    def __init__(self):
        '''初始化游戏的设置'''
        self.screen_width = 400
        self.screen_height = 224
        self.bg_color = (230, 230, 230)
        # Mario的位置
        self.mario_speed_factor = 1

        self.mario_limit = 3








