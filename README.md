# InteractiveGameLabeler

## Overview

The Interactive Game Labeler is a user-friendly program designed to assist in the labeling of buttons on game screens for subsequent use in creating evaluators for user performance. This program allows users to label the locations of buttons by executing and clicking directly on the displayed game screens. The labeled information is then saved in a JSON file for further analysis.

## Usage

    - Upon running the script, use the LEFT and RIGHT arrow keys to navigate through the game screens.

    - Click the TOP-LEFT CORNER of a button to mark its starting point and KEEP IT CLICKED.

    - UNCLICK at the BOTTOM-RIGHT CORNER of the same button to complete the labeling process.

    - Repeat the process for all buttons on the current game screen.

    - Use the LEFT and RIGHT arrow keys to navigate through different game screens and label buttons accordingly.

    - Close the program when you have completed labeling all buttons.

## Output

The labeled button coordinates are saved in a JSON file named button_coordinates.json. This file contains information about each button's top-left and bottom-right coordinates for each game screen.

## Notes

    - Ensure that the images in the images folder have the following formats: .png, .jpg, .jpeg, or .gif.

    - The program provides on-screen instructions for ease of use.

    - The labeled information is saved in a structured JSON format.
