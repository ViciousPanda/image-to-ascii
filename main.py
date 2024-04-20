import os
import sys

# import function that sorts a string on character density
from char_density import char_density_sort

# import from asset folder
from assets import menu_dict

# import linked list
from node import LinkedImage

# Import an image processing tool
from PIL import Image


# select, resize and add the image to the linked list
class SelectImage:

    def __init__(self):
        self.filename = None
        self.max_width = 0
        self.max_height = 0
        self.current_width = 0
        self.current_height = 0
        self.colour = True
        self.pixel_matrix = None

    # returns the relative path of the asset folder
    def asset_path(self, filename):
        script_dir = os.path.dirname(__file__)
        rel_path = "images/" + filename
        return os.path.join(script_dir, rel_path)

    # convert filename image to pixel matrix
    def get_image(self, ext_filename="img_6.jpg"):
        self.filename = ext_filename
        filename_path = self.asset_path(self.filename)
        img = Image.open(filename_path)
        self.current_width, self.current_height = img.size
        self.max_width = self.current_width
        self.max_height = self.current_height
        self.pixel_matrix = img.getdata()

    # resizes image to the provided character column width
    def image_resize(self, character_columns):
        # request a fullsized image
        self.get_image(self.filename)
        if self.max_width > character_columns:
            self.current_width = character_columns
            self.current_height = round(
                self.max_height * character_columns / self.max_width
            )
        else:
            self.current_width = self.max_width
            self.current_height = self.max_height
        new_size = (self.current_width, self.current_height)
        self.pixel_matrix = self.pixel_matrix.resize(new_size)

    # add pixel matrix to a linked list
    def image_to_ll(self):
        image_list = LinkedImage(self.current_width, self.current_height)
        for y in range(self.current_height):
            for x in range(self.current_width):
                # insert last pixel first, so it lands at the back of the linked list
                image_list.insert_beginning(
                    self.pixel_matrix[
                        (self.current_width * self.current_height)
                        - (y * self.current_width)
                        - (x + 1)
                    ]
                )
        return image_list


class Action:
    def __init__(self, image):
        self.image = image
        self.converted_image = None
        self.width = image.width
        self.height = image.height

    # exit the program
    @staticmethod
    def quit():
        sys.exit(0)

    # clear the console
    @staticmethod
    def cls():
        os.system("cls" if os.name == "nt" else "clear")

    # peek the first 5 lines
    @staticmethod
    def peek(image):
        count = 5
        for n in image.get_all_nodes():
            print(n.value)
            count -= 1
            if count == 0:
                print(" ")
                return None

    # conversts (averages) the RGB Image Linked List into a monochrome Image Linked List
    def make_bnw(self):
        image_list = LinkedImage(self.width, self.height)
        for n in self.image:
            r, g, b = n.value
            sum_rgb = r + g + b
            average_rgb = round(sum_rgb / 3)
            image_list.insert_beginning(average_rgb)
        self.image = image_list

    # replaces pixel light values with ascii characters from strings
    def make_ascii(self, string=" .:-=+*#%@"):
        image_list = LinkedImage(self.width, self.height)
        self.string = string
        ascii_string = char_density_sort(self.string)
        ascii_length = len(ascii_string)
        for n in self.image:
            i = round(ascii_length * n.value / 256)
            # insert the char in ascii_string in index value * character spacing
            image_list.insert_beginning(ascii_string[i - 1] * 2)
        self.converted_image = image_list

    # print the ascii image in the console
    def print_ascii(self):
        self.cls()
        print(
            "\n image width = {}, image height = {} \n".format(self.width, self.height)
        )
        width_count = 1
        for n in self.converted_image.get_all_nodes():
            print(n.value, end="")
            if width_count == self.width:
                print(" ")
                width_count = 0
            width_count += 1
        return None


class UserInput:

    def __init_(self):
        self.input = ""

    # ask user for custom input
    @staticmethod
    def user_input():
        usr_input = None
        while not usr_input:
            usr_input = input("custom ASCII key: ")
        return usr_input

    # draw menu from menu_dict file
    def ascii_menu(self):
        for key, value in menu_dict.menu.items():
            print(" {} ) for {}".format(key, value[0]))

        self.input = self.user_input()

    # check input for menu values
    def menu_function(self):
        if len(self.input) <= 1:
            if self.input[0].upper() in menu_dict.menu:
                self.input = self.input[0].upper()
                print(self.input)
                if self.input == "Q":
                    Action.quit()
                else:
                    print(menu_dict.menu[self.input][1])
                    return menu_dict.menu[self.input][1]
            else:
                print("Wrong menu option")
                self.ascii_menu()
        else:
            return self.input


def main():
    Action.cls()

    # init
    image = SelectImage()
    image.get_image()
    image_ll = Action(image.image_to_ll())
    image_ll.make_bnw()
    image_ll.make_ascii()
    image_ll.print_ascii()

    while True:
        user = UserInput()
        user.ascii_menu()
        ascii_string = user.menu_function()
        image_ll.make_ascii(ascii_string)
        image_ll.print_ascii()

    # image.image_resize(70)

    """
    img = Image.open(asset_path("img_6.jpg"))
    width, height = img.size
    pixel_matrix = img.getdata()

    colour_matrix = image_to_matrix(pixel_matrix, width, height, 80)
    bnw_matrix = make_bnw(colour_matrix)
    while True:
        ascii_string = ascii_menu()
        ascii_matrix = make_ascii(bnw_matrix, ascii_string)
        print_img(ascii_matrix)
    """


if __name__ == "__main__":
    main()
else:
    print("Image is being processed")


"""

    # different ascii strings
    # ascii_string = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi\{C\}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    # ascii_string = ("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,\"^`'.")
    # ascii_string = " .:-=+*#%@"
    # ascii_string = "`.:~=+o*%8&#@O"
    # ascii_string = "-=+*"
    # ascii_string = ""
    

class select image


class make image
    default
    resize
    push into LL
    establish Black and White
    assign ascii / invert

class action
    quit
    invert
    size
    colour/bnw
    ascii string

class ask user
    initiate
    select image / default
    draw as default
    
    loop
    ask input
    redraw
    
    print
    


"""
