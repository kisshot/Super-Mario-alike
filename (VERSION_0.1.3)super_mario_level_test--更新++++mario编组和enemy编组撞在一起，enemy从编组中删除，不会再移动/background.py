'''还是没有什么用'''


import pygame
from settings import Settings
import settings as st

class Background():

    def __init__(self, ai_settings, screen):
        """初始化Mario并设置其初始值"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        """Extracts image from sprite sheet"""
        # 加载Mario图像并获取其外接矩阵
        self.background_image_filename = 'resources/images/level_1.png'
        self.background = pygame.image.load(self.background_image_filename).convert()

        # 获取正常状态的马里奥
        self.rect = self.background.get_rect()

        # 将Mario放在屏幕底部中央
        self.rect.x = 0 #self.screen_rect.centerx - 160
        self.rect.y = 0

    # def update(self, center):
    #     """根据移动标志调整Mario的位置"""
    #
    #     self.rect.centerx -= center

    def blitme(self, center):
        """在指定位置绘制背景图"""
        self.screen.blit(self.background, (-center, 0))
        print('Background: ', center)





