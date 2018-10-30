import pygame
from settings import Settings
from mario import Mario
from mario_shadow import Mario_shadow
import game_functions as gf
from enemies import Enemy
from pygame.sprite import Group



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
    # 背景图片
    # background = pygame.image.load(background_image_filename).convert()

    # 放置Mario
    mario = Mario(ai_settings, screen)
    # mario_shadow = Mario_shadow(ai_settings, screen)

    # 敌人
    enemy = Enemy(ai_settings, screen)
    enemies = Group()
    enemies.add(enemy)



    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, mario)


        # 将背景图画上去
        # screen.blit(background, (0, 577))

        centerx = mario.update()
        # mario_shadow.update()
        # print(centerx)

        enemy.update()
        enemy.handle_state(mario,enemies)
        gf.update_screen(ai_settings, screen, mario, enemy, centerx)

run_game()

