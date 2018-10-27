import sys

import pygame
from mario import Mario
import settings as st

def check_keydown_events(event, ai_settings, screen, mario):
    """响应按键"""


    if event.key == pygame.K_RIGHT:
        # 向右移动Mario
        mario.moving_right = True

    elif event.key == pygame.K_LEFT:
        # 向左移动Mario
        mario.moving_left = True
    elif event.key == pygame.K_w:
        # 马里奥跳跃
        mario.moving_up = True


def check_keyup_events(event, mario):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        mario.moving_right = False
    elif event.key == pygame.K_LEFT:
        mario.moving_left = False
    if event.key == pygame.K_w:
        mario.moving_up = False
        mario.moving_down = True

def check_events(ai_settings, screen, mario):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, mario)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mario)

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                mario.facing_right = True


def update_screen(ai_settings, screen, mario, enemy, centerx):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 背景图片
    background_image_filename = 'resources/images/level_1.png'
    # 每次循环时都重绘屏幕
    background = pygame.image.load(background_image_filename).convert()


    # 将背景图画上去

    screen.blit(background, (-centerx, 0))

    # screen.fill(ai_settings.bg_color)

    enemy.blitme(centerx)
    mario.blitme()



    # 让最近绘制的屏幕可见
    pygame.display.update()



