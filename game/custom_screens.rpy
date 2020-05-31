define rainbow_order = [
# 'Emhari',
 #'Bigs',
# 'Yolanda',
# 'Rocky',
# 'Alonzo',
 'Isabelle',
 'Anoki',
 'Arihi',
#'Catherine',
 #'Inaya',
 'Ashlie',
 'Malik']

define character_structs = {
    "Malik": {
        "hue": 335,
        "color": "#A30748",
        "demo_routes": ['Isabelle', 'Anoki', 'Arihi'],
        "sprite_pos": (154, 52),
        "select_sprite": ["casual1", "confused"],
        "intro": "Failed rap career aside, this man still owes you a free chicken sandwich. Maybe you should hit him up to see if you can cash in on that."
    },
    "Ashlie": {
        "hue": 320,
        "color": "#E650B4",
        "demo_routes": ['Isabelle'],
        "sprite_pos": (214, 153),
        "select_sprite": ["normal", "sly"],
        "intro": "New Jersey’s number one twitch streamer and she can hardly keep a relationship. Or a friendship for that matter. Maybe you should check on her?"
    },
    # add Inaya
    "Catherine": {
        "hue": 270,
        "color": "#4D0099",
        "sprite_pos": (133, 35),
        "select_sprite": ["neutral", "ng_neutral"],
        "intro": "Your favorite fashionista is probably entirely too busy talking shit about whatever the Kardashians wore to reply to you. Maybe you caught her in a good mood."
    },
    "Arihi": {
        "hue": 215,
        "color": "#002B66",
        "demo_routes": ['Malik'],
        "sprite_pos": (203, 109),
        "select_sprite": ["arms_neutral", "special"],
        "intro": "You know he has a habit to try to fix everyone, being a therapist and all. But has he really tried to put that on his partners?"
    },
    "Anoki": {
        "hue": 175,
        "color": "#39E5D7",
        "demo_routes": ['Malik'],
        "sprite_pos": (94, 203),
        "select_sprite": ["casual", "special"],
        "intro": "The last time you spoke to them you got into a heated argument about the importance of elf ears in an elf cosplay. You wonder if they brought that fight to their new partner?"
    },
    "Isabelle": {
        "hue": 150,
        "color": "#22E584",
        "demo_routes": ['Malik', 'Ashlie'],
        "sprite_pos": (2, 81),
        "select_sprite": ["neutral", "special"],
        "intro": "You miss the sweet sound of Hamilton in your ear, you wonder how she’s been doing with that one person she was talking about the last time you spoke."
    },
    "Alonzo": {
        "hue": 80,
        "color": "#6B8E23",
        "sprite_pos": (76, 146),
        "select_sprite": ["default", "camera"],
        "intro": "You wonder how long it’ll take to get a response from Alonzo, you know his fuckboy tendencies often lead him to forgetting to reply to a text from an old friend."
    },
    "Rocky": {
        "hue": 56,
        "sprite_pos": (132, 38),
        "color": "#F6E700",
        "select_sprite": ["happy", "neutral"],
        "intro": "You wonder if he got his controlling nature under control. You remember it wrecking the last relationships he had."
    },
    "Yolanda": {
        "hue": 40,
        "color": "#F2A711",
        "sprite_pos": (143, 127),
        "select_sprite": ["neutral", "special"],
        "intro": "You probably caught her in the middle of a hair appointment, even though she typically is sweet enough to remind you of that."
    },
    # add Bigs
    "Emhari": {
        "hue": 6,
        "color": "#CB4335",
        "sprite_pos": (224, 48),
        "select_sprite": ["neutral", "suggestive"],
        "intro": "You never understood why he needed 7 different weddings rings despite only wanting to marry one person. Maybe he finally found the one?"
    },
}

define character_list = rainbow_order

# character select screen constants

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.custom_button_width = None
define gui.custom_button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.custom_button_borders = Borders(4, 4, 4, 4)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.custom_button_tile = False
define gui.custom_button_color = "#fff"

## The font used by the button.
define gui.custom_button_text_font = gui.interface_text_font

## The size of the text used by the button.
define gui.custom_button_text_size = gui.interface_text_size

define gui.back_button_width = 90
define gui.back_button_height = 90

define gui.text_button_color = "#fff"

define sprite_not_found = Image(im.MatrixColor("sprites/Anoki/anoki_annoyed.png",
    im.matrix.desaturate()))

define no_second_character = Image("gui/splits/bg_cs2_dark.png")
define no_first_character = Image("gui/flattened_character_select/bg_null.png")

default first_character = ""
default hovered_variable = first_character
default second_character = ""
default second_hovered_variable = second_character
image i_luv_mice = Fixed(Solid("F00", xysize=(150, 50)), Solid("FFF", xysize=(100, 50)), xysize=(150, 50))

init python:
    print ("in init")
    renpy.audio.music.register_channel("movie_channel", renpy.config.movie_mixer, loop=True, stop_on_mute=False, movie=True, framedrop=False)
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

    CENTER_AT = (400, 400)
    char_time = 6.0
    i = 0
    tim = 0.0
    def char_transition(st, at, char):
        global i, tim
        val = character_structs[char]
        char_lower = char.lower()
        d = Image("sprites/%s/%s_std_%s.png" %
            (char_lower, char_lower, val['select_sprite'][i]))
        tim += 0.1
        blah = abs(math.sin((tim % char_time) / char_time * 2 * math.pi))
        if round(blah, 2) == 1.0:
            tim = char_time / 2
            i = (i + 1) % 2
            return d, char_time
        return Transform(d, alpha=blah), 0.1

    def shadow_transition(st, at, char):
        global i, tim
        val = character_structs[char]
        char_lower = char.lower()
        d = Image("sprites/%s/%s_std_%s.png" %
            (char_lower, char_lower, val['select_sprite'][i]))
        d = im.FactorScale(val['sprite'], 1.08, bilinear=True)
        d = AlphaMask(Solid(val['color']), d)
        tim += 0.1
        blah = abs(math.sin((tim % char_time) / char_time * 2 * math.pi))
        if round(blah, 2) == 1.0:
            tim = char_time / 2
            i = (i + 1) % 2
            return d, char_time
        return Transform(d, alpha=blah), 0.1

    def char_transition2(st, at, char):
        val = character_structs[char]
        char_lower = char.lower()
        i = int(st/ char_time * 2) % len(val['select_sprite'])
        d = Image("sprites/%s/%s_std_%s.png" %
            (char_lower, char_lower, val['select_sprite'][i]))
        blah = abs(math.sin((st % char_time) / char_time * 2 * math.pi))
        return Transform(d, alpha=blah), 0.1

    for char, val in character_structs.iteritems():
        char_lower = char.lower()
        val['bg'] = Image("gui/first_character_select/bg_%s_full.png" % char_lower)
        val['name_title'] = Image("gui/first_character_select/bg_%s_text.png" % char_lower)
        val['sprite_moving'] = DynamicDisplayable(char_transition, char=char)
        val['sprite'] = Image("sprites/%s/%s_std_%s.png" %
            (char_lower, char_lower, val['select_sprite'][0]))
        val['left_sprite'] = Image("gui/splits/ds_%s_L.png" % (char_lower))
        val['right_sprite'] = Image("gui/splits/ds_%s_R.png" % (char_lower))

        if 'flip' in val:
            val['sprite'] = im.Flip(val['sprite'], horizontal=True)
        val['shadow'] = im.FactorScale(val['sprite'], 1.08, bilinear=True)
        val['shadow'] = AlphaMask(Solid(val['color']), val['shadow'])

        phone_sprite = "gui/character_select/cs1_%s.png" % (char)
        style.select_icon_button[char].background = \
            Image(phone_sprite)
        style.select_icon_button[char].hover_background = \
            Image("gui/character_select/cs1_%s_hover.png" % (char))
        style.select_icon_button[char].selected_idle_background = \
            im.MatrixColor("gui/character_select/cs1_%s_hover.png" % (char), im.matrix.desaturate())
        style.select_icon_button[char].insensitive_background = \
             im.MatrixColor(phone_sprite, im.matrix.desaturate())

        style.phone_icon_button[char].background = \
            Image("gui/contacts/ct_%s.png" % (char_lower))
        style.phone_icon_button[char].hover_background = \
            Image("gui/contacts/ct_%s_hover.png" % (char_lower))
        style.phone_icon_button[char].selected_idle_background = \
            Image("gui/contacts/ct_%s_select.png" % (char_lower))

        style.qsave_button[char].background = \
            im.MatrixColor("gui/dialoglog/button_qsave.png", custom_hue_shifter(val['hue']))
        style.qsave_button[char].hover_background = \
            im.MatrixColor("gui/dialoglog/button_qsave_hover.png", custom_hue_shifter(val['hue']))

        style.qload_button[char].background = \
            im.MatrixColor("gui/dialoglog/button_qload.png", custom_hue_shifter(val['hue']))
        style.qload_button[char].hover_background = \
            im.MatrixColor("gui/dialoglog/button_qload_hover.png", custom_hue_shifter(val['hue']))

        style.story_back_button[char].background = \
            im.MatrixColor("gui/dialoglog/button_back.png", custom_hue_shifter(val['hue']))
        style.story_back_button[char].hover_background = \
            im.MatrixColor("gui/dialoglog/button_back_hover.png", custom_hue_shifter(val['hue']))

        style.history_button[char].background = \
            im.MatrixColor("gui/dialoglog/button_history.png", custom_hue_shifter(val['hue']))
        style.history_button[char].hover_background = \
            im.MatrixColor("gui/dialoglog/button_history_hover.png", custom_hue_shifter(val['hue']))

        style.skip_button[char].background = \
            im.MatrixColor("gui/dialoglog/button_skip.png", custom_hue_shifter(val['hue']))
        style.skip_button[char].hover_background = \
            im.MatrixColor("gui/dialoglog/button_skip_hover.png", custom_hue_shifter(val['hue']))

        style.auto_button[char].background = \
            im.MatrixColor("gui/dialoglog/button_auto.png", custom_hue_shifter(val['hue']))
        style.auto_button[char].hover_background = \
            im.MatrixColor("gui/dialoglog/button_auto_hover.png", custom_hue_shifter(val['hue']))
        style.auto_button[char].selected_background = \
            im.MatrixColor("gui/dialoglog/button_auto_active.png", custom_hue_shifter(val['hue']))

        style.save_button[char].background = \
            im.MatrixColor("gui/dialoglog/button_save.png", custom_hue_shifter(val['hue']))
        style.save_button[char].hover_background = \
            im.MatrixColor("gui/dialoglog/button_save_hover.png", custom_hue_shifter(val['hue']))

        style.preference_button[char].background = \
            im.MatrixColor("gui/dialoglog/button_preferences.png", custom_hue_shifter(val['hue']))
        style.preference_button[char].hover_background = \
            im.MatrixColor("gui/dialoglog/button_preferences_hover.png", custom_hue_shifter(val['hue']))
        style.text_button[char].xpadding = 50
        style.text_button[char].ypadding = 20
        style.text_button_text[char].color = "#fff"
        style.text_button[char].background = \
            im.MatrixColor("gui/character_select/button_bg.png",
            custom_hue_shifter(val['hue']))
        style.text_button[char].hover_background = \
            im.MatrixColor("gui/character_select/button_bg_hover.png",
            custom_hue_shifter(val['hue']))
        style.back_button[char].background = \
            im.MatrixColor("gui/character_select/button_goback.png",
            custom_hue_shifter(val['hue']))
        style.back_button[char].hover_background = \
            im.MatrixColor("gui/character_select/button_goback_hover.png",
            custom_hue_shifter(val['hue']))

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.custom_button_text_xalign = 0.0

screen character_hover(character):
    style_prefix "char_hover"
    python:
        if character == "":
            bg = no_first_character
        else:
            info = character_structs[character]
            bg = info['bg']
            name_title = info['name_title']
            shadow = info['shadow']
            sprite_moving = info['sprite_moving']
            sprite = info['sprite']
            x, y = info['sprite_pos']
            shadow_x = x - 50
            shadow_y = y + 10
    add bg

    if character != "":
        add shadow:
            pos (shadow_x, shadow_y)
        add sprite_moving:
            pos(x, y)
        add name_title:
            pos(540, 0)

    hbox:
        style_prefix "custom"
        pos (756, 960)

        if (character == ""):
            textbutton _("CANCEL") action [SetVariable("first_character", ""), MainMenu()] style style.text_button["Malik"]
        else:
            textbutton _("CANCEL") action [SetVariable("first_character", ""), MainMenu()] style style.text_button[character]
            textbutton _("CONFIRM") action Return(character) style style.text_button[character]

    button action MainMenu() style style.back_button[character]:
        pos (193, 960)
        xsize 90
        ysize 90
    transclude

screen first_character_select_screen():
    use character_hover(hovered_variable)
    $ quick_menu = False

    hbox:
        xalign 0.5
        yalign 0.8
        for i, char in enumerate(rainbow_order):
            $ has_demo_route = 'demo_routes' in character_structs[char]
            textbutton _(" "):
                yoffset -20
                ysize 180
                action [ToggleVariable("first_character", true_value=char, false_value=""), SetVariable("hovered_variable", char)]
                hovered SetVariable("hovered_variable", char)
                unhovered SetVariable("hovered_variable", first_character)
                style style.select_icon_button[char]


screen second_character_hover(character):
    python:
        if character == "":
            right_sprite = no_second_character
        else:
            right_sprite = character_structs[character]['right_sprite']
    add right_sprite

screen second_character_select_screen(first_char):

    style_prefix "char_hover"
    use second_character_hover(second_hovered_variable)
    python:
        info = character_structs[first_char]
        left_sprite = info['left_sprite']
        if 'demo_routes' in info:
            routes = info['demo_routes']
        else:
            routes = rainbow_order
    add left_sprite

    hbox:
        style_prefix "custom"
        pos (796, 731)

        textbutton _("NAH  "):
            action [SetVariable("first_character", first_char),
                    SetVariable("hovered_variable", first_char),
                    SetVariable("second_character", ""),
                    SetVariable("second_hovered_variable", ""),
                    Jump("select_screen")]
            style style.text_button[first_character]
        textbutton _("SEND"):
            action Return(second_character)
            style style.text_button[first_character]

    vpgrid:
        pos (796, 240)
        xminimum 400
        cols 3
        yspacing 0
        xspacing -5
        style_prefix "select_icon"
        $ i = 0
        for char in routes:
            if char != first_char:
                textbutton _(""):
                    action [ToggleVariable("second_character", true_value=char, false_value=""), SetVariable("second_hovered_variable", char)]
                    hovered SetVariable("second_hovered_variable", char)
                    unhovered SetVariable("second_hovered_variable", second_character)
                    style style.phone_icon_button[char]
                    xminimum 110
                    yminimum 120

style empty_frame is empty

style main_menu_frame:
    xsize 420
    yfill True


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
