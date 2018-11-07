import sys
import pygame
from mario import Mario
import settings as st
from data import ground_step



def check_keydown_events(event, ai_settings, screen, mario):
    """响应按键"""
    # keys = pygame.key.get_pressed()

    # if keys[pygame.K_RIGHT]:
    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
        mario.state = st.WALK
        if event.key == pygame.K_RIGHT:
            # 向右移动Mario
            mario.moving_right = True
            mario.state = st.WALK_RIGHT

        elif event.key == pygame.K_LEFT:
            # 向左移动Mario
            mario.moving_left = True
            mario.state = st.WALK_LEFT

    elif event.key == pygame.K_w:
        # 马里奥跳跃
        mario.moving_up = True
        mario.state = st.JUMP

def check_keyup_events(event, mario):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        mario.moving_right = False
        mario.state = st.STAND

    elif event.key == pygame.K_LEFT:
        mario.moving_left = False
        mario.state = st.STAND

    if event.key == pygame.K_w:
        mario.moving_up = False
        mario.moving_down = True
        mario.state = st.FALL


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

def handle_state(marios, enemies):
    # spritecollideany
    # spritecollide
    if pygame.sprite.groupcollide(marios, enemies, False, True):
        # enemies.empty()  #'''这句话很关键'''
        print('THEY ARE TOGETHER+++++++++++++++++++++++++++++++++++++')

def update_screen(ai_settings, screen, mario, enemies, centerx):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 背景图片
    background_image_filename = 'resources/images/level_1.png'
    # 每次循环时都重绘屏幕
    background = pygame.image.load(background_image_filename).convert()
    # 将背景图画上去
    screen.blit(background, (-centerx, 0))
    for enemy in enemies:
        enemy.blitme(centerx)
    # enemy_shadow.blitme(centerx)
    mario.blitme(centerx)
    # 让最近绘制的屏幕可见
    pygame.display.update()










def setup_ground(self):
    """Creates collideable, invisible rectangles over top of the ground for
    sprites to walk on"""

    ground_rect1 = ground_step.Ground(0, 200, 2953, 60)
    ground_rect2 = ground_step.Ground(3048, 200, 635, 60)
    ground_rect3 = ground_step.Ground(3819, 200, 2735, 60)
    ground_rect4 = ground_step.Ground(6647, 200, 2300, 60)

    self.ground_group = pygame.sprite.Group(ground_rect1,
                                        ground_rect2,
                                        ground_rect3,
                                        ground_rect4)

def setup_pipes(self):
    """Create collideable rects for all the pipes"""

    pipe1 = ground_step.Ground(393, 170, 35, 30)
    pipe2 = ground_step.Ground(560, 155, 35, 45)
    pipe3 = ground_step.Ground(1973, 366, 83, 170)
    pipe4 = ground_step.Ground(2445, 366, 83, 170)
    pipe5 = ground_step.Ground(6989, 452, 83, 82)
    pipe6 = ground_step.Ground(7675, 452, 83, 82)

    self.pipe_group = pygame.sprite.Group(pipe1, pipe2,
                                        pipe3, pipe4,
                                        pipe5, pipe6)

def setup_steps(self):
    """Create collideable rects for all the steps"""
    step1 = ground_step.Ground(5745, 495, 40, 44)
    step2 = ground_step.Ground(5788, 452, 40, 44)
    step3 = ground_step.Ground(5831, 409, 40, 44)
    step4 = ground_step.Ground(5874, 366, 40, 176)

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

    self.step_group = pygame.sprite.Group(step1, step2,
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

def setup_spritegroups(self):
    """Sprite groups created for convenience"""
    self.ground_step_pipe_group = pygame.sprite.Group(self.ground_group,
                                                  self.pipe_group,
                                                  self.step_group)

def adjust_mario_position(self):
    """Adjusts Mario's position based on his x, y velocities and
    potential collisions"""
    self.last_x_position = self.mario.rect.right
    self.mario.rect.x += round(self.mario.x_vel)
    self.check_mario_x_collisions()

    if self.mario.in_transition_state == False:
        self.mario.rect.y += round(self.mario.y_vel)
        self.check_mario_y_collisions()


def check_mario_x_collisions(self):
    """Check for collisions after Mario is moved on the x axis"""
    collider = pygame.sprite.spritecollideany(self.mario,
                                            self.ground_step_pipe_group)
    if collider:
        self.adjust_mario_for_x_collisions(collider)

def adjust_mario_for_x_collisions(self, collider):
    """Puts Mario flush next to the collider after moving on the x axis"""
    if self.mario.rect.x < collider.rect.x:
        self.mario.rect.right = collider.rect.left
    else:
        self.mario.rect.left = collider.rect.right

    self.mario.x_vel = 0


def check_mario_y_collisions(self):
    """Checks for collisions when Mario moves along the y-axis"""
    ground_step_or_pipe = pygame.sprite.spritecollideany(self.mario, self.ground_step_pipe_group)
    if ground_step_or_pipe:
        self.adjust_mario_for_y_ground_pipe_collisions(ground_step_or_pipe)
    self.test_if_mario_is_falling()

def adjust_mario_for_y_ground_pipe_collisions(self, collider):
    """Mario collisions with pipes on the y-axis"""
    if self.mario.rect.bottom < collider.rect.bottom:
        self.mario.y_vel = 0
        self.mario.rect.bottom = collider.rect.top
    elif self.mario.rect.top > collider.rect.top:
        self.mario.y_vel = 7
        self.mario.rect.top = collider.rect.bottom

def test_if_mario_is_falling(self):
    """Changes Mario to a FALL state if more than a pixel above a pipe,
    ground, step or box"""
    self.mario.rect.y += 1
    test_collide_group = pygame.sprite.Group(self.ground_step_pipe_group)

    self.mario.rect.y -= 1






