###################################
## Isabelle's Routes
###################################
## Add routes for Isabelle here.
##

define isabelle = Character("Isabelle", color="#4046e0")

# TODO: update image with isabelle sprites once they're available.
image isabelle_img:
    "gui/character_select/anoki.png"
    # The anoki sprite is too big for the screen, so it is scaled.
    zoom 0.25
    yoffset 200

label IsabelleMalik:
    jump MalikIsabelle
    return

label IsabelleAshlie:
    isabelle "TODO add Isabelle and Ashlie's route here for demo"
    return
