import os
from PIL import Image

# returns the relative path of the asset folder


def asset_path(filename):
    script_dir = os.path.dirname(__file__)
    rel_path = "assets/" + filename
    return os.path.join(script_dir, rel_path)


def image_to_matrix(image, width, height):
    matrix = []
    for x in range(width):
        matrix.append([])
        for y in range(height):
            matrix[x].append(image[y * width + x])
    return matrix


def make_bnw(image):
    bnw_matrix = []
    for x in range(len(image[0])):
        bnw_matrix.append([])
        for y in range(len(image)):
            sum_rgb = image[y][x][0] + image[y][x][1] + image[y][x][2]
            average_pixel = round(sum_rgb / 3)
            bnw_matrix[x].append(average_pixel)
    return bnw_matrix


def make_ascii(image):
    ascii_matrix = []
    # ascii_string = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi\{C\}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    # ascii_string = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,\"^`'."
    # ascii_string = " .:-=+*#%@"
    # ascii_string = "`.:~=+o*%8&#@O"
    ascii_string = "-+/=*"

    ascii_length = len(ascii_string)
    for x in range(len(image[0])):
        ascii_matrix.append([])
        for y in range(len(image)):
            i = round(ascii_length * image[y][x] / 256)
            ascii_matrix[x].append(ascii_string[i - 1] * 2)
    return ascii_matrix


def print_img(image):
    for x in range(len(image[0])):
        for y in range(len(image)):
            print(image[y][x], end="")
        print("")


img = Image.open(asset_path('img_5.jpg'))
width, height = img.size

pixel_matrix = img.getdata()
colour_matrix = image_to_matrix(pixel_matrix, width, height)
bnw_matrix = make_bnw(colour_matrix)
ascii_matrix = make_ascii(bnw_matrix)

print_img(ascii_matrix)
