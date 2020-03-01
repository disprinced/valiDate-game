﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# probably should also be in italics
define reader = Character("", what_font="gui/fonts/Dosis-Medium.otf")

image bg to_be_continued:
    "endings/to_be_continued.png"

image bg test_background:
    "backgrounds/chick_fil_a.jpg"


### CODE FOR ONE SCREEN AT A TIME
label start:
    scene black
    reader "The sun casts over a cold Jersey City day, the wind isn't blowing as hard as it usually does, but you still find yourself hugging your coat a bit closer to your body to shield yourself from the cold. You duck into the hair salon you have been directed to by a friend. The warm heat of a space heater fills your body the moment you step in."
    reader "You don't have a name, at least not yet. But you do have an interest for poetry and the art of hearing people speak their feelings over the occasional chill hip-hop beat."
    reader "The room is dark, all lights pointed towards the area in the far back that sort of looks like a makeshift stage. The room is full of faces you've never seen before, faces so warm yet distraught? Did you just walk into a cult?"
    reader "You decide to sit yourself in the corner, pulling out your phone to text one of your friends, maybe they will help you in your time of need."
    reader "Who will you text?"

    call screen a_char_select_screen(None)
    $ char1 = _return

    scene black
    $ intro = character_structs[char1]['intro']
    if "sprite" in character_structs[char1]:
        $ image_path = character_structs[char1]["sprite"]
        image s2:
            image_path

        show s2 with pixellate:
            zoom 0.2
            yoffset 200

    reader "[intro]"

    call screen a_char_select_screen(_return) with fade
    $ char2 = _return

    if renpy.has_label(char1 + char2):
        $renpy.call(char1 + char2)
        return
    else:
        $renpy.call("unimplemented",char1, char2)
        return
    return


label start2:
    call screen a_char_select_screen(None)
    $ char1 = _return
    call screen a_char_select_screen(_return)
    $ char2 = _return

    if renpy.has_label(char1 + char2):
        $renpy.call(char1 + char2)
        return
    else:
        $renpy.call("unimplemented",char1, char2)
        return
    return

label unimplemented(char1, char2):
    scene bg to_be_continued
    show text "[char1] and [char2]'s route hasn't been implemented/written yet!"
    window hide
    pause
    return
