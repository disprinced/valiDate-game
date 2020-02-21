###################################
## Isabelle's Routes
###################################
## Add routes for Isabelle here.
##

define isabelle = Character("Isabelle", color="#4046e0")

# TODO: update image with isabelle sprites once they're available.
image isabelle happy:
    "sprites/anoki_happy.png"
    # The anoki sprite is too big for the screen, so it is scaled.
    zoom 0.5
    yoffset 200

# TODO: update image with isabelle sprites once they're available.
image isabelle annoyed:
    "sprites/anoki_annoyed.png"
    # The anoki sprite is too big for the screen, so it is scaled.
    zoom 0.5
    yoffset 200

label IsabelleMalik:
    jump MalikIsabelle
    return

label IsabelleAshlie:
    isabelle "TODO add Isabelle and Ashlie's route here for demo"
    return
