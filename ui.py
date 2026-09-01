import pygame
from settings import (
    VIRTUAL_WIDTH, RESOLUTIONS, VOLUME_STEPS,
    COLOR_TEXT, COLOR_ACCENT, COLOR_BAR_ACTIVE, 
    COLOR_BAR_INACTIVE, COLOR_BORDER
)

class SettingsMenu:
    def __init__(self):
        self.res_index = 0
        self.is_fullscreen = False
        self.volume_level = 5  # Default is 5 out of 10 (50% volume)
        self.selected_option = 0  # 0: Resolution, 1: Fullscreen, 2: Volume

        self.font = pygame.font.SysFont("arial", 24)
        self.big_font = pygame.font.SysFont("arial", 32, bold=True)

    def handle_input(self, event):
        """Keyboard controls (arrow keys + WASD)."""
        if event.type == pygame.KEYDOWN:
            # Navigate up/down through menu items
            if event.key in (pygame.K_UP, pygame.K_w):
                self.selected_option = (self.selected_option - 1) % 3
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.selected_option = (self.selected_option + 1) % 3

            # Change values ​​left / right
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                self._change_option_value(-1)
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                self._change_option_value(1)

    def _change_option_value(self, direction):
        if self.selected_option == 0:  # Resolution
            self.res_index = (self.res_index + direction) % len(RESOLUTIONS)
        elif self.selected_option == 1:  # Toggle Full-Screen Mode
            self.is_fullscreen = not self.is_fullscreen
        elif self.selected_option == 2:  # Volume steps
            self.volume_level = max(0, min(VOLUME_STEPS, self.volume_level + direction))
            self._apply_volume()

    def _apply_volume(self):
        """Applying a volume level from 0.0 to 1.0 in Pygame Mixer."""
        volume_float = self.volume_level / VOLUME_STEPS
        pygame.mixer.music.set_volume(volume_float)

    def draw(self, surface):
        surface.fill((15, 15, 25))

        # Title
        title = self.big_font.render("SETTINGS", True, COLOR_TEXT)
        surface.blit(title, (VIRTUAL_WIDTH // 2 - title.get_width() // 2, 40))

        # 1. Resolution selection
        res_w, res_h = RESOLUTIONS[self.res_index]
        res_str = f"Rsolution:  < {res_w} x {res_h} >"
        color0 = COLOR_ACCENT if self.selected_option == 0 else COLOR_TEXT
        txt0 = self.font.render(res_str, True, color0)
        surface.blit(txt0, (100, 140))

        # 2. Full-screen mode
        fs_str = f"Screen mode: < {'Full-screen' if self.is_fullscreen else 'Windowed'} >"
        color1 = COLOR_ACCENT if self.selected_option == 1 else COLOR_TEXT
        txt1 = self.font.render(fs_str, True, color1)
        surface.blit(txt1, (100, 210))

        # 3. Volume slider
        color2 = COLOR_ACCENT if self.selected_option == 2 else COLOR_TEXT
        vol_pct = int((self.volume_level / VOLUME_STEPS) * 100)
        vol_str = f"Volume: {vol_pct}%"
        txt2 = self.font.render(vol_str, True, color2)
        surface.blit(txt2, (100, 280))

        # Rendering the volume rectangles
        self._draw_volume_bar(surface, x=100, y=325)

    def _draw_volume_bar(self, surface, x, y):
        """Rendering the slider as a series of rectangles."""
        block_width = 28
        block_height = 40
        gap = 8  # Spacing between rectangles

        for i in range(VOLUME_STEPS):
            rect = pygame.Rect(x + i * (block_width + gap), y, block_width, block_height)

            if i < self.volume_level:
                # Filled (active) rectangle
                pygame.draw.rect(surface, COLOR_BAR_ACTIVE, rect, border_radius=4)
            else:
                # Empty (inactive) rectangle
                pygame.draw.rect(surface, COLOR_BAR_INACTIVE, rect, border_radius=4)

            # Outline
            border_color = COLOR_ACCENT if (self.selected_option == 2 and i < self.volume_level) else COLOR_BORDER
            pygame.draw.rect(surface, border_color, rect, width=2, border_radius=4)