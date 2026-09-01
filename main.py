import pygame
import sys
from settings import VIRTUAL_WIDTH, VIRTUAL_HEIGHT, RESOLUTIONS
from ui import SettingsMenu

def main():
    pygame.init()
    pygame.mixer.init()

    # Create a virtual canvas of fixed size
    virtual_surface = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))

    menu = SettingsMenu()
    current_res = RESOLUTIONS[menu.res_index]
    flags = pygame.FULLSCREEN if menu.is_fullscreen else 0
    screen = pygame.display.set_mode(current_res, flags)
    pygame.display.set_caption("Tetris Arcade - Settings")

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Pass keyboard events to the menu
            menu.handle_input(event)

            # Checking for screen mode or resolution changes
            new_res = RESOLUTIONS[menu.res_index]
            new_flags = pygame.FULLSCREEN if menu.is_fullscreen else 0

            if new_res != current_res or new_flags != flags:
                current_res = new_res
                flags = new_flags
                screen = pygame.display.set_mode(current_res, flags)

        # 1. Render the menu onto a virtual canvas.
        menu.draw(virtual_surface)

        # 2. Scale the image to fit the actual window/screen.
        scaled_surface = pygame.transform.smoothscale(virtual_surface, current_res)
        screen.blit(scaled_surface, (0, 0))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()