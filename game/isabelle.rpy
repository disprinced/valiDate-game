###################################
## Isabelle's Routes
###################################
## Add routes for Isabelle here.
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

image bg red_lobster:
    "backgrounds/vtg_ppl_b_dither.png"

image bg car:
    "backgrounds/vtg_geo_combo.png"

image bg isa_house:
    "backgrounds/vtg_gta_combo.png"

label IsabelleAshlie:
    isabelle "TODO add Isabelle and Ashlie's route here for demo"
    return
