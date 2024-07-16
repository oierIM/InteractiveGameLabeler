# InteractiveGameLabeler

## 0. Requirements

A requirements.txt file is generated to download dependencies with ease. You can use virtualenv to create a environmets with the dependencies.

* Virtualenv env
* source env/bin/activate

## 1. Labeler

### 1.0 Overview

The Interactive Game Labeler is a user-friendly program designed to assist in the labeling of buttons on game screens for subsequent use in creating evaluators for user performance. This program allows users to label the locations of buttons by executing and clicking directly on the displayed game screens. The labeled information is then saved in a JSON file for further analysis.

### 1.1 Usage

    - Upon running labeler.py, use the LEFT and RIGHT arrow keys to navigate through the game screens.

    - Click the TOP-LEFT CORNER of a button to mark its starting point and KEEP IT CLICKED.

    - UNCLICK at the BOTTOM-RIGHT CORNER of the same button to complete the labeling process.

    - Repeat the process for all buttons on the current game screen.

    - Use the LEFT and RIGHT arrow keys to navigate through different game screens and label buttons accordingly.

    - Close the program when you have completed labeling all buttons.

### 1.2 Output

The labeled button coordinates are saved in a JSON file named button_coordinates.json. This file contains information about each button's top-left and bottom-right coordinates for each game screen.

### 1.3 Notes

    - Ensure that the images in the images folder have the following formats: .png, .jpg, .jpeg, or .gif.

    - The program provides on-screen instructions for ease of use.

    - The labeled information is saved in a structured JSON format.

## 2. Evaluator

### 2.0 Overview

This program loads images from a specified folder and displays them. The program also detects mouse clicks on predefined button areas within each image, which are specified in a JSON file, the one created by using the labeler program above. This way, we are able to know where each player is located in a game at a specific instance.

### 2.1 Usage

    - Prepare the image and button coordinates folder

    - Execute the program and play the game as normal

### 2.2 Notes

    - Make sure the JSON file and image folder are correctly named and placed in the same directory as the script.

    - The program currently supports image files with extensions .png, .jpg, .jpeg, and .gif.

## 3. Server

server.py will run on the produciton server (wordpress). From now, the only purpose of this server is to server as the common host of the button_cordinates.json file. In the future, this server is intended to save and process all information gathered by the users. **This file is intended to be in the same directory as button_cordinates.json**
