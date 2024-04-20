import os
import sys

# import function that sorts a string based on character density
from char_density import char_density_sort

# import from asset folder
from assets import menu_dict

# import linked list
from node import LinkedImage

# Import an image processing tool
from PIL import Image as PImage

# import custom image files
from tkinter import filedialog
from tkinter import *


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

    # popup request to select jpg file
    @staticmethod
    def import_file():
        root = Tk()
        root.filename = filedialog.askopenfilename(
            initialdir="/",
            title="Select file",
            filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")),
        )
        return root.filename

    # convert filename image to pixel matrix
    def get_image(self, ext_filename="images/img_6.jpg"):
        self.filename = ext_filename
        img = PImage.open(self.filename)
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
    def user_input(input_string=""):
        usr_input = None
        while not usr_input:
            usr_input = input(input_string)
        return usr_input

    # draw menu from menu_dict file
    def ascii_menu(self):
        for key, value in menu_dict.menu.items():
            print(" {} ) for {}".format(key, value[0]))

        self.input = self.user_input("User ASCII characters: ")

    # check input for menu values
    def menu_function(self):
        if len(self.input) <= 1:
            if self.input[0].upper() in menu_dict.menu:
                self.input = self.input[0].upper()
                print(self.input)
                if self.input == "Q":
                    Action.quit()
                elif self.input == "N":
                    main()
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
    custom_image = SelectImage.import_file()
    image.get_image(custom_image)

    while True:
        image_size = UserInput.user_input("Character Width: ")
        if image_size.isnumeric():
            image_size = int(image_size)
            break

    image.image_resize(image_size)

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


if __name__ == "__main__":
    main()
else:
    print("Image is being processed")


"""



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
