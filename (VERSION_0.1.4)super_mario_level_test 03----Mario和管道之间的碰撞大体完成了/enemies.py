import pygame
from pygame.sprite import Sprite
import settings as st

class Enemy(Sprite):
    """所有敌人的基本类（包含乌龟、蘑菇等等）"""

    def __init__(self, ai_settings, screen):
        '''初始化敌人并设置其起始位置'''
        Sprite.__init__(self)
        self.screen = screen
        self.ai_settings = ai_settings
        self.enemies_sheet = pygame.image.load('resources/images/enemies.png')
        self.screen_rect = screen.get_rect()

        #加载敌人图像，并设置其rect属性
        self.image = self.get_image(0, 4, 16, 32)
        self.rect = self.image.get_rect()

        self.rect.x = 500
        self.rect.y = self.screen_rect.bottom - 50

        # 在enemy的属性x中存储小数值
        self.x = float(self.rect.x)

    '''下一个函数没什么用：移到了game_functions'''

    def handle_state(self, mario, enemies):
        #spritecollideany
        if pygame.sprite.spritecollide(mario, enemies, False):
            enemies.empty()
            print('THEY ARE TOGETHER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    def get_image(self, x, y, width, height):
        """Get the image frames from the sprite sheet"""
        image = pygame.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.enemies_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(st.BLACK)

        # image = pygame.transform.scale(image,
        #                            (int(rect.width * st.SIZE_MULTIPLIER),
        #                             int(rect.height * st.SIZE_MULTIPLIER)))
        return image


    def update(self):
        '''目前就算地图动，敌人也会按照固定的速读往前移动，两者呈现相对静止状态'''
        """根据移动标志调整Enemy的位置"""

        self.rect.x -= 1
        print('ENEMY: ', self.rect.x)

        # return self.rect.centerx


    def blitme(self, centerx):
        """
        在指定位置绘制敌人，按照世界地图的绘制位置重新绘制enemy的x坐标，从而实现两者
        的相对静止，mario不移动（但记录其center坐标），世界地图依照这一坐标移动（看起来就
        像是Mario在移动），enemy与世界地图相对静止，同时按照固定速度往左移动
        """
        self.screen.blit(self.image, (self.rect.x - centerx + 50, self.rect.y))
        if self.rect.x > (centerx - 5) and self.rect.x < (centerx + 5):
            print('FUCK YOU!!!')



