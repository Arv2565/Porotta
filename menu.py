import pygame
import subprocess

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

background_img = pygame.image.load('blah.png')


# Set the title of the game
pygame.display.set_caption("Menu - Hope Among the Ruins")
icon = pygame.image.load('first.png')
pygame.display.set_icon(icon)

# Set the font for the menu items
font = pygame.font.Font('yui.otf', 36)

# Define the menu items
menu_items = ["Start Game","Exit"]

# Set the default selected menu item
selected_item = 0

# Main game loop
while True:
    # Background Image

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item -= 1
                if selected_item < 0:
                    selected_item = len(menu_items) - 1
            if event.key == pygame.K_DOWN:
                selected_item += 1
                if selected_item >= len(menu_items):
                    selected_item = 0
            if event.key == pygame.K_RETURN:
                if selected_item == 0:
                    # Launch the game
                    subprocess.Popen(["python", "game_file.py"])
                
                elif selected_item == 1:
                    # Quit the game
                    pygame.quit()
                    quit()

    # Draw the screen
    screen.fill((0, 0, 0))

    for i, item in enumerate(menu_items):
        if i == selected_item:
            text = font.render(item, True, (255, 0, 0))
        else:
            text = font.render(item, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (screen_width // 2, (i + 1) * (screen_height //(len(menu_items) + 1)))
        #screen.blit(background_img, (0, 0))
        screen.blit(text, text_rect)
        #screen.fill((0, 0, 0))
        

    # Update the screen
    pygame.display.update()