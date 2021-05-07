import pygame

# задание параметров
WIDTH = 600
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

class BackGround(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

class Generator(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load(filename).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = 0

    def update(self):
        self.angle += 2
        self.rotate()

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

# создание игры и окна
pygame.init()
pygame.mixer.init() # инициализация звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # задание экрана
pygame.display.set_caption("Ветрогенератор и облака.")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

background = BackGround("background.png")
all_sprites.add(background)

cloud1 = Cloud(10, 70, "cloud.png")
all_sprites.add(cloud1)

cloud2 = Cloud(550, 120, "cloud.png")
all_sprites.add(cloud2)

cloud3 = Cloud(250, 170, "cloud.png")
all_sprites.add(cloud3)

generator = Generator(185, 230, "generator.png")
all_sprites.add(generator)



running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()