import pygame

# Virtual resolution (the canvas on which everything is drawn)
VIRTUAL_WIDTH = 800
VIRTUAL_HEIGHT = 600

# Available resolutions
RESOLUTIONS = [
    (800, 600),
    (1024, 768),
    (1280, 720),
    (1920, 1080)
]

# Block volume scale settings
VOLUME_STEPS = 10  # Number of small rectangles (10 divisions = 100%, 1 division = 10%)

# Color polette
COLOR_BG = (15, 15, 25)
COLOR_TEXT = (240, 240, 240)
COLOR_ACCENT = (0, 220, 255)         # Active row highlight color
COLOR_BAR_ACTIVE = (0, 230, 120)     # Filled rectangle (green/turquoise)
COLOR_BAR_INACTIVE = (40, 45, 60)    # Empty rectangle
COLOR_BORDER = (80, 85, 100)