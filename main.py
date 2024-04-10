import os
import sys

# import function that sorts a string on character density
from char_density import char_density_sort

# import linked list
from node import LinkedImage

# Import an image processing tool
from PIL import Image


# clear screen
def cls():
    os.system("cls" if os.name == "nt" else "clear")


# returns the relative path of the asset folder
def asset_path(filename):
    script_dir = os.path.dirname(__file__)
    rel_path = "assets/" + filename
    return os.path.join(script_dir, rel_path)


# adds the image pixel matrix to the Image Linked List
def image_to_matrix(image, width, height):
    image_list = LinkedImage(width, height)
    for y in range(height):
        for x in range(width):
            # insert last pixel first, so it lands at the back of the linked list
            image_list.insert_beginning(image[(width * height) - (y * width) - (x + 1)])
    return image_list


# conversts (averages) the RGB Image Linked List into a monochrome Image Linked List
def make_bnw(image):
    width = image.width
    height = image.height
    image_list = LinkedImage(width, height)
    for n in image:
        r, g, b = n.value
        sum_rgb = r + g + b
        average_rgb = round(sum_rgb / 3)
        image_list.insert_beginning(average_rgb)
    return image_list


def make_ascii(image, string):
    width = image.width
    height = image.height
    image_list = LinkedImage(width, height)
    ascii_string = char_density_sort(string)
    ascii_length = len(ascii_string)
    for n in image:
        i = round(ascii_length * n.value / 256)
        # insert the char in ascii_string in index value * character spacing
        image_list.insert_beginning(ascii_string[i - 1] * 2)
    return image_list


def print_img(image):
    cls()
    width = image.width
    height = image.height
    print("\n image width = {}, image height = {} \n".format(width, height))
    width_count = 1
    for n in image.get_all_nodes():
        print(n.value, end="")
        if width_count == width:
            print(" ")
            width_count = 0
        width_count += 1
    return None


def peek(image):
    count = 5
    for n in image.get_all_nodes():
        print(n.value)
        count -= 1
        if count == 0:
            print(" ")
            return None


def user_input():
    usr_input = None
    while not usr_input:
        usr_input = input("input: ")
    return usr_input


def ascii_menu():
    print("\n 1 for default long string")
    print(" 2 for default short string")
    print(" Anything else to create your own input")
    print(" Q to quit")
    usr_input = user_input()
    cls()

    if usr_input.upper() == "Q":
        sys.exit(0)
    elif usr_input == "1":
        return "  `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi\{{}C{}}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    elif usr_input == "2":
        return " .:-=+*#%@"
    else:
        return usr_input


def main():
    cls()
    img = Image.open(asset_path("img_5.jpg"))
    width, height = img.size
    pixel_matrix = img.getdata()

    colour_matrix = image_to_matrix(pixel_matrix, width, height)
    bnw_matrix = make_bnw(colour_matrix)
    while True:
        ascii_string = ascii_menu()
        ascii_matrix = make_ascii(bnw_matrix, ascii_string)
        print_img(ascii_matrix)


if __name__ == "__main__":
    main()
else:
    print("Image is being imported")


"""

    # different ascii strings
    # ascii_string = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi\{C\}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    # ascii_string = ("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,\"^`'.")
    # ascii_string = " .:-=+*#%@"
    # ascii_string = "`.:~=+o*%8&#@O"
    # ascii_string = "-=+*"
    # ascii_string = ""
    
"""
