###################################
## Isabelle constants
###################################
## Add constants related to Isabelle here
##

define isabelle = Character("Isabelle", color="#4046e0")

image isabelle default1:
    "sprites/isabelle/SPRITEDEFAULT-1.png"
    zoom 0.25
    yoffset 200

image isabelle default2:
    "sprites/isabelle/SPRITEDEFAULT-2.png"
    zoom 0.25
    yoffset 200

image isabelle angry:
    "sprites/isabelle/SPRITEANGRY.png"
    zoom 0.25
    yoffset 200

image isabelle condescending:
    "sprites/isabelle/SPRITEcondescending.png"
    zoom 0.25
    yoffset 200

image isabelle sad:
    "sprites/isabelle/SPRITESAD.png"
    zoom 0.25
    yoffset 200

image isabelle upset:
    "sprites/isabelle/SPRITEUPSET.png"
    # The anoki sprite is too big for the screen, so it is scaled.
    zoom 0.25
    yoffset 200


label IsabelleAshlie:
    isabelle "TODO add Isabelle and Ashlie's route here for demo"
    return
