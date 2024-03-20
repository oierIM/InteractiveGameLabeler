import pygame
import os
import json
from button import Button
json_filename = "button_coordinates.json"

# Pygame hasieratu
pygame.init()

# Irudiak karpeta batetik irakurri eta gordetzeko funtzioa
def load_images(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            images.append((filename, pygame.image.load(os.path.join(folder_path, filename))))
    return images

#Botoiak kargatu Button klaseko instantzi bezala
def load_buttons(button_coordinates_data):
    buttons = {i: [] for i in button_coordinates_data.keys()}
    for i in buttons:
        for j in button_coordinates_data[i]:
            t = j["top_left"]["x"], j["top_left"]["y"]
            b = j["bottom_right"]["x"], j["bottom_right"]["y"]
            new_button = Button(t, b, i)
            buttons[i].append(new_button)
    return buttons

# irudi batean botoi bat badago, marraztu botoia
def draw_buttons(image_index):
    screen.fill((255, 255, 255))

    # marraztu irudia
    scaled_image = pygame.transform.scale(image_list[image_index][1],
                                          (int(image_list[image_index][1].get_width() * calculate_scale_factor(image_list[image_index][1])),
                                           int(image_list[image_index][1].get_height() * calculate_scale_factor(image_list[image_index][1]))))
    screen.blit(scaled_image, (0, 0))

        
    blue_with_transparency = (0, 0, 255, 128) # (R, G, B, alpha)
    if image_list[image_index][0] in button_data:
        for button in button_data[image_list[image_index][0]]:
            #Lortu kordenadak
            top_left = (button.tx, button.ty)
            bottom_right = (button.bx, button.by)

            #Marraztu karratua
            size = (abs(button.bx - button.tx), abs(button.by - button.ty))
            transparent_surface = pygame.Surface(size, pygame.SRCALPHA)
            pygame.draw.rect(transparent_surface, blue_with_transparency, (0, 0, size[0], size[1]), 0)
            screen.blit(transparent_surface, (top_left, (button.bx - button.tx, button.ty - button.ty)))


    pygame.display.flip()

#Click baten kordenatuak pasata, lortu kordenatuaren gainean dagoen botoia
def detect_button(x, y, filename):
    for button in button_data[filename]:
        if button.tx < x < button.bx and button.ty < y < button.by:
            return button
    return None

# Irudien tamaina eskalatzeko funtzioa
def calculate_scale_factor(image):
    image_width, image_height = image.get_size()
    return min(window_width / image_width, window_height / image_height)



# Irudien karpeta adierazi eta kargatu
image_folder = "images"
image_list = load_images(image_folder)
total_images = len(image_list)
current_image_index = 0

# Pantailaren tamaina adierazi (irudien resolution ikusi eta aldatu)
window_width = 1765
window_height = 993
screen = pygame.display.set_mode((window_width, window_height))

# botoien koordenatuak gordeko diren JSON fitxategia sortu
with open(json_filename, "r") as f:
    button_coordinates_data = json.load(f)

button_data = load_buttons(button_coordinates_data)

# botoiak nora joan diren marrazteko
mouse_pressed = False
top_left_coordinates = None

# irudiak pantailaratu hasi aurretik
draw_buttons(current_image_index)

# Define variables for double-click detection
last_click_time = 0
double_click_threshold = 500  # Time threshold for double-click in milliseconds


running = True
while running:
    dbclock = pygame.time.Clock()
    for event in pygame.event.get():
        image_file = image_list[current_image_index][0]

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            current_time = pygame.time.get_ticks()
            if current_time - last_click_time < double_click_threshold:
                button = detect_button(x, y, image_file)
                if button != None:
                    print(button)

            last_click_time = pygame.time.get_ticks()

            # sagua sakatu denean, botoiaren goiko ezkerreko puntua gorde
            if not mouse_pressed:
                top_left_coordinates = (x, y)
                mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # sagua askatu denean, botoiaren beheko eskuineko puntua gorde
            if mouse_pressed:
                x, y = event.pos
                bottom_right_coordinates = (x, y)
                mouse_pressed = False

                # botoiaren koordenatuak gorde
                if abs(top_left_coordinates[0] - bottom_right_coordinates[0]) >100 and abs(top_left_coordinates[1] - bottom_right_coordinates[1]) > 100:
                    print("Karratua egiten")
                    button = Button(top_left_coordinates, bottom_right_coordinates, image_file)
                    button_data[image_file].append(button)
                    button.save_json()

                # botoiak marraztu
                draw_buttons(current_image_index)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # Aurreko irudia
                current_image_index = (current_image_index - 1) % total_images
                draw_buttons(current_image_index)
            elif event.key == pygame.K_RIGHT:  # Hurrengo irudia
                current_image_index = (current_image_index + 1) % total_images
                draw_buttons(current_image_index)

pygame.quit()