import pygame
import json

pygame.init()

# kargatu botoiak jsonetik
def load_button_coordinates(json_file):
    with open(json_file, "r") as f:
        return json.load(f)

# ikusi ea botoi bat klikatu den
def is_button_pressed(button, x, y):
    return button["top_left"]["x"] < x < button["bottom_right"]["x"] and \
           button["top_left"]["y"] < y < button["bottom_right"]["y"]

# main
def evaluate_game(button_coordinates_data):
    # beste programaren pantaila tamaina
    window_width = 1765
    window_height = 993
    screen = pygame.display.set_mode((window_width, window_height))

    pressed_buttons = {image_file: set() for image_file in button_coordinates_data.keys()}

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                image_file = "current_image.jpg"  

                if image_file in button_coordinates_data:
                    for button in button_coordinates_data[image_file]:
                        if is_button_pressed(button, x, y):
                            pressed_buttons[image_file].add(button["button_id"])

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    json_filename = "button_coordinates.json"
    button_coordinates_data = load_button_coordinates(json_filename)
    evaluate_game(button_coordinates_data)