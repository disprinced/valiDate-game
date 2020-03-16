define rainbow_order = [
    'Emhari',
    #'Bigs',
    'Yolanda',
    'Rocky',
    'Alonzo',
    'Isabelle',
    'Anoki',
    'Arihi',
    'Catherine',
    #'Inaya',
    'Ashlie',
    'Malik']

define character_structs = {
    "Malik": {
        "hue": 335,
        "intro": "Failed rap career aside, this man still owes you a free chicken sandwich. Maybe you should hit him up to see if you can cash in on that."
    },
    "Ashlie": {
        "hue": 320,
        "intro": "New Jersey’s number one twitch streamer and she can hardly keep a relationship. Or a friendship for that matter. Maybe you should check on her?"
    },
    # add Inaya
    "Catherine": {
        "hue": 270,
        "intro": "Your favorite fashionista is probably entirely too busy talking shit about whatever the Kardashians wore to reply to you. Maybe you caught her in a good mood."
    },
    "Arihi": {
        "hue": 215,
        "intro": "You know he has a habit to try to fix everyone, being a therapist and all. But has he really tried to put that on his partners?"
    },
    "Anoki": {
        "hue": 175,
        "sprite": "sprites/anoki_happy.png",
        "intro": "The last time you spoke to them you got into a heated argument about the importance of elf ears in an elf cosplay. You wonder if they brought that fight to their new partner?"
    },
    "Isabelle": {
        "hue": 150,
        "sprite": "sprites/isabelle/SPRITEDEFAULT-1.png",
        "intro": "You miss the sweet sound of Hamilton in your ear, you wonder how she’s been doing with that one person she was talking about the last time you spoke."
    },
    "Alonzo": {
        "hue": 80,
        "intro": "You wonder how long it’ll take to get a response from Alonzo, you know his fuckboy tendencies often lead him to forgetting to reply to a text from an old friend."
    },
    "Rocky": {
        "hue": 56,
        "intro": "You wonder if he got his controlling nature under control. You remember it wrecking the last relationships he had."
    },
    "Yolanda": {
        "hue": 40,
        "intro": "You probably caught her in the middle of a hair appointment, even though she typically is sweet enough to remind you of that."
    },
    # add Bigs
    "Emhari": {
        "hue": 6,
        "intro": "You never understood why he needed 7 different weddings rings despite only wanting to marry one person. Maybe he finally found the one?"
    },
}

define character_list = rainbow_order
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
    import math
    def custom_hue_shifter(hue):
        h = hue * math.pi / 180
        x = math.cos(h)
        y = math.sin(h)
        return im.matrix(
            2.0/3 * x + 1.0/3,
            -1.0/3 * x - 0.57735026919 * y + 1.0 / 3,
            -1.0/3 * x + 0.57735026919 * y + 1.0 / 3,
            0, 0,
            -1.0/3 * x + 0.57735026919 * y + 1.0 / 3,
            2.0/3 * x + 1.0/3,
            -1.0/3 * x - 0.57735026919 * y + 1.0 / 3,
            0, 0,
            -1.0/3 * x - 0.57735026919 * y + 1.0 / 3,
            -1.0/3 * x + 0.57735026919 * y + 1.0 / 3,
            2.0/3 * x + 1.0/3,
            0, 0,
            0, 0, 0, 1, 0,
            0, 0, 0, 0, 1)

    for char, values in character_structs.iteritems():
        style.select_icon_button[char].background = \
            im.MatrixColor(
        "gui/buttons_defaults/button_chamfer_phonesku10_0.png",
        #im.matrix.hue(values['hue']))
        custom_hue_shifter(values['hue']))
        style.select_icon_button[values['hue']].hover_background = \
            im.MatrixColor(
        "gui/buttons_defaults/button_chamfer_phonesku10_0_hover.png",
        #im.matrix.hue(values['hue']))
        custom_hue_shifter(values['hue']))
        style.select_icon_button[values['hue']].insensitive_background = \
            im.MatrixColor(
        "gui/buttons_defaults/button_chamfer_phonesku10_0_hover.png",
        im.matrix.desaturate())
        style.select_icon_button[char].selected_background = \
            im.MatrixColor(
        "gui/buttons_defaults/button_chamfer_phonesku10_0_onclick.png",
        #im.matrix.hue(values['hue']))
        custom_hue_shifter(values['hue']))



## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.custom_button_text_xalign = 0.0

#define anoki_sprite = "sprites/anoki_happy.png"
#define isabelle_sprite = "sprites/isabelle/SPRITEDEFAULT-1.png"
define sprite_not_found = im.MatrixColor("sprites/anoki_annoyed.png",
    im.matrix.desaturate())

define image_path = im.MatrixColor("sprites/anoki_annoyed.png",
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
    if character is not None:
        if "sprite" in character_structs[character]:
            $ sprite = character_structs[character]["sprite"]
            add sprite:
                zoom 0.6
                xoffset -300
        else:
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
            textbutton _("BACK") action Jump("start")
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
