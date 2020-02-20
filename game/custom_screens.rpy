
## Character Select Screen ###################################
##
## Displays character selection
##

screen character_select_screen:
    tag gameplay

    style_prefix "malik"

    use game_menu(_("Character Selection"), scroll="viewport", yinitial=1.0):
        vbox:
            box_wrap True
            label _("Character Select")
            hbox:
                # Add more vboxes for each character.
                # TODO: Change textbutton to clickable image.
                vbox:
                    style_prefix "radio"
                    textbutton _("Malik") action Call("malik_route_start")

                vbox:
                    style_prefix "radio"
                    textbutton _("Isabelle") action Call("isabelle_route_start")
