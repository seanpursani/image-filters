"""
This program creates an image which has the patch copied 6 times (in 2 rows and 3 columns) 
where each patch gets re-colored. This effect is inspired by some of Andy Warhol’s paintings. 
"""

import random
from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = r'C:\Users\seanp\Software Dev\PYTHON PROJECTS\CODEINPLACE PROJECTS\CodeInPlace\assign_3\images'


def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    make_canvas(final_image, N_ROWS, N_COLS)
    final_image.show()


def make_canvas(final_image, n_rows, n_cols):
    start_y = 0
    for y in range(N_ROWS):
        start_x = 0
        for x in range(N_COLS):
            patch = get_colour()
            put_patch(final_image, start_x, start_y, patch)
            start_x += PATCH_SIZE
        start_y += PATCH_SIZE


def get_colour():
    red_scale = random_num()
    green_scale = random_num()
    blue_scale = random_num()
    patch = make_recolored_patch(red_scale, green_scale, blue_scale)
    return patch

# return a random floating-point number between 0.5-2.0
def random_num():
    return random.uniform(0.5, 2.0)


def put_patch(final_image, start_x, start_y, patch):
    for x in range(patch.width):
        for y in range(patch.height):
            pixel = patch.get_pixel(x, y)
            final_image.set_pixel((x + start_x), (y + start_y), pixel)

# recolours image by taking in red, green and blue values as arguments
def make_recolored_patch(red_scale, green_scale, blue_scale):
    patch = SimpleImage(PATCH_NAME)
    for pix in patch:
        pix.red *= red_scale
        pix.green *= green_scale
        pix.blue *= blue_scale
    return patch


if __name__ == '__main__':
    main()