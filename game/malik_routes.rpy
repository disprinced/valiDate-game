###################################
## Malik's Routes
###################################
## Add routes for Malik here.
##

define malik = Character("Malik", color="#8a41ba")

# TODO: update image with isabelle sprites once they're available.
image malik_img:
    "gui/character_select/anoki.png"
    # The anoki sprite is too big for the screen, so it is scaled.
    zoom 0.25
    yoffset 200

label MalikIsabelle:
    reader "It’s around 12:30 PM when you come out of your back office to make sure people aren’t fucking around in the front."
    reader "Business per usual, the bar has its usual day drinkers, while the restaurant is still at top tier. It has a 3 star rating for a reason."
    reader "A woman around your age walks into the main entrance. A bit unsure of what side she wanted to go to. You catch her eye, and her loud physique fills in the room with the feeling of a high school musical."
    reader "And that isn’t a good thing."

    scene bg test_background
    show isabelle happy:
        xalign 0.0
        linear 0.5 xalign 0.5
    isabelle "So I’m thinking that I want a drown down some dry biscuits with a shot of tequila?"
    malik "Nice to know you don’t drink much."

    show isabelle annoyed

    isabelle "Yeah, not much of a drinker. I dabble more in the COOL drug scene. Nothing crazy! Just the shit growing from the earth."
    return

label MalikAnoki:
    scene bg test_background
    malik "TODO add Malik and Anoki's route here for demo"
    return

label MalikArihi:
    scene bg test_background
    malik "TODO add Malik and Arihi's route here for demo"
    return

# TODO contemplate moving these into [char]_routes.rpy files when created
label AnokiMalik:
    jump MalikAnoki
    return

label ArihiMalik:
    jump MalikArihi
    return
