import pygame
from settings import Settings
from mario import Mario
import game_functions as gf



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





    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, mario)


        # 将背景图画上去
        # screen.blit(background, (0, 577))

        centerx = mario.update()

        gf.update_screen(ai_settings, screen, mario, centerx)








run_game()

