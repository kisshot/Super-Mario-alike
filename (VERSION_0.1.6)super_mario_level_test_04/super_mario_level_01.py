import pygame
from pygame.sprite import Group

import game_functions as gf
import settings as st
from data import ground_step
from enemy import Enemy
import enemy
from mario import Mario
from settings import Settings
from state.game_stats import GameStats

def setup_ground():
    """Creates collideable, invisible rectangles over top of the ground for
    sprites to walk on"""

    ground_rect1 = ground_step.Ground(0, 200, 1048, 24)
    ground_rect2 = ground_step.Ground(1088, 200, 239, 24)
    ground_rect3 = ground_step.Ground(1374, 200, 1022, 24)
    ground_rect4 = ground_step.Ground(2431, 200, 910, 24)
    ground_group = pygame.sprite.Group(ground_rect1,
                                        ground_rect2,
                                        ground_rect3,
                                        ground_rect4)
    return ground_group

def setup_pipes():
    """Create collideable rects for all the pipes"""

    pipe1 = ground_step.Ground(395, 170, 35, 60)
    pipe2 = ground_step.Ground(560, 155, 35, 60)
    pipe3 = ground_step.Ground(688, 140, 30, 90)
    pipe4 = ground_step.Ground(863, 140, 30, 90)
    pipe5 = ground_step.Ground(2558, 170, 30, 30)
    pipe6 = ground_step.Ground(2816, 170, 30, 30)

    pipe_group = pygame.sprite.Group(pipe1, pipe2,
                                        pipe3, pipe4,
                                        pipe5, pipe6)
    return pipe_group

def setup_steps():
    """Create collideable rects for all the steps"""
    step1 = ground_step.Ground(2097, 183, 16, 16)   # 16
    step2 = ground_step.Ground(2110, 167, 16, 32)
    step3 = ground_step.Ground(2126, 151, 16, 48)
    step4 = ground_step.Ground(2142, 135, 16, 64)

    step5 = ground_step.Ground(6001, 366, 40, 176)
    step6 = ground_step.Ground(6044, 408, 40, 40)
    step7 = ground_step.Ground(6087, 452, 40, 40)
    step8 = ground_step.Ground(6130, 495, 40, 40)

    step9 = ground_step.Ground(6345, 495, 40, 40)
    step10 = ground_step.Ground(6388, 452, 40, 40)
    step11 = ground_step.Ground(6431, 409, 40, 40)
    step12 = ground_step.Ground(6474, 366, 40, 40)
    step13 = ground_step.Ground(6517, 366, 40, 176)

    step14 = ground_step.Ground(6644, 366, 40, 176)
    step15 = ground_step.Ground(6687, 408, 40, 40)
    step16 = ground_step.Ground(6728, 452, 40, 40)
    step17 = ground_step.Ground(6771, 495, 40, 40)

    step18 = ground_step.Ground(7760, 495, 40, 40)
    step19 = ground_step.Ground(7803, 452, 40, 40)
    step20 = ground_step.Ground(7845, 409, 40, 40)
    step21 = ground_step.Ground(7888, 366, 40, 40)
    step22 = ground_step.Ground(7931, 323, 40, 40)
    step23 = ground_step.Ground(7974, 280, 40, 40)
    step24 = ground_step.Ground(8017, 237, 40, 40)
    step25 = ground_step.Ground(8060, 194, 40, 40)
    step26 = ground_step.Ground(8103, 194, 40, 360)

    step27 = ground_step.Ground(8488, 495, 40, 40)

    step_group = pygame.sprite.Group(step1, step2,
                                        step3, step4,
                                        step5, step6,
                                        step7, step8,
                                        step9, step10,
                                        step11, step12,
                                        step13, step14,
                                        step15, step16,
                                        step17, step18,
                                        step19, step20,
                                        step21, step22,
                                        step23, step24,
                                        step25, step26,
                                        step27)
    return step_group

def setup_enemies():
    """创建敌人的群组"""

    pass


def check_mario_x_collisions(mario, ground_step_pipe_group):
    """Check for collisions after Mario is moved on the x axis"""
    collider = pygame.sprite.spritecollideany(mario,
                                            ground_step_pipe_group)
    if collider:
        adjust_mario_for_x_collisions(mario, collider)

def adjust_mario_for_x_collisions(mario, collider):
    """Puts Mario flush next to the collider after moving on the x axis"""
    if mario.rect.x < collider.rect.x and mario.rect.top > collider.rect.top:
        mario.rect.right = collider.rect.left
    elif mario.rect.x > collider.rect.x and mario.rect.top > collider.rect.top:
        mario.rect.left = collider.rect.right

def check_mario_y_collisions(mario, ground_step_pipe_group):
    """Checks for collisions when Mario moves along the y-axis"""
    ground_step_or_pipe = pygame.sprite.spritecollideany(mario, ground_step_pipe_group)
    if ground_step_or_pipe:
        adjust_mario_for_y_ground_pipe_collisions(mario, ground_step_or_pipe)
    test_if_mario_is_falling(mario, ground_step_pipe_group)

def adjust_mario_for_y_ground_pipe_collisions(mario, collider):
    """Mario collisions with pipes on the y-axis"""
    if mario.rect.bottom < collider.rect.bottom:
        # mario.y_vel = 0
        mario.rect.bottom = collider.rect.top
        if mario.state == st.END_OF_LEVEL_FALL:
            mario.state = st.WALKING_TO_CASTLE
        else:
            mario.state = st.WALK
    elif mario.rect.top > collider.rect.top:
        # mario.y_vel = 7
        mario.rect.top = collider.rect.bottom
        mario.state = st.FALL

