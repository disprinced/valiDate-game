# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define reader = Character("")

image bg to_be_continued:
    "endings/to_be_continued.png"

image bg test_background:
    "backgrounds/chick_fil_a.jpg"

### CODE FOR ONE SCREEN AT A TIME
label start:
    call screen a_char_select_screen(None)
    $ char1 = _return
    call screen a_char_select_screen(_return)
    $ char2 = _return

    if renpy.has_label(char1 + char2):
        $renpy.call(char1 + char2)
    else:
        $renpy.call("unimplemented",char1, char2)
    return
label unimplemented(char1, char2):
    scene bg to_be_continued
    show text "[char1] and [char2]'s route hasn't been implemented/written yet!"
    window hide
    pause
    return
