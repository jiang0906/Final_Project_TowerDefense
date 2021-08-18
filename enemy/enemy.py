from __future__ import annotations
import random
import pygame
import math
import os
from settings import PATH_1, PATH_2, PATH_3, BASE, IMAGE_PATH
from color_settings import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.model import GameModel

pygame.init()
GREEN_ENEMY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "GreenEnemy.png")), (50, 50))
RED_ENEMY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "RedEnemy.png")), (50, 50))
PURPLE_ENEMY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "PurpleEnemy.png")), (50, 50))
BLACK_ENEMY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "BlackEnemy.png")), (50, 50))

PATH_ALT = [PATH_1, PATH_2, PATH_3]


class GreenEnemy:
    def __init__(self):
        self.max_health = 5
        self.health = self.max_health
        self.path = random.choice(PATH_ALT)
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.image = GREEN_ENEMY_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.__expedition = []
        self.damage_double_check=1

    def move(self):
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        max_count = int(distance / self.stride)

        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance

        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count

        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.rect.center = self.path[self.path_index]

    def draw(self, win):
        for en in self.__expedition:
            win.blit(en.image, en.rect)

            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(win, RED, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(win, GREEN, [en.rect.x, en.rect.y - 10, bar_width, bar_height])

    def stride_revise(self):
        self.stride = 0.85

    def stride_revise_getback(self):
        self.stride = 1

    def damage_double(self, level: int):
        if level == 0:
            self.damage_double_check = 1.3
        elif level == 1:
            self.damage_double_check = 1.6
        elif level == 2:
            self.damage_double_check = 2.0
        elif level == 3:
            self.damage_double_check = 2.3
        elif level == 4:
            self.damage_double_check = 2.6
        elif level == 5:
            self.damage_double_check = 3

    def damage_double_back(self):
        self.damage_double_check = 1


class RedEnemy:
    def __init__(self):
        self.max_health = 8
        self.health = self.max_health
        self.path = random.choice(PATH_ALT)
        self.path_index = 0
        self.move_count = 0
        self.stride = 0.8
        self.image = RED_ENEMY_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.__expedition = []
        self.damage_double_check=1

    def move(self):
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        max_count = int(distance / self.stride)

        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance

        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count

        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.rect.center = self.path[self.path_index]

    def draw(self, win):
        for en in self.__expedition:
            win.blit(en.image, en.rect)

            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(win, RED, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(win, GREEN, [en.rect.x, en.rect.y - 10, bar_width, bar_height])

    def stride_revise(self):
        self.stride = 0.65

    def stride_revise_getback(self):
        self.stride = 0.8

    def damage_double(self, level: int):
        if level==0:
            self.damage_double_check = 1.3
        elif level==1:
            self.damage_double_check = 1.6
        elif level==2:
            self.damage_double_check = 2.0
        elif level==3:
            self.damage_double_check = 2.3
        elif level==4:
            self.damage_double_check = 2.6
        elif level==5:
            self.damage_double_check = 3

    def damage_double_back(self):
        self.damage_double_check = 1


class PurpleEnemy:
    def __init__(self):
        self.max_health = 10
        self.health = self.max_health
        self.path = random.choice(PATH_ALT)
        self.path_index = 0
        self.move_count = 0
        self.stride = 1.4
        self.image = PURPLE_ENEMY_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.__expedition = []
        self.damage_double_check = 1

    def move(self):
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        max_count = int(distance / self.stride)

        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance

        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count

        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.rect.center = self.path[self.path_index]

    def draw(self, win):
        for en in self.__expedition:
            win.blit(en.image, en.rect)

            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(win, RED, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(win, GREEN, [en.rect.x, en.rect.y - 10, bar_width, bar_height])

    def stride_revise(self):
        self.stride = 1.25

    def stride_revise_getback(self):
        self.stride = 1.4

    def damage_double(self, level: int):
        if level==0:
            self.damage_double_check = 1.3
        elif level==1:
            self.damage_double_check = 1.6
        elif level==2:
            self.damage_double_check = 2.0
        elif level==3:
            self.damage_double_check = 2.3
        elif level==4:
            self.damage_double_check = 2.6
        elif level==5:
            self.damage_double_check = 3

    def damage_double_back(self):
        self.damage_double_check = 1


class BlackEnemy:
    def __init__(self):
        self.max_health = 15
        self.health = self.max_health
        self.path = random.choice(PATH_ALT)
        self.path_index = 0
        self.move_count = 0
        self.stride = 1.2
        self.image = BLACK_ENEMY_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.__expedition = []
        self.damage_double_check = 1

    def move(self):
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        max_count = int(distance / self.stride)

        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance

        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count

        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.rect.center = self.path[self.path_index]

    def draw(self, win):
        for en in self.__expedition:
            win.blit(en.image, en.rect)

            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(win, RED, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(win, GREEN, [en.rect.x, en.rect.y - 10, bar_width, bar_height])

    def stride_revise(self):
        self.stride = 1.05

    def stride_revise_getback(self):
        self.stride = 1.2

    def damage_double(self, level: int):
        if level==0:
            self.damage_double_check = 1.3
        elif level==1:
            self.damage_double_check = 1.6
        elif level==2:
            self.damage_double_check = 2.0
        elif level==3:
            self.damage_double_check = 2.3
        elif level==4:
            self.damage_double_check = 2.6
        elif level==5:
            self.damage_double_check = 3

    def damage_double_back(self):
        self.damage_double_check = 1


class EnemyGroup:
    def __init__(self):
        self.campaign_count = 0
        self.campaign_max_count = 60
        self.__reserved_member = []
        self.__expedition = []
        self.wave = 0

    def advance(self, model: GameModel):
        # use model.hp and model.money to access the hp and money information
        self.campaign()
        for en in self.__expedition:
            en.move()
            # delete the object and get money when it is killed
            if en.health <= 0:
                self.retreat(en)

                model.support += 1
                if model.support > 100:
                    model.support = 100
                if model.support + model.notsupport > 100:
                    model.notsupport = 100 - model.support

                if GreenEnemy():
                    model.money += 20
                elif RedEnemy():
                    model.money += 20
                elif PurpleEnemy():
                    model.money += 30
                else:
                    model.money += 30
            # delete the object and drop 1 hp when it reach the base
            if BASE.collidepoint(en.rect.centerx, en.rect.centery):
                self.retreat(en)
                model.hp -= 1

                model.notsupport += 8
                if model.notsupport > 100:
                    model.notsupport = 100
                if model.support + model.notsupport > 100:
                    model.support = 100 - model.notsupport

    def draw(self, win):
        for en in self.__expedition:
            win.blit(en.image, en.rect)
            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(win, RED, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(win, GREEN, [en.rect.x, en.rect.y - 10, bar_width, bar_height])

    def campaign(self):
        """
        Enemy go on an expedition
        """
        if self.campaign_count > self.campaign_max_count and self.__reserved_member:
            self.__expedition.append(self.__reserved_member.pop())
            self.campaign_count = 0
        else:
            self.campaign_count += 1

    def add(self, num: int):
        """
        Generate the enemies for next wave
        """
        # 生成順序為 綠->紫->紅->黑
        if self.wave % 4 == 0:
            self.__reserved_member = [GreenEnemy() for _ in range(num)]
        elif self.wave % 4 == 1:
            self.__reserved_member = [PurpleEnemy() for _ in range(num)]
        elif self.wave % 4 == 2:
            self.__reserved_member = [RedEnemy() for _ in range(num)]
        else:
            self.__reserved_member = [BlackEnemy() for _ in range(num)]
        self.wave += 1

    def get(self):
        """
        Get the enemy list
        """
        return self.__expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.__reserved_member or self.__expedition else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.__expedition.remove(enemy)