def test_if_mario_is_falling(mario, ground_step_pipe_group):
    """Changes Mario to a FALL state if more than a pixel above a pipe,
    ground, step or box"""

    if pygame.sprite.spritecollideany(mario, ground_step_pipe_group) is None:
        mario.state = st.FALL

    # if mario.state == st.FALL:
    #     mario.rect.y += 1
    # else:
    #     pass

    # test_collide_group = pygame.sprite.Group(ground_step_pipe_group)

    # mario.rect.y -= 1


def adjust_enemy_position(enemies, pipe_group):
    """Moves all enemies along the x, y axes and check for collisions"""
    for enemy in enemies:

        check_enemy_x_collisions(enemy, pipe_group)


        # # check_enemy_y_collisions(enemy)
        # delete_if_off_screen(enemy)

def check_enemy_x_collisions(enemy, pipe_group):
    """Enemy collisions along the x axis.  Removes enemy from enemy group
    in order to check against all other enemies then adds it back."""
    # enemy.kill()

    collider = pygame.sprite.spritecollideany(enemy,
                                              pipe_group)
    # enemy_collider = pygame.sprite.spritecollideany(enemy, self.enemy_group)

    if collider:
        if enemy.direction == st.LEFT:
            enemy.rect.left = collider.rect.right
            enemy.direction = st.RIGHT
            enemy.x_vel = -1
        elif enemy.direction == st.RIGHT:
            enemy.rect.right = collider.rect.left
            enemy.direction = st.LEFT
            enemy.x_vel = 1

def test_if_enemy_is_falling(enemies, ground_group):
    for enemy in enemies:
        if pygame.sprite.spritecollideany(enemy, ground_group) is None:
            enemy.state = st.FALL
            enemy.y_vel = 5

def check_enemy_y_collisions(self, enemy):
    """Enemy collisions on the y axis"""
    collider = pygame.sprite.spritecollideany(enemy,
                                              self.ground_step_pipe_group)

    if collider:
        if enemy.rect.bottom > collider.rect.bottom:
            enemy.y_vel = 7
            enemy.rect.top = collider.rect.bottom
            enemy.state = st.FALL
        elif enemy.rect.bottom < collider.rect.bottom:

            enemy.y_vel = 0
            enemy.rect.bottom = collider.rect.top
            enemy.state = st.WALK

    else:
        enemy.rect.y += 1
        test_group = pygame.sprite.Group(self.ground_step_pipe_group)
        if pygame.sprite.spritecollideany(enemy, test_group) is None:
            if enemy.state != st.JUMP:
                enemy.state = st.FALL

        enemy.rect.y -= 1

def delete_if_off_screen(self, enemy):
    """Removes enemy from sprite groups if 500 pixels left off the screen,
        underneath the bottom of the screen, or right of the screen if shell"""
    if enemy.rect.x < (self.viewport.x - 300):
        enemy.kill()

    elif enemy.rect.y > (self.viewport.bottom):
        enemy.kill()

    elif enemy.state == st.SHELL_SLIDE:
        if enemy.rect.x > (self.viewport.right + 500):
            enemy.kill()


def run_game():
    '''
    运行游戏主程序
    :return:
    '''
    # background_image_filename = 'resources/images/level_1.png' #'/Users/lufan/Python_CODE_03/super_mario_level_01/resources/images/level_1.png'
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 创建一个窗口
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # 设置窗口标题
    pygame.display.set_caption('Super Mario Bros')
    # 初始化声音模块
    pygame.mixer.init()
    # 加载音乐
    pygame.mixer.music.load(r"resources/music/death.wav")
    # pygame.mixer.music.play()

    # 创建一个用于存储游戏信息的实例
    stats = GameStats(ai_settings)

    # 放置Mario
    mario = Mario(ai_settings, screen)
    marios = Group()
    # 敌人
    enemy1 = Enemy(x=500, screen=screen, direction=st.LEFT)
    enemy2 = Enemy(x=600, screen=screen, direction=st.LEFT)
    enemy3 = Enemy(x=1100, screen=screen, direction=st.LEFT) #1100

    enemies = Group()
    enemies.add(enemy1)
    enemies.add(enemy2)
    enemies.add(enemy3)

    marios.add(mario)

    '''地面元素'''
    ground_group = setup_ground()
    pipe_group = setup_pipes()
    step_group = setup_steps()
    ground_step_pipe_group = pygame.sprite.Group(ground_group,
                                                 pipe_group,
                                                 step_group)

    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, mario)

        if stats.game_active:
            centerx = mario.update()
            # print(centerx)

            enemies.update()

            '''在这里加入update函数，检测碰撞情况，并将handle_state(marios,enemies)也并入到update函数中'''
            gf.handle_state(stats, marios,enemies)

            check_mario_x_collisions(mario, ground_step_pipe_group)
            check_mario_y_collisions(mario, ground_step_pipe_group)

            adjust_enemy_position(enemies, pipe_group)
            test_if_enemy_is_falling(enemies, ground_group)

            # check_enemy_x_collisions(enemy1, pipe_group)

            # if mario.rect.y > 180 and (1048 < mario.rect.x < 1080) or (1319 < mario.rect.x < 1372) \
            #         or (2396 < mario.rect.x < 2431) :
            #     mario.state = st.FALL
                # # mario.rect.y += 1
            gf.update_screen(ai_settings, screen, mario, enemies ,centerx)

        elif stats.game_active == False:
            gf.update_menu(screen, mario)

run_game()



