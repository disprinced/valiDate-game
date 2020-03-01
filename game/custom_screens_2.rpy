###################################
## Character Select Screen
###################################
## Displays character selection
##

# CODE FOR TWO SCREENS AT A TIME
# label start:
#     call screen two_select_screens
#     if renpy.has_label(_return):
#         $renpy.call(_return)
#     else:
#         $renpy.call("unimplemented", _return)
#     return
#
# label unimplemented(char):
#     scene bg to_be_continued
#     show text "[char]'s route hasn't been implemented/written yet!"
#     window hide
#     pause
#     return

init python:
    first_character = ""
    second_character = ""

screen two_select_screens:

    add cs.background
    fixed:
        pos(170, 174)
        vbox:
            label _("Character Select 1")
            use a_char_select_screen_2("first_character"):
                    label _("[first_character]")

    fixed:
        pos (1236, 199)
        vbox:
            label _("Character Select 2")
            use a_char_select_screen_2("second_character"):
                    label _("[second_character]")

    hbox:
        style_prefix "custom"
        pos (708, 928)
        #pos (703, 980)
        vbox:
            if (first_character == "") and (second_character == ""):
                textbutton _("select two characters!")
            elif (first_character == "") or (second_character == ""):
                textbutton _("select one more character!")
            elif first_character == second_character:
                textbutton _("no self dates (yet) ;)")
            else:
                textbutton _("selected!") action Return(first_character + second_character)
        vbox:
            textbutton _("CANCEL") action MainMenu()


screen a_char_select_screen_2(selected_char_name):
    modal False
    #tag gameplay

    style_prefix "empty"
    frame:
        has vbox
        box_wrap True

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
                                    textbutton _("[char] ") action ToggleVariable(selected_char_name, true_value=char, false_value="") style style.select_icon_button[char]
                            $elem_index += 1
        transclude
