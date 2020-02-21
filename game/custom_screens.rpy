###################################
## Character Select Screen
###################################
## Displays character selection
##
define character_list = ["Malik", "Isabelle", "Anoki", "Ashlie", "Arihi"]

# character select screen constants
# this will probably be diff for every character
define cs.background = "backgrounds/charsel_anoki.png"

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

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.custom_button_text_xalign = 0.0

screen test_screen:
    tag gameplay
    add cs.background
    frame:
        vbox:
            hbox:
                style_prefix "radio"
                xfill True
                box_wrap True
                label _("Character Select")

            hbox:
                style_prefix "radio"
                # TODO: Change textbutton to clickable image.
                vpgrid:
                    cols 4
                    spacing 50
                    for char in character_list:
                        textbutton _("[char] ") action Return(char)
            hbox:
                style_prefix "custom"

style custom_label is pref_label
style custom_label_text is pref_label_text
style custom_button is gui_button
style custom_button_text is gui_button_text
style custom_vbox is pref_vbox

style custom_button:
    properties gui.button_properties("custom_button")
    foreground "gui/buttons_defaults_/button_chamfer_3x1_0_[prefix_]foreground.png"
    background "gui/buttons_defaults_/button_chamfer_3x1_0_[prefix_]background.png"

style custom_button_text:
    properties gui.button_text_properties("custom_button")


screen first_character_select_screen:
    tag gameplay

    use game_menu(_("Character Selection"), scroll="viewport"):
        vbox:
            hbox:
                style_prefix "radio"
                xfill True
                box_wrap True
                label _("Character Select")

            hbox:
                style_prefix "radio"
                # TODO: Change textbutton to clickable image.
                vpgrid:
                    cols 4
                    spacing 50
                    for char in character_list:
                        textbutton _("[char] ") action Return(char)

###################################
## Second Character Select Screen
###################################
## Choose the character for initial character to interact with.
##
screen second_character_select_screen(character):
    tag gameplay

    use game_menu(_(character + " Character Selection"),
        scroll="viewport"):
        vbox:
            hbox:
                style_prefix "radio"
                xfill True
                box_wrap True
                label _(character + " Character Select ")
            hbox:
                style_prefix "radio"
                # TODO: Change textbutton to clickable image.
                vpgrid:
                    cols 4
                    spacing 50
                    for char in character_list:
                        if char != character:
                            if renpy.has_label(character + char):
                                textbutton _("[char] ") action Call(character + char)
                            else:
                                textbutton _("[char] ") action Call("unimplemented", character, char)
