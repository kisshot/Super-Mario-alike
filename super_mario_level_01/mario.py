import pygame
from settings import Settings
import settings as st

class Mario():

    def __init__(self, ai_settings, screen):
        """初始化Mario并设置其初始值"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        """Extracts image from sprite sheet"""
        # 加载Mario图像并获取其外接矩阵
        self.sprite_sheet = pygame.image.load('resources/images/mario_bros.png')

        # 获取正常状态的马里奥
        self.load_images_from_sheet()
        self.image = self.small_normal_frames[0][0]
        self.rect = self.image.get_rect()

        # 将Mario放在屏幕底部中央
        self.rect.centerx = 0 #self.screen_rect.centerx - 160
        self.rect.bottom = self.screen_rect.bottom - 24

        # 在Mario的属性center中存储小数值
        self.center = float(self.rect.centerx)


        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.facing_right = False


    def load_images_from_sheet(self):
        self.right_small_normal_frames = []
        self.left_small_normal_frames = []
        self.small_normal_frames = []


        '''面向右侧的马里奥图像'''
        self.right_small_normal_frames.append(
            self.get_mario_image(178, 32, 12, 16))  # Right [0]
        self.right_small_normal_frames.append(
            self.get_mario_image(144, 32, 16, 16))  # Right jump [1]


        '''这里把右侧的马里奥图像翻转'''
        for frame in self.right_small_normal_frames:
            new_image = pygame.transform.flip(frame, True, False)
            self.left_small_normal_frames.append(new_image) # Left [0] | Left jump[1]



        # Right: 0, Left: 1
        self.small_normal_frames = [self.right_small_normal_frames, self.left_small_normal_frames]

    def get_mario_image(self, x, y, width, height):

        image = pygame.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(st.BLACK)
        # image = pygame.transform.scale(image,
        #                            (int(rect.width * st.SIZE_MULTIPLIER),
        #                             int(rect.height * st.SIZE_MULTIPLIER)))
        return image

    def update(self):
        """根据移动标志调整Mario的位置"""

        '''
        目前存在问题，无法依据行动方向决定图像是哪一个？？？？？？？
        '''
        self.gravity = 1.25

        #c更新Mario的center值，而不是rect
        if self.moving_right and self.rect.right < (self.screen_rect.right / 2):
            self.image = self.small_normal_frames[0][0]
            self.center += self.ai_settings.mario_speed_factor

        if self.moving_left and self.rect.left > 0:      # self.screen_rect.left
            self.image = self.small_normal_frames[1][0]
            self.center -= self.ai_settings.mario_speed_factor

        if self.moving_up:
            if self.moving_right and self.rect.bottom > self.screen_rect.bottom - 64:
                self.image = self.small_normal_frames[0][1]
                self.center += self.ai_settings.mario_speed_factor
                self.rect.bottom -= self.gravity

            elif self.moving_left and self.rect.bottom > self.screen_rect.bottom - 64:
                self.image = self.small_normal_frames[1][1]
                self.center -= self.ai_settings.mario_speed_factor
                self.rect.bottom -= self.gravity

            elif self.rect.bottom >= self.screen_rect.bottom - 64:
                self.image = self.small_normal_frames[0][0]
                self.rect.bottom -= self.gravity

        if self.moving_down:
            self.falling()
        # 根据self.center更新rect对象
        self.rect.centerx = self.center

        return self.rect.centerx

    def falling(self):
        """Called when Mario is in a FALL state"""
        # if self.rect.bottom < self.screen_rect.bottom - 24:
        #     self.rect.bottom += self.gravity
        if self.moving_right and self.rect.bottom < self.screen_rect.bottom - 24:
            self.image = self.small_normal_frames[0][1]
            self.center += self.ai_settings.mario_speed_factor
            self.rect.bottom += self.gravity

        elif self.moving_left and self.rect.bottom < self.screen_rect.bottom - 24:
            self.image = self.small_normal_frames[1][1]
            self.center -= self.ai_settings.mario_speed_factor
            self.rect.bottom += self.gravity

        else:
            if self.rect.bottom < self.screen_rect.bottom - 24:
                self.image = self.small_normal_frames[0][0]
                self.rect.bottom += self.gravity

    def blitme(self):
        """在指定位置绘制Mario"""
        self.screen.blit(self.image, self.rect)




    def jumping(self):
        """Called when Mario is in a JUMP state."""
        pass




