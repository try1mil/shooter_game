#Create your own shooter
import pygame
import random
from pygame import *

pygame.init()
mixer.init()
font.init()


window = display.set_mode((700, 500))
display.set_caption("Shooter")


background = transform.scale(image.load("galaxy.jpg"), (700, 500))
player_image = transform.scale(image.load("rocket.png"), (85, 80))
enemy_image = transform.scale(image.load('ufo.png'), (78, 80))
bullet_image = transform.scale(image.load("bullet.png"), (20, 22))
asteroid_image = transform.scale(image.load("asteroid.png"), (80, 80))

mixer.music.load('space.ogg')
mixer.music.play(-1)
shoot_sound = mixer.Sound('fire.ogg')

FPS = 60
clock = time.Clock()

lost = 0
hit_saucers = 0

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.speed = 7

    def update(self, keys):
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed

        self.rect.clamp_ip(window.get_rect())


class Enemy(GameSprite):
    def __init__(self):
        x = random.randint(0, 622)
        y = random.randint(-150, -50)
        super().__init__(x, y, enemy_image)
        self.speed = 1

    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            lost += 1
            self.rect.y = random.randint(-150, -50)
            self.rect.x = random.randint(0, 622)


class Asteroid(GameSprite):
    def __init__(self):
        x = random.randint(0, 622)
        y = random.randint(-150, -50)
        super().__init__(x, y, asteroid_image)
        self.speed = random.randint(1, 2)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = random.randint(-150, -50)
            self.rect.x = random.randint(0, 622)


class Bullet(GameSprite):
    def __init__(self, x, y):
        super().__init__(x, y, bullet_image)
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

def main():
    global lost, hit_saucers
    running = True

    player = Player(310, 400, player_image)
      
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    for _ in range(5):
        enemies.add(Enemy())
    for _ in range(5):
        asteroids.add(Asteroid())

    font = pygame.font.SysFont('Arial', 30)
    font_2 = pygame.font.SysFont('Arial', 70)

    win = font_2.render('YOU WON!', True, (255, 215, 0))
    lose = font_2.render('YOU LOSE!', True, (255, 215, 0))

    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == KEYDOWN and e.key == K_SPACE:
                bullet = Bullet(player.rect.centerx - 10, player.rect.top)
                bullets.add(bullet)
                shoot_sound.play()

        keys = key.get_pressed()
        player.update(keys)

        enemies.update()
        bullets.update()
        asteroids.update()

        collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
        for _ in collisions:
            hit_saucers += 1
            enemies.add(Enemy())

        if pygame.sprite.spritecollide(player, asteroids, True):
            window.blit(lose, (200, 200))
            pygame.display.update()
            pygame.time.wait(2000)
            running = False

        elif hit_saucers >= 10:
            window.blit(win, (200, 200))
            pygame.display.update()
            pygame.time.wait(2000)
            running = False

        elif lost > 3:
            window.blit(lose, (200, 200))
            pygame.display.update()
            pygame.time.wait(2000)
            running = False

        window.blit(background, (0, 0))
        player.draw(window)
        bullets.draw(window)
        enemies.draw(window)
        asteroids.draw(window)

        miss_text = font.render(f"Missed: {lost}", True, (255, 255, 255))
        hit_text = font.render(f"Hits: {hit_saucers}", True, (255, 255, 255))
        window.blit(miss_text, (10, 10))
        window.blit(hit_text, (10, 40))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()