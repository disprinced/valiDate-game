
define character_list = ["Malik", "Isabelle", "Anoki", "Ashlie", "Arihi",
                        "Yolanda", "Rocky", "Alonzo", "Catherine", "Emhari"]
#define character_list = [str(x) for x in range(10)]

# character select screen constants
# this will probably be diff for every character
#define cs.background = "backgrounds/charsel_anoki.png"
define cs.background = "#d6a3b9"

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.custom_button_width = None
define gui.custom_button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.custom_button_borders = Borders(4, 4, 4, 4)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.custom_button_tile = False

## The font used by the button.
define gui.custom_button_text_font = gui.interface_text_font

## The size of the text used by the button.
define gui.custom_button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.custom_button_text_idle_color = gui.idle_small_color
define gui.custom_button_text_hover_color = gui.hover_color
define gui.custom_button_text_selected_color = gui.selected_color
define gui.custom_button_text_insensitive_color = gui.insensitive_color

init python:
    for char in character_list:
        hue = renpy.random.randint(0,360)
        style.select_icon_button[char].background = \
            im.MatrixColor(
        "gui/buttons_defaults/button_chamfer_phonesku10_0.png",
        im.matrix.hue(hue))
        style.select_icon_button[char].hover_background = \
            im.MatrixColor(
        "gui/buttons_defaults/button_chamfer_phonesku10_0_hover.png",
        im.matrix.hue(hue))
        style.select_icon_button[char].insensitive_background = \
            im.MatrixColor(
        "gui/buttons_defaults/button_chamfer_phonesku10_0_hover.png",
        im.matrix.desaturate())
        style.select_icon_button[char].selected_background = \
            im.MatrixColor(
        "gui/buttons_defaults/button_chamfer_phonesku10_0_onclick.png",
        im.matrix.hue(hue))

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.custom_button_text_xalign = 0.0

define anoki_sprite = "sprites/anoki_happy.png"
define sprite_not_found = im.MatrixColor("sprites/anoki_annoyed.png",
    im.matrix.desaturate())
###################################
## Character Select Screen
###################################
## Displays character selection
##
screen a_char_select_screen(character):
    modal True
    tag gameplay
    add cs.background
    if character == "Anoki":
        add anoki_sprite:
            zoom 0.6
            xoffset -300
    elif character is not None:
        add sprite_not_found:
            zoom 0.6
            xoffset -300

    $ char_name = "" if character is None else character

    frame style "empty_frame":
        pos (700, 134)
        text "[char_name]":
            style "main_menu_title"
            size 100

    hbox:
        style_prefix "custom"
        pos (703, 980)
        vbox:
            textbutton _("cancel 2") action MainMenu()
        vbox:
            textbutton _("CANCEL") action MainMenu()

    style_prefix "empty"
    frame:
        has vbox
        if character is None:
            pos (627, 177)
        else:
            pos (1236, 199)
        box_wrap True
        if character is not None:
            label _("Who should [character] go on a date with???")
        else:
            label _("Character Select")
        vbox :
            style_prefix "select_icon"
            $ num_cols = 3
            $ elem_index = 0
            for row in range((len(character_list) / num_cols) + 1):
                hbox:
                    yoffset (-80 * row)
                    if row % 2 == 1:
                        $ num_cols = 4
                        xoffset -80
                    else:
                        $ num_cols = 3
                        xoffset 0
                    for col in range(num_cols):
                        if elem_index < len(character_list):

                            $char = character_list[elem_index]
                            frame xmaximum 160 ymaximum 240 style "empty_frame":
                                # Disable character if already on selected character
                                if character == char:
                                    textbutton _("[char] ") style style.select_icon_button[char]

                                else:
                                    textbutton _("[char] ") action Return(char)  style style.select_icon_button[char]
                            $elem_index += 1

style empty_frame is empty

style main_menu_frame:
    xsize 420
    yfill True


style custom_label is pref_label
style custom_label_text is pref_label_text
style custom_button is gui_button
style custom_button_text is gui_button_text
style custom_vbox is pref_vbox

style custom_button:
    xpadding 50
    ypadding 30
    properties gui.button_properties("custom_button")
    background Frame("gui/buttons_defaults/button_chamfer_3x1_0_background.png")
    hover_background Frame("gui/buttons_defaults/test.png")

style custom_button_text:
    properties gui.button_text_properties("custom_button")


style select_icon_label is pref_label
style select_icon_height is gui_button_height
style select_icon_label_text is pref_label_text
style select_icon_yminimum is gui_button_height
style select_icon_button is gui_button
style select_icon_button_text is gui_button_text
style select_icon_vbox is pref_vbox

style select_icon_button:
    xpadding 50
    ypadding 100
    properties gui.button_properties("select_icon")

style select_icon_button_text:

    properties gui.button_text_properties("custom_button")
