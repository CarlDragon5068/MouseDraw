import numpy as np
from PIL import Image
import pyautogui #pyautogui controls the mouse of the system
import time

#Return the image as an array
def load_image(image_path):
    img = Image.open(image_path).convert("L")
    return np.array(img)

#Sets the pixels tending towards black to black and those tending towards white to white
def process_image_to_bits(array):
    bit_image = []

    for row in array:
        row_bits = ""
        for pixel in row:
            row_bits += "0" if pixel >= 128 else "1"
        streak_start = 0

        for i in range(len(row_bits)):
            if i == len(row_bits) - 1 or row_bits[i] != row_bits[i + 1]:
                streak_length = i - streak_start + 1

                if row[streak_start] == "1": 

                else:
                    
                streak_start = i + 1
    return bit_image


def draw_from_bits(bit_image, start_x, start_y, pixel_size=1, drawing_speed=0.001):
    pass

def main():
    source_image = r"image/m.png"

    array = load_image(source_image)
    bit_image = process_image_to_bits(array)

    print("Starting in 3 seconds...")
    time.sleep(3)

    start_x, start_y = pyautogui.position() #set starting position to that of our cursor

    start_time = time.time()
    # draw_from_bits(bit_image, start_x, start_y, pixel_size=0.5, drawing_speed=0.001)
    print(f"Drawing completed in {time.time() - start_time:.2f} seconds")

    pyautogui.mouseUp()


if __name__ == "__main__":
    main()
0
