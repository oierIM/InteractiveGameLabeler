import pygame
import json
import os

pygame.init()

# Load button coordinates from JSON file
def load_button_coordinates(json_file):
    with open(json_file, "r") as f:
        return json.load(f)

# Check if a button is pressed based on mouse coordinates
def is_button_pressed(button, x, y):
    return button["top_left"]["x"] < x < button["bottom_right"]["x"] and \
           button["top_left"]["y"] < y < button["bottom_right"]["y"]

# Load images and scale them to fit the Pygame window
def load_images(folder_path, window_width, window_height):
    images = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image = pygame.image.load(os.path.join(folder_path, filename))
            scaled_image = pygame.transform.scale(image, (window_width, window_height))
            images.append((filename, scaled_image))
    return images

# Evaluate game logic
def evaluate_game(button_coordinates_data, image_folder, window_width, window_height):
    # Set up Pygame window
    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()

    # Load images and scale them
    image_dict = load_images(image_folder, window_width, window_height)
    current_image_index = 0
    total_images = len(image_dict)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                image_file = image_dict[current_image_index][0]
                if image_file in button_coordinates_data:
                    for button in button_coordinates_data[image_file]:
                        if is_button_pressed(button, x, y):
                            print("Button clicked:",current_image_index, button)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Previous image
                    current_image_index = (current_image_index - 1) % total_images
                elif event.key == pygame.K_RIGHT:  # Next image
                    current_image_index = (current_image_index + 1) % total_images

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw current image on the screen
        current_image = image_dict[current_image_index][1]
        screen.blit(current_image, (0, 0))

        pygame.display.flip()
        clock.tick(60)  # Limit frame rate to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    json_filename = "button_coordinates.json"
    image_folder = "images"
    window_width = 1080
    window_height = 720

    button_coordinates_data = load_button_coordinates(json_filename)
    evaluate_game(button_coordinates_data, image_folder, window_width, window_height)
