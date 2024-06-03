import pygame
import os
import json
from button import Button
import tkinter as tk
from tkinter import simpledialog
json_filename = "button_coordinates.json"

# Pygame initialization
pygame.init()

# Function to load images from a folder
def load_images(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            images.append((filename, pygame.image.load(os.path.join(folder_path, filename))))
    return images

# Load buttons as instances of the Button class
def load_buttons(button_coordinates_data):
    buttons = {i: [] for i in button_coordinates_data.keys()}
    for i in buttons:
        for j in button_coordinates_data[i]:
            t = j["top_left"]["x"], j["top_left"]["y"]
            b = j["bottom_right"]["x"], j["bottom_right"]["y"]
            type_of_button = j.get("type_of_button", 0)  # Default to 0 if not specified
            new_button = Button(t, b, i, type_of_button)
            buttons[i].append(new_button)
    return buttons

# Color mapping for different types of buttons
color_map = {
    0: (0, 0, 255, 128),  # Blue 
    1: (255, 0, 0, 128),  # Red 
    2: (0, 255, 0, 128),  # Green 
    3: (255, 255, 0, 128),  # Yellow 
}

# Draw buttons on an image
def draw_buttons(image_index):
    screen.fill((255, 255, 255))

    # Draw the image
    scaled_image = pygame.transform.scale(image_list[image_index][1],
                                          (int(image_list[image_index][1].get_width() * calculate_scale_factor(image_list[image_index][1])),
                                           int(image_list[image_index][1].get_height() * calculate_scale_factor(image_list[image_index][1]))))
    screen.blit(scaled_image, (0, 0))

    if image_list[image_index][0] in button_data:
        for button in button_data[image_list[image_index][0]]:
            # Get coordinates
            top_left = (button.tx, button.ty)
            bottom_right = (button.bx, button.by)

            # Determine color based on type_of_button
            color = color_map.get(button.type_of_button, (0, 0, 255, 128))  # Default to blue if not found

            # Draw rectangle
            size = (abs(button.bx - button.tx), abs(button.by - button.ty))
            transparent_surface = pygame.Surface(size, pygame.SRCALPHA)
            pygame.draw.rect(transparent_surface, color, (0, 0, size[0], size[1]), 0)
            screen.blit(transparent_surface, (top_left, (button.bx - button.tx, button.ty - button.ty)))

    pygame.display.flip()

# Detect button based on click coordinates
def detect_button(x, y, filename):
    for button in button_data[filename]:
        if button.tx < x < button.bx and button.ty < y < button.by:
            return button
    return None

# Calculate scale factor for images
def calculate_scale_factor(image):
    image_width, image_height = image.get_size()
    return min(window_width / image_width, window_height / image_height)

# Function to get type_of_button input from the user via a Tkinter dialog
def get_type_of_button():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    type_of_button = simpledialog.askinteger("Input", "Enter the type_of_button (integer value):")
    root.destroy()
    return type_of_button

# Specify image folder and load images
image_folder = "joko1/images"
image_list = load_images(image_folder)
total_images = len(image_list)
current_image_index = 0

# Set window size (adjust based on image resolution)
window_width = 1765
window_height = 993
screen = pygame.display.set_mode((window_width, window_height))

# Create JSON file to store button coordinates
with open(json_filename, "r") as f:
    button_coordinates_data = json.load(f)

button_data = load_buttons(button_coordinates_data)

# Variables to track mouse presses
mouse_pressed = False
top_left_coordinates = None

# Draw initial image and buttons
draw_buttons(current_image_index)

# Variables for double-click detection
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
                if button is not None:
                    print(button)

            last_click_time = pygame.time.get_ticks()

            # When mouse button is pressed, store the top-left corner coordinates
            if not mouse_pressed:
                top_left_coordinates = (x, y)
                mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # When mouse button is released, store the bottom-right corner coordinates
            if mouse_pressed:
                x, y = event.pos
                bottom_right_coordinates = (x, y)
                mouse_pressed = False

                # Save button coordinates if a valid rectangle is selected
                if abs(top_left_coordinates[0] - bottom_right_coordinates[0]) > 100 and abs(top_left_coordinates[1] - bottom_right_coordinates[1]) > 100:
                    type_of_button = get_type_of_button()
                    if type_of_button is not None:  # Ensure the user didn't cancel the input
                        button = Button(top_left_coordinates, bottom_right_coordinates, image_file, type_of_button)
                        button_data[image_file].append(button)
                        button.save_json()

                    # Draw updated buttons
                    draw_buttons(current_image_index)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # Previous image
                current_image_index = (current_image_index - 1) % total_images
                draw_buttons(current_image_index)
            elif event.key == pygame.K_RIGHT:  # Next image
                current_image_index = (current_image_index + 1) % total_images
                draw_buttons(current_image_index)

pygame.quit()
