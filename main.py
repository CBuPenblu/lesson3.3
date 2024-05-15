import pygame
import random

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Alien Shooter")
icon = pygame.image.load("img/istockphoto-1327876790-612x612.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 100
target_height = 100

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

color = get_random_color()

font = pygame.font.Font(None, 74)

score = 0
misses = 0
high_score = 0
message = ""

initial_speed = 0.5
target_speed_x = random.choice([-initial_speed, initial_speed])
target_speed_y = random.choice([-initial_speed, initial_speed])

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 1
                if score > high_score:
                    high_score = score
                message = ""
                target_speed_x *= 1.1
                target_speed_y *= 1.1
            else:
                message = ":) LOOSER (:"
                misses += 1
                score = 0
                color = get_random_color()
                target_speed_x = random.choice([-initial_speed, initial_speed])
                target_speed_y = random.choice([-initial_speed, initial_speed])

    target_x += target_speed_x
    target_y += target_speed_y

    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    screen.blit(target_img, (target_x, target_y))

    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    misses_text = font.render("Tries: " + str(misses), True, (255, 255, 255))
    screen.blit(misses_text, (500, 10))

    high_score_text = font.render("High Score: " + str(high_score), True, (255, 255, 255))
    screen.blit(high_score_text, (900, 10))

    if message:
        message_text = font.render(message, True, (255, 0, 0))
        screen.blit(message_text, (
            SCREEN_WIDTH // 2 - message_text.get_width() // 2, SCREEN_HEIGHT // 6 - message_text.get_height() // 6))

    pygame.display.update()

pygame.quit()