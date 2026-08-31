import pygame

pygame.init()

# Set up the display
RESOLUTIONS = [(800, 600), (1024, 768), (1280, 720), (1366, 768), (1600, 900), (1920, 1080)]
current_res_idx = 0
pygame.display.set_caption("Tetris Game")

VIRTUAL_WIDTH = 800
VIRTUAL_HEIGHT = 600

virtual_surface = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))


current_w, current_h = RESOLUTIONS[current_res_idx]
screen = pygame.display.set_mode((current_w, current_h))
pygame.display.set_caption("Resolution setting")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
running = True

def change_resolution(index):
    global screen, current_w, current_h
    current_w, current_h = RESOLUTIONS[index]
    # recreate window with new resolution
    screen = pygame.display.set_mode((current_w, current_h))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # you can set up resolution by using 1, 2, 3, 4, 5, 6
            if event.key == pygame.K_1:
                current_res_idx = 0
                change_resolution(current_res_idx)
            elif event.key == pygame.K_2:
                current_res_idx = 1
                change_resolution(current_res_idx)
            elif event.key == pygame.K_3:
                current_res_idx = 2
                change_resolution(current_res_idx)
            elif event.key == pygame.K_4:
                current_res_idx = 3
                change_resolution(current_res_idx)
            elif event.key == pygame.K_5:
                current_res_idx = 4
                change_resolution(current_res_idx)
            elif event.key == pygame.K_6:
                current_res_idx = 5
                change_resolution(current_res_idx)

# rendering in Virtual canvas
    virtual_screen.fill((30, 30, 40))

    # Text of interface 
    text_info = font.render(
        f"Current resolution: {current_w}x{current_h}", True, (255, 255, 255)
    )
    text_hint = font.render(
        "press 1 (800, 600), 2 (1024, 768), 3 (1280, 720), 4 (1366, 768), 5 (1600, 900), or 6 (1920, 1080)",
        True,
        (200, 200, 200),
    )

    virtual_screen.blit(text_info, (50, 50))
    virtual_screen.blit(text_hint, (50, 120))

    # rendering of testing object
    pygame.draw.rect(virtual_screen, (230, 80, 80), (50, 200, 200, 200))

    # Scaling to the real window
    scaled_surface = pygame.transform.scale(
        virtual_screen, (current_w, current_h)
    )
    screen.blit(scaled_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()