import os
import sys
import os


user_path = str(os.path.expanduser('~'))
pykitty_dir = os.path.realpath(__file__).replace("utils/functions.py",'')


fonts = ["Cascadia Code", "FiraCode","UbuntuMono NerdFont"]
themes_path = user_path + "/.config/kitty/themes" 
config_path = user_path + "/.config/kitty"
man_path = pykitty_dir + "/README"



def set_theme(new_theme,n_theme_path):
    g = open(n_theme_path, "r")
    theme_lines = g.readlines()


    with open(config_path + "/kitty.conf", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if lines[i].startswith("#Kitty theme"):
                config_index = i
    with open(config_path + "/kitty.conf", "w") as f:
        for i in range(len(lines)):
            if i < config_index:
                f.write(lines[i])
            elif i == config_index:
                f.write("#Kitty theme\n")

    config = open(config_path + "/kitty.conf", "a")
    config.write("\n#" + str(new_theme) + "\n")

    for n in range(len(theme_lines)):
        config.write(theme_lines[n])

    config.close()
    g.close()

    with open( pykitty_dir + "/fav.txt", "r") as f:
        fav_lines = f.readlines()
    with open("fav.txt", "w") as f:
        for i in range(len(fav_lines)):
            if fav_lines[i].startswith(new_theme):
                fav_index = int(fav_lines[i].split()[1]) + 1
                f.write(fav_lines[i].split()[0] + " " + str(fav_index) + "\n")
            else:
                    f.write(fav_lines[i])


def favorites(items):
    if items == "themes":
        theme_dict = {}

        with open( user_path + "/Pykitty/CLI/fav.txt", "r") as f:
            fav_lines = f.readlines()
            for n in range(len(fav_lines)):
                name = fav_lines[n].split()[0]
                index = int(fav_lines[n].split()[1])
                theme_dict[str(name)] = index
        elements = sorted(theme_dict, key=theme_dict.get, reverse=True)[:5]
        for n in range(len(elements)):
            print(elements[n], " "*(20 - len(elements[n])) + "times used:", theme_dict[elements[n]])

def set_font(new_font):
    if new_font not in fonts:
        print("Font not found")
        return

    else:
        with open(config_path + "/kitty.conf", "r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if lines[i].startswith("font_family"):
                    config_index = i
        with open(config_path + "/kitty.conf", "w") as f:
            for i in range(len(lines)):
                if i != config_index:
                    f.write(lines[i])
                elif i == config_index:
                    f.write("font_family " + str(new_font) + "\n")
        

def set_font_size(new_font_size):

    with open(config_path + "/kitty.conf", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if lines[i].startswith("font_size"):
                config_index = i
    with open(config_path + "/kitty.conf", "w") as f:
        for i in range(len(lines)):
            if i != config_index:
                f.write(lines[i])
            elif i == config_index:
                f.write("font_size " + str(new_font_size) + "\n")


def print_manual():
    with open(man_path, "r") as f:
        man_lines = f.readlines()
        for n in range(len(man_lines)):
            print(man_lines[n])

def set_margin(n):
    with open(config_path + "/kitty.conf", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if lines[i].startswith("window_margin_width"):
                config_index = i
    with open(config_path + "/kitty.conf", "w") as f:
        for i in range(len(lines)):
            if i != config_index:
                f.write(lines[i])
            elif i == config_index:
                f.write("window_margin_width " + str(n) + "\n")
