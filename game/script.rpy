# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    import random
#    achievement.register("test", steam="test123")
#    achievement.Sync()
    renpy.music.register_channel("theme_music", "music", loop=True, tight=True)
    achievement.steam_position = "top right"

# probably should also be in italics
define reader = Character("", what_font="gui/fonts/Dosis-Medium.otf")
define unknown =  Character("?????", what_font="gui/fonts/Dosis-Medium.otf")


define audio.bad_end = "audio/030120_vtg_badend.mp3"
define audio.good_end = "audio/030120_vtg_badend.mp3"

image bg to_be_continued:
    "endings/to_be_continued.png"

image bg test_background:
    "backgrounds/chick_fil_a.jpg"

image bg demo_over:
    "endings/buyvalidate.png"

define prelude_movies = [
    "gui/main_menu/prelude_example_a.webm",
    "gui/main_menu/prelude_example_b.webm",
    "gui/main_menu/prelude_example_c.webm",
    "gui/main_menu/prelude_example_d.webm",
]
image prelude_test = Movie(play=prelude_movies, channel="movie_channel", loop=True,size=(1920, 1080), xpos=0, ypos=0, xanchor=0, yanchor=0)

#image movie_background = Movie(play="gui/main_menu/prelude.webm", size=(1920, 1080), xpos=0, ypos=0, xanchor=0, yanchor=0)

define demo = False

label splashscreen:
    $ quick_menu = False
    python:
        renpy.random.shuffle(prelude_movies)

    #call screen prelude()
    show prelude_test with dissolve

    reader "The sun shines out over a cold Jersey City day. The wind isn’t blowing as hard as it usually does, but you still find yourself hugging your coat a bit closer to your body to shield yourself from the cold."
    reader "Hurrying yourself along, you duck into a hair salon your friend pointed you towards, and the warmth of a space heater fills your body the moment you step in."
    reader "The room is dark, all lights pointed towards the area in the far back that sort of looks like a makeshift stage. It’s full of faces you’ve never seen before -- they look so warm, yet so distraught? Did you just walk into a cult?"
    reader "You decide to sit yourself in the corner, pulling out your phone to text one of your friends, hoping one can help you in your time of need."
    reader "Who will you text?"

    hide prelude_test
    show black with dissolve

    return

### CODE FOR ONE SCREEN AT A TIME
label start:

    stop music fadeout 1.0

    play theme_music "audio/022320_vtg_charsel.mp3"

    #$ renpy.profile_screen(_("first_character_select_screen"), show=True, update=True, time=True, debug=True)
    jump select_screen
    return

label select_screen:
    call screen first_character_select_screen()

    $ char1 = _return

    scene black
    $ intro = character_structs[char1]['intro']
    # if "sprite" in character_structs[char1]:
    #     $ image_path = character_structs[char1]["sprite"]
    #     image s2:
    #         image_path
    #
    #     show s2 with pixellate:
    #         zoom 0.2
    #         yoffset 200

    reader "[intro]"

    call screen second_character_select_screen(_return) with fade
    $ char2 = _return
    $ quick_menu = True

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

label demo_over:
    scene bg demo_over
    window hide
    pause
    return
