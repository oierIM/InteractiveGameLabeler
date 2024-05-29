import json

json_filename = "button_coordinates.json"

class Button:
    def __init__(self, t, b, image_file, type_of_button=0):
        self.tx = t[0]
        self.ty = t[1]
        self.bx = b[0]
        self.by = b[1]
        self.type_of_button = type_of_button
        self.func = []  # List of functions that the button fulfills according to our internal documentation
        self.image_file = image_file
        self.button_dict = {
            "top_left": {"x": self.tx, "y": self.ty},
            "bottom_right": {"x": self.bx, "y": self.by},
            "type_of_button": self.type_of_button
        }

    def save_json(self, json_file="button_coordinates.json"):
        # Read current buttons
        with open(json_file, "r") as f:
            button_coordinates_data = json.load(f)

        if not self.image_file in button_coordinates_data:
            button_coordinates_data[self.image_file] = []
        button_coordinates_data[self.image_file].append(self.button_dict)

        with open(json_file, "w") as json_file:
            json.dump(button_coordinates_data, json_file)

