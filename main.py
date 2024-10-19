import pygame

pygame.init()

screen = pygame.display.set_mode((620, 620))
screen.fill((30, 30, 30))
pygame.display.set_caption("Click Speed Test")
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)

color = (0, 255, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
RED = (255, 0, 0)
MAGENTA = (255,0,255)

cursor_pos = (100, 100)
radius = 30
mouse_clicked = False
click_speed = 0
time = 0

run = True

while run:
    time_reading = font.render(f'TIME: {round(time / 1000, 1)}s', True, (255, 255, 255), 1)
    speed_reading = font.render(f'CPS: {round(click_speed / ((time + 0.01) / 1000), 1)}/s', True, (255, 255, 255), 1)

    screen.blit(time_reading, (400, 10))
    screen.blit(speed_reading, (10, 10))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if time < 5000:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_speed += 1
                mouse_clicked = True
                screen.fill((30, 30, 30))
                radius = 30
                cursor_pos = pygame.mouse.get_pos()
            if mouse_clicked:
                time = pygame.time.get_ticks()
                if radius < 50:
                    if click_speed / (time/1000) <= 3:
                        color = CYAN
                    elif click_speed / (time/1000) <= 5:
                        color = GREEN
                    elif click_speed / (time/1000) <= 7:
                        color = YELLOW
                    elif click_speed / (time/1000) <= 9:
                        color = ORANGE
                    elif click_speed / (time/1000) <= 11:
                        color = RED
                    elif click_speed / (time/1000) > 11:
                        color = MAGENTA
                    pygame.draw.circle(screen, color, cursor_pos, radius, int(radius * 2))
                else:
                    screen.fill((30, 30, 30))
    radius += 1
    if time >= 5000:
        screen.fill((30, 30, 30))
        end_text = font.render(f"CPS: {click_speed / 5}", True, (255, 255, 255))
        screen.blit(end_text, (225, 300))

    pygame.display.update()
    clock.tick(600)