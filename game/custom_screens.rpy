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
        "left_pos": (1129, 52),
        "select_sprite": ["casual1", "confused"],
        "phone_sprite": ["casual1", "confused"],
        "intro": "Failed rap career aside, this man still owes you a free chicken sandwich. Maybe you should hit him up to see if you can cash in on that."
    },
    "Ashlie": {
        "hue": 320,
        "color": "#E650B4",
        "demo_routes": ['Isabelle'],
        "sprite_pos": (214, 153),
        "left_pos": (1189, 153),
        "select_sprite": ["normal", "sly"],
        "phone_sprite": ["normal", "sly"],
        "intro": "New Jersey’s number one twitch streamer and she can hardly keep a relationship. Or a friendship for that matter. Maybe you should check on her?"
    },
    # add Inaya
    "Catherine": {
        "hue": 270,
        "color": "#4D0099",
        "sprite_pos": (133, 35),
        "left_pos": (1108, 35),
        "select_sprite": ["neutral", "ng_neutral"],
        "phone_sprite": ["neutral", "ng_neutral"],
        "intro": "Your favorite fashionista is probably entirely too busy talking shit about whatever the Kardashians wore to reply to you. Maybe you caught her in a good mood."
    },
    "Arihi": {
        "hue": 215,
        "color": "#002B66",
        "demo_routes": ['Malik'],
        "sprite_pos": (203, 109),
        "left_pos": (1178, 109),
        "select_sprite": ["arms_neutral", "special_test"],
        "phone_sprite": ["phone_texting", "phone_calling"],
        "intro": "You know he has a habit to try to fix everyone, being a therapist and all. But has he really tried to put that on his partners?"
    },
    "Anoki": {
        "hue": 175,
        "color": "#39E5D7",
        "demo_routes": ['Malik'],
        "sprite_pos": (94, 203),
        "left_pos": (1069, 203),
        "select_sprite": ["casual", "special"],
        "phone_sprite": ["phone_texting", "phone_talking"],
        "intro": "The last time you spoke to them you got into a heated argument about the importance of elf ears in an elf cosplay. You wonder if they brought that fight to their new partner?"
    },
    "Isabelle": {
        "hue": 150,
        "color": "#22E584",
        "demo_routes": ['Malik', 'Ashlie'],
        "sprite_pos": (2, 81),
        "left_pos": (977, 81),
        "select_sprite": ["neutral", "special"],
        "phone_sprite": ["phone_texting", "phone_calling"],
        "intro": "You miss the sweet sound of Hamilton in your ear, you wonder how she’s been doing with that one person she was talking about the last time you spoke."
    },
    "Alonzo": {
        "hue": 80,
        "color": "#6B8E23",
        "sprite_pos": (76, 146),
        "left_pos": (1051, 146),
        "select_sprite": ["default", "camera"],
        "phone_sprite": ["default", "camera"],
        "intro": "You wonder how long it’ll take to get a response from Alonzo, you know his fuckboy tendencies often lead him to forgetting to reply to a text from an old friend."
    },
    "Rocky": {
        "hue": 56,
        "sprite_pos": (132, 38),
        "left_pos": (1107, 38),
        "color": "#F6E700",
        "select_sprite": ["happy", "neutral"],
        "phone_sprite": ["happy", "neutral"],
        "intro": "You wonder if he got his controlling nature under control. You remember it wrecking the last relationships he had."
    },
    "Yolanda": {
        "hue": 40,
        "color": "#F2A711",
        "sprite_pos": (143, 127),
        "left_pos": (1118, 127),
        "select_sprite": ["neutral", "special"],
        "phone_sprite": ["phone_texting", "phone_calling"],
        "intro": "You probably caught her in the middle of a hair appointment, even though she typically is sweet enough to remind you of that."
    },
    # add Bigs
    "Emhari": {
        "hue": 6,
        "color": "#CB4335",
        "sprite_pos": (224, 48),
        "left_pos": (1199, 48),
        "select_sprite": ["neutral", "suggestive"],
        "phone_sprite": ["neutral", "suggestive"],
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
default c2_state = "default"

define bluh = StateMachineDisplayable(
"bluh",        # An unique name for this displayable
"default",            # The initial state for this displayable
# A mapping of "state": displayable
{
  "default": sprite_not_found
}
)

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

    def make_composite(char, file, index):
        val = character_structs[char]
        char_lower = char.lower()
        d = Image("sprites/%s/%s_std_%s.png" %
        (char_lower, char_lower, val[file][index]))
        d1 = im.FactorScale(d, 1.08, bilinear=True)
        d1 = AlphaMask(Solid(val['color']), d1)
        return Composite((1920, 1080),
            (0, 0), d1,
            (75, 18), d)

    def turn_off_calling(char, routes):
        for c in routes:
            if c != char:
                character_structs[c]['c2_moving'].set_state("default")
    char_time = 6.0
    i = 0
    tim = 0.0

    def shadow_transition(st, at, char):
        global i, tim
        val = character_structs[char]
        char_lower = char.lower()
        if (char == 'Arihi' and i == 1):
            d = Image("sprites/%s/%s_std_%s.png" %
                (char_lower, char_lower, val['select_sprite'][i]),
                offset=(-200, 100))
            d1 = im.FactorScale(d, 1.08, bilinear=True)
            d1 = AlphaMask(Solid(val['color']), d1,
                offset=(-200, 100))
        else:
            d = Image("sprites/%s/%s_std_%s.png" %
                (char_lower, char_lower, val['select_sprite'][i]))
            d1 = im.FactorScale(d, 1.08, bilinear=True)
            d1 = AlphaMask(Solid(val['color']), d1)
        result = Composite((1920, 1080),
            (0, 0), d1,
            (75, 18), d)
        tim += 0.1
        blah = abs(math.sin((tim % char_time) / char_time * 2 * math.pi))
        if round(blah, 2) == 1.0:
            tim = char_time / 2
            i = (i + 1) % 2
            return result, char_time
        return Transform(result, alpha=blah), 0.1


    # class SwitchImageAction(Action):
    #     def __init__(self, char):
    #         self.char_val = character_structs[char]
    #         self.char_lower = char.lower()
    #         self.texting_img = self.make_composite(self.char_val['phone_sprite'][0])
    #         self.phone_img = self.make_composite(self.char_val['phone_sprite'][1])
    #
    #     def make_composite(self, file):
    #         d = Image("sprites/%s/%s_std_%s.png" %
    #         (self.char_lower, self.char_lower, file))
    #         d1 = im.FactorScale(d, 1.08, bilinear=True)
    #         d1 = AlphaMask(Solid(self.char_val['color']), d1)
    #         return Composite((1920, 1080),
    #             (0, 0), d1,
    #             (75, 18), d)
    #
    #     def periodic(self, st):

    alpha_value = 0
    def cs2_animation(st, at, char):
        global tim, alpha_value
        val = character_structs[char]
        char_lower = char.lower()
        tim += 0.1
        if second_character != "" and second_character == second_hovered_variable:
            if alpha_value == 0:
                tim = 0.1

            d = Image("sprites/%s/%s_std_%s.png" %
            (char_lower, char_lower, val['phone_sprite'][1]))
            d1 = im.FactorScale(d, 1.08, bilinear=True)
            d1 = AlphaMask(Solid(val['color']), d1)
            result = Composite((1920, 1080),
                (0, 0), d1,
                (75, 18), d)

            alpha_value = abs(math.sin((tim % char_time) / char_time * 2 * math.pi))
            if round(alpha_value, 2) == 1.0:
                tim = char_time / 2
                return result, None
            return Transform(result, alpha=alpha_value), 0.1
        else:
            #d = Image("sprites/%s/%s_std_%s.png" %
            #    (char_lower, char_lower, val['select_sprite'][0]))
            d = Image("sprites/%s/%s_std_%s.png" % (char_lower, char_lower, val['phone_sprite'][0]))
            d1 = im.FactorScale(d, 1.08, bilinear=True)
            d1 = AlphaMask(Solid(val['color']), d1)
            result = Composite((1920, 1080),
                (0, 0), d1,
                (75, 18), d)

            x = 60 if tim >= 1.0 else tim * 60
            return Transform(result, xpos=x), 0.1


        tim += 0.1
        blah = abs(math.sin((tim % char_time) / char_time * 2 * math.pi))
        if round(blah, 2) == 1.0:
            tim = char_time / 2
            i = (i + 1) % 2
            return result, char_time
        return Transform(result, alpha=blah), 0.1



    for char, val in character_structs.iteritems():
        char_lower = char.lower()

        # First character select assets
        val['bg'] = Image("gui/first_character_select/bg_%s_full.png" % char_lower)
        val['name_title'] = Image("gui/first_character_select/bg_%s_text.png" % char_lower)
        val['sprite'] = Image("sprites/%s/%s_std_%s.png" %
            (char_lower, char_lower, val['select_sprite'][0]))
        val['moving'] = DynamicDisplayable(shadow_transition, char=char)

        # Second character select assets.
        val['left_background'] = Image("gui/splits/L_cs2_%s_bg.png" % char_lower)
        val['right_background'] = Image("gui/splits/R_cs2_%s_bg.png" % char_lower)
        val['second_text'] = Image("gui/splits/cs2_%s_text.png" % char_lower)
        val['c2_state'] = "default"
        val['c2_moving'] = StateMachineDisplayable(
        "%s_c2_moving" % char,        # An unique name for this displayable
        "default",            # The initial state for this displayable
        # A mapping of "state": displayable
        {
          "default": make_composite(char, "phone_sprite", 0),
          "calling": make_composite(char, "phone_sprite", 1)
        }
      )
      #DynamicDisplayable(cs2_animation, char=char)

        val['phone_background'] = \
            im.MatrixColor("gui/splits/cs2_phone.png", custom_hue_shifter(val['hue']))

        if 'flip' in val:
            val['sprite'] = im.Flip(val['sprite'], horizontal=True)

        phone_sprite = "gui/character_select/cs1_%s.png" % (char)
        style.select_icon_button[char].background = \
            Image(phone_sprite)
        style.select_icon_button[char].hover_background = \
            Image("gui/character_select/cs1_%s_hover.png" % (char))
        style.select_icon_button[char].selected_idle_background = \
            Image("gui/character_select/cs1_%s_active.png" % (char))
        style.select_icon_button[char].selected_hover_background = \
            Image("gui/character_select/cs1_%s_active.png" % (char))
        style.select_icon_button[char].insensitive_background = \
             im.MatrixColor(phone_sprite, im.matrix.desaturate())

        style.contact_button[char].background = \
            Image("gui/contacts/cs2_%s_button.png" % char_lower)
        style.contact_button[char].hover_background = \
            Image("gui/contacts/cs2_%s_button_hover.png" % char_lower)
        style.contact_button[char].selected_idle_background = \
            Image("gui/contacts/cs2_%s_button_active.png" % char_lower)

        style.nah_button[char].background = \
            im.MatrixColor("gui/splits/cs2_phone_button_nah.png",
            custom_hue_shifter(val['hue']))
        style.nah_button[char].hover_background = \
            im.MatrixColor("gui/splits/cs2_phone_button_nah_hover.png",
            custom_hue_shifter(val['hue']))
        style.send_button[char].background = \
            im.MatrixColor("gui/splits/cs2_phone_button_send.png",
            custom_hue_shifter(val['hue']))
        style.send_button[char].hover_background = \
            im.MatrixColor("gui/splits/cs2_phone_button_send_hover.png",
            custom_hue_shifter(val['hue']))
        style.send_button[char].insensitive_background = \
            im.MatrixColor("gui/splits/cs2_phone_button_send.png", im.matrix.desaturate())

        # style.phone_icon_button[char].background = \
        #     Image("gui/contacts/ct_%s.png" % (char_lower))
        # style.phone_icon_button[char].hover_background = \
        #     Image("gui/contacts/ct_%s_hover.png" % (char_lower))
        # style.phone_icon_button[char].selected_idle_background = \
        #     Image("gui/contacts/ct_%s_select.png" % (char_lower))

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
            moving = info['moving']
            sprite = info['sprite']
            x, y = info['sprite_pos']
            x = x -75
            y = y - 18
    add bg

    if character != "":
        add moving:
            pos(x,y)
        add name_title:
            pos(540, 0)

    hbox:
        style_prefix "custom"
        spacing 50
        ypos 950
        xalign 0.5

        if (character == ""):
            textbutton _("CANCEL") action [SetVariable("first_character", ""), MainMenu()] style style.text_button["Malik"]
        else:
            textbutton _("CANCEL") action [SetVariable("first_character", ""), MainMenu()] style style.text_button[character]
            textbutton _("CONFIRM") action Return(character) style style.text_button[character]

    # button action MainMenu() style style.back_button[character]:
    #     pos (193, 960)
    #     xsize 90
    #     ysize 90
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
                style style.select_icon_button[char]
                action [ToggleVariable("first_character", true_value=char, false_value="")]
                hovered SetVariable("hovered_variable", char)
                unhovered SetVariable("hovered_variable", first_character)


screen second_character_hover(character):
    python:
        if character == "":
            right_background = no_second_character
        else:
            info = character_structs[character]
            right_background = info['right_background']
            right_sprite = info['c2_moving']
            right_text = info['second_text']
            x,y = info['left_pos']
            x += 100

    add right_background:
        pos (960, 0)

    if character != "":
        add right_sprite:
            pos(x,y)
        add right_text:
            pos(1200, 600)

screen second_character_select_screen(first_char):

    style_prefix "char_hover"
    use second_character_hover(second_hovered_variable)
    python:
        info = character_structs[first_char]
        left_background = info['left_background']
        left_sprite = info['sprite']
        left_text = info['second_text']
        phone = info['phone_background']
        #left_sprite = info['left_sprite']
        if 'demo_routes' in info:
            routes = info['demo_routes']
        else:
            routes = rainbow_order
        x, y = info['sprite_pos']
        if second_character != "":
            right_sprite = character_structs[second_character]['c2_moving']
        else:
            right_sprite =  bluh

    add left_background
    add left_sprite:
        pos(x,y)
    add left_text:
        pos(120, 600)
    add phone:
        pos(659, 60)

    hbox:
        style_prefix "custom"
        # pos (796, 731)
        #pos (795, 720)
        ypos 720
        xalign 0.5
        textbutton _(" "):
            style style.nah_button[first_char]
            action [SetVariable("first_character", first_char),
                    SetVariable("hovered_variable", first_char),
                    SetVariable("second_character", ""),
                    SetVariable("second_hovered_variable", ""),
                    Jump("select_screen")]

            xminimum 165
            yminimum 90
        if second_character != "":
            textbutton _(" "):
                action If(second_character != "", Return(second_character))
                style style.send_button[first_char]
                xminimum 165
                yminimum 90
        # textbutton _(" "):
        #     action If(second_character != "", Return(second_character))
        #     style style.send_button[first_char]
        #     xminimum 165
        #     yminimum 90

    vbox:
        pos (810, 255)
        for char in routes:
            textbutton _(" "):
                style style.contact_button[char]
                action [ToggleVariable("second_character", true_value=char, false_value=""),
                Function(turn_off_calling,
                char=char,
                routes=routes),
                Function(character_structs[char]['c2_moving'].set_state, new_state="calling", transition=dissolve)
                ]

                hovered SetVariable("second_hovered_variable", char)
                unhovered SetVariable("second_hovered_variable", second_character)
                xminimum 300
                yminimum 75

        # pos (796, 240)
        # xminimum 400
        # cols 3
        # yspacing 0
        # xspacing -5
        # style_prefix "select_icon"
        # $ i = 0
        # for char in routes:
        #     if char != first_char:
        #         textbutton _(""):
        #             action [ToggleVariable("second_character", true_value=char, false_value=""), SetVariable("second_hovered_variable", char)]
        #             hovered SetVariable("second_hovered_variable", char)
        #             unhovered SetVariable("second_hovered_variable", second_character)
        #             style style.phone_icon_button[char]
        #             xminimum 110
        #             yminimum 120

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
