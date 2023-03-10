import pygame
from projectile import Projectile
from math import sin


class Player(pygame.sprite.Sprite):
    def __init__(self, path, spawn):
        super().__init__()
        self.sprites_down_s = []
        self.sprites_down_w = []
        self.sprites_up_s = []
        self.sprites_up_w = []
        self.sprites_right_s = []
        self.sprites_right_w = []
        self.sprites_left_s = []
        self.sprites_left_w = []

        self.sprites_down_s.append(pygame.transform.scale(pygame.image.load(
            path + "static/front/static_front1.png"), (60, 60)))
        self.sprites_down_s.append(pygame.transform.scale(pygame.image.load(
            path + "static/front/static_front2.png"), (60, 60)))
        self.sprites_down_s.append(pygame.transform.scale(pygame.image.load(
            path + "static/front/static_front3.png"), (60, 60)))
        self.sprites_down_s.append(pygame.transform.scale(pygame.image.load(
            path + "static/front/static_front4.png"), (60, 60)))
        self.sprites_down_s.append(pygame.transform.scale(pygame.image.load(
            path + "static/front/static_front5.png"), (60, 60)))
        self.sprites_down_w.append(pygame.transform.scale(pygame.image.load(
            path + "walk/front/walking_front1.png"), (60, 60)))
        self.sprites_down_w.append(pygame.transform.scale(pygame.image.load(
            path + "walk/front/walking_front2.png"), (60, 60)))
        self.sprites_down_w.append(pygame.transform.scale(pygame.image.load(
            path + "walk/front/walking_front3.png"), (60, 60)))
        self.sprites_down_w.append(pygame.transform.scale(pygame.image.load(
            path + "walk/front/walking_front4.png"), (60, 60)))
        self.sprites_up_s.append(pygame.transform.scale(pygame.image.load(path + "static/back/back1.png"), (60, 60)))
        self.sprites_up_s.append(pygame.transform.scale(pygame.image.load(path + "static/back/back2.png"), (60, 60)))
        self.sprites_up_s.append(pygame.transform.scale(pygame.image.load(path + "static/back/back3.png"), (60, 60)))
        self.sprites_up_s.append(pygame.transform.scale(pygame.image.load(path + "static/back/back4.png"), (60, 60)))
        self.sprites_up_s.append(pygame.transform.scale(pygame.image.load(path + "static/back/back5.png"), (60, 60)))
        self.sprites_up_w.append(pygame.transform.scale(pygame.image.load(
            path + "walk/back/walking_back1.png"), (60, 60)))
        self.sprites_up_w.append(pygame.transform.scale(pygame.image.load(
            path + "walk/back/walking_back2.png"), (60, 60)))
        self.sprites_up_w.append(pygame.transform.scale(pygame.image.load(
            path + "walk/back/walking_back3.png"), (60, 60)))
        self.sprites_up_w.append(pygame.transform.scale(pygame.image.load(
            path + "walk/back/walking_back4.png"), (60, 60)))
        self.sprites_right_s.append(pygame.transform.scale(pygame.image.load(
            path + "static/right/static_right1.png"), (60, 60)))
        self.sprites_right_s.append(pygame.transform.scale(pygame.image.load(
            path + "static/right/static_right2.png"), (60, 60)))
        self.sprites_right_s.append(pygame.transform.scale(pygame.image.load(
            path + "static/right/static_right3.png"), (60, 60)))
        self.sprites_right_s.append(pygame.transform.scale(pygame.image.load(
            path + "static/right/static_right4.png"), (60, 60)))
        self.sprites_right_s.append(pygame.transform.scale(pygame.image.load(
            path + "static/right/static_right5.png"), (60, 60)))
        self.sprites_right_w.append(pygame.transform.scale(pygame.image.load(
            path + "walk/right/walking_right1.png"), (60, 60)))
        self.sprites_right_w.append(pygame.transform.scale(pygame.image.load(
            path + "walk/right/walking_right2.png"), (60, 60)))
        self.sprites_right_w.append(pygame.transform.scale(pygame.image.load(
            path + "walk/right/walking_right3.png"), (60, 60)))
        self.sprites_right_w.append(pygame.transform.scale(pygame.image.load(
            path + "walk/right/walking_right4.png"), (60, 60)))
        self.sprites_left_s.append(pygame.transform.flip(self.sprites_right_s[0], True, False))
        self.sprites_left_s.append(pygame.transform.flip(self.sprites_right_s[1], True, False))
        self.sprites_left_s.append(pygame.transform.flip(self.sprites_right_s[2], True, False))
        self.sprites_left_s.append(pygame.transform.flip(self.sprites_right_s[3], True, False))
        self.sprites_left_s.append(pygame.transform.flip(self.sprites_right_s[4], True, False))
        self.sprites_left_w.append(pygame.transform.flip(self.sprites_right_w[0], True, False))
        self.sprites_left_w.append(pygame.transform.flip(self.sprites_right_w[1], True, False))
        self.sprites_left_w.append(pygame.transform.flip(self.sprites_right_w[2], True, False))
        self.sprites_left_w.append(pygame.transform.flip(self.sprites_right_w[3], True, False))

        self.current_sprite = 0
        self.sprite_state = 2
        self.sprite_sound = self.sprite_state - 0.1
        self.image = self.sprites_right_s[self.current_sprite]
        self.spawn_x = spawn[0]
        self.spawn_y = spawn[1]
        self.current_x = spawn[0]
        self.current_y = spawn[1]
        self.rect = self.image.get_rect(topleft=spawn)
        self.moving_x = False
        self.moving_y = False
        self.direction = pygame.math.Vector2()
        self.speed = 2.5
        self.fire = False
        self.reloading = False
        self.vulnerable = True
        self.vulnerable_cooldown = 3000
        self.vulnerable_time = 0
        self.reload_cooldown = 1000
        self.reload_time = 0
        self.bullets = pygame.sprite.Group()
        self.health = 3

        self.shoot_sound = pygame.mixer.Sound("assets/sounds/shoot_2.wav")
        self.step_sound = pygame.mixer.Sound("assets/sounds/step_2.wav")
        self.shot_zombie = pygame.mixer.Sound("assets/sounds/step_2.wav")

        self.obstacles = None
        self.zombies = None
        self.hazards = None

    def get_image(self):
        return self.image

    def get_spawn_x(self):
        return self.spawn_x

    def get_spawn_y(self):
        return self.spawn_y

    def get_current_x(self):
        return self.current_x

    def get_current_y(self):
        return self.current_y

    def get_speed(self):
        return self.direction

    def get_fire(self):
        return self.fire

    def get_reloading(self):
        return self.reloading

    def get_reload_time(self):
        return self.reload_time

    def get_bullets(self):
        return self.bullets

    def get_health(self):
        return self.health

    def get_rect(self):
        return self.rect

    def set_image(self, asset):
        self.image = asset

    def set_spawn_x(self, spawn_x):
        self.spawn_x = spawn_x

    def set_spawn_y(self, spawn_y):
        self.spawn_y = spawn_y

    def set_current_x(self, current_x):
        self.current_x = current_x

    def set_current_y(self, current_y):
        self.current_y = current_y

    def set_speed(self, speed):
        self.direction = speed

    def reset_speed(self):
        self.direction = pygame.math.Vector2()

    def set_reloading(self, reloading):
        self.reloading = reloading

    def set_reload_time(self, reload_time):
        self.reload_time = reload_time

    def add_bullet(self, projectile):
        self.bullets.add(projectile)

    def remove_bullet(self, projectile):
        self.bullets.remove(projectile)

    def set_health(self, health):
        self.health = health

    def set_rect(self, rect):
        self.rect = rect

    def set_rect_topleft(self, x, y):
        self.rect.topleft = (x, y)

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles

    def set_zombies(self, zombies):
        self.zombies = zombies

    def set_hazards(self, hazards):
        self.hazards = hazards

    def set_movement(self, joy):
        if joy.get_hat(0)[1] == 1:
            self.direction.y = -1
            self.sprite_state = 1
            self.moving_y = True
        elif joy.get_hat(0)[1] == -1:
            self.direction.y = 1
            self.sprite_state = 4
            self.moving_y = True
        else:
            self.direction.y = 0
            self.moving_y = False

        if joy.get_hat(0)[0] == 1:
            self.direction.x = 1
            self.sprite_state = 2
            self.moving_x = True
        elif joy.get_hat(0)[0] == -1:
            self.moving_x = True
            self.direction.x = -1
            self.sprite_state = 3
        else:
            self.direction.x = 0
            self.moving_x = False

    def collision(self, orient):
        if not self.vulnerable and pygame.time.get_ticks() - self.vulnerable_time >= self.vulnerable_cooldown:
            self.vulnerable = True
        if orient == 0:
            for sprite in self.obstacles:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:  # Going right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # Going left
                        self.rect.left = sprite.rect.right
            if self.vulnerable:
                for zombie in self.zombies:
                    if zombie.rect.colliderect(self.rect):
                        self.health -= 1
                        self.vulnerable = False
                        self.vulnerable_time = pygame.time.get_ticks()
                if self.hazards is not None:
                    for hazard in self.hazards:
                        if hazard.rect.colliderect(self.rect):
                            self.health -= 1
                            self.vulnerable = False
                            self.vulnerable_time = pygame.time.get_ticks()

        if orient == 1:
            for sprite in self.obstacles:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:  # Going down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:  # Going up
                        self.rect.top = sprite.rect.bottom
            if self.vulnerable:
                for zombie in self.zombies:
                    if zombie.rect.colliderect(self.rect):
                        print(self.health)
                        self.health -= 1
                        print(self.health)
                        self.vulnerable = False
                        self.vulnerable_time = pygame.time.get_ticks()
                if self.hazards is not None:
                    for hazard in self.hazards:
                        if self.health > 0:
                            if hazard.rect.colliderect(self.rect):
                                self.health -= 1
                                self.vulnerable = False
                                self.vulnerable_time = pygame.time.get_ticks()
                        else:
                            self.kill()
            for zombie in self.zombies:
                collide = pygame.sprite.spritecollide(zombie, self.bullets, True)
                if collide:
                    self.shot_zombie.play()
                    zombie.damaged()

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x = self.rect.x + self.direction.x * speed
        self.collision(0)
        self.rect.y = self.rect.y + self.direction.y * speed
        self.collision(1)

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0

    def update(self):
        if self.health > 0:
            self.move(self.speed)
            self.current_sprite += 0.1
            if self.moving_x or self.moving_y:
                if self.current_sprite >= 4:
                    self.current_sprite = 0
                if self.sprite_state == 1:
                    self.image = self.sprites_up_w[int(self.current_sprite)]
                elif self.sprite_state == 2:
                    self.image = self.sprites_right_w[int(self.current_sprite)]
                elif self.sprite_state == 3:
                    self.image = self.sprites_left_w[int(self.current_sprite)]
                elif self.sprite_state == 4:
                    self.image = self.sprites_down_w[int(self.current_sprite)]

            else:
                if self.current_sprite >= 5:
                    self.current_sprite = 0
                if self.sprite_state == 1:
                    self.image = self.sprites_up_s[int(self.current_sprite)]
                elif self.sprite_state == 2:
                    self.image = self.sprites_right_s[int(self.current_sprite)]
                elif self.sprite_state == 3:
                    self.image = self.sprites_left_s[int(self.current_sprite)]
                elif self.sprite_state == 4:
                    self.image = self.sprites_down_s[int(self.current_sprite)]

            if not self.vulnerable:
                alpha = self.wave_value()
                self.image.set_alpha(alpha)
            else:
                self.image.set_alpha(255)
        else:
            self.kill()

    def shoot(self, direction):
        if self.health > 0:
            if self.sprite_state == 2:
                if direction == (0, 0):
                    direction = (1, 0)
                bullet = Projectile(
                    "assets/bullet.png", direction, self.rect.midright[0], self.rect.midright[1], self.obstacles)
                self.bullets.add(bullet)
            elif self.sprite_state == 1:
                if direction == (0, 0):
                    direction = (0, 1)
                bullet = Projectile(
                    "assets/bullet.png", direction, self.rect.midtop[0], self.rect.midtop[1], self.obstacles)
                self.bullets.add(bullet)
            elif self.sprite_state == 3:
                if direction == (0, 0):
                    direction = (-1, 0)
                bullet = Projectile(
                    "assets/bullet.png", direction, self.rect.midleft[0], self.rect.midleft[1], self.obstacles)
                self.bullets.add(bullet)
            elif self.sprite_state == 4:
                if direction == (0, 0):
                    direction = (0, -1)
                bullet = Projectile(
                    "assets/bullet.png", direction, self.rect.midbottom[0], self.rect.midbottom[1], self.obstacles)
                self.bullets.add(bullet)

    def set_fire(self, joy):
        if joy.get_button(1) == 1 and not self.reloading:
            self.shoot_sound.play()
            self.shoot(joy.get_hat(0))
            self.reloading = True
            self.reload_time = pygame.time.get_ticks()
        elif self.reloading:
            if pygame.time.get_ticks() - self.reload_time >= self.reload_cooldown:
                self.reloading = False
