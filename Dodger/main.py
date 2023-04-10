import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Love Catcher")

BG = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 40
PLAYER_VEL = 7

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

HEART_WIDTH = 10
HEART_HEIGHT = 15
HEART_VEL = 4

FONT = pygame.font.SysFont("comicsans", 30)


def draw(player, elapsed_time, stars,hearts,hearts_collected):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    hearts_text = FONT.render(f"Hearts Collected: {hearts_collected}",1,"white")
    WIN.blit(hearts_text,(570,10))



    pygame.draw.rect(WIN, "purple", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    for heart in hearts:
        pygame.draw.rect(WIN,'red',heart)

    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0
    heart_add_increment = 2100
    heart_count = 0

    stars = []
    hit = False
    hearts = []
    hearts_collected = 0
    while run:
        star_count += clock.tick(60)
        heart_count += clock.tick(65)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT,
                                   STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0
        
        if heart_count > heart_add_increment:
            for _ in range(3):
                heart_x = random.randint(0,WIDTH - HEART_WIDTH)
                heart = pygame.Rect(heart_x, -HEART_WIDTH, HEART_WIDTH, HEART_WIDTH)
                hearts.append(heart)
            heart_add_increment = max(200, heart_add_increment -50)
            heart_count = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        for heart in hearts[:]:
            heart.y += HEART_VEL
            if heart.y > HEIGHT:
                hearts.remove(heart)
            elif heart.y + heart.height >= player.y and heart.colliderect(player):
                hearts.remove(heart)
                hearts_collected += 1

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars,hearts,hearts_collected)

    pygame.quit()


if __name__ == "__main__":
    main()