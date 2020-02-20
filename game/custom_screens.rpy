###################################
## Character Select Screen
###################################
## Displays character selection
##
define character_list = ["Malik", "Isabelle", "Anoki", "Ashlie", "Arihi"]

screen first_character_select_screen:
    tag gameplay

    use game_menu(_("Character Selection"), scroll="viewport", yinitial=1.0):
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
        scroll="viewport", yinitial=1.0):
        vbox:
            hbox:
                style_prefix "radio"
                xfill True
                box_wrap True
                label _(character + " Character Select ")
            hbox:
                style_prefix "radio"
                # Add more vboxes for each character.
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
