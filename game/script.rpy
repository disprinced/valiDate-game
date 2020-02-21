# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define reader = Character("")

image bg to_be_continued:
    "endings/to_be_continued.png"

image bg test_background:
    "backgrounds/chick_fil_a.jpg"

label start:
    # call screen test_screen
    call screen first_character_select_screen
    call screen second_character_select_screen(_return)
    return

label unimplemented(char1, char2):
    scene bg to_be_continued
    show text "[char1] and [char2]'s route hasn't been implemented/written yet!"
    window hide
    pause
    return
