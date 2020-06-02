###################################
## Malik's Routes
###################################
## Add routes for Malik here.
##


label MalikIsabelle:
    scene bg bobeyes
    show malik casual 1
#Malik in the middle
    reader "There's a lot in this world that you can't do on your own. You find yourself in front of your Bopeyes around 10 a.m. It's dark outside, despite the fact that it's the middle of June. The clouds overshadow your store as you fumble for your keys. "
    reader "It looks like it might rain, which already puts a damper in your mood. You hate the rain, you always find yourself thinking of your wife -- or, more accurately,  your ex-wife. The wife who made you into the person you are now. "
    reader "Or, well --  at least according to your latest mixtape."
    reader "Shit. You forgot to bring your duffle bag full of CDs today. You typically slip them into every order, but you guess you can show off your bars another day."
    reader "You pull out your phone, notifications dry as always. "
    reader "Well, not dry. You've got plenty of texts, you just can't be bothered to answer right now. They're mostly from people you'll probably cry about not getting a response from later. "
    reader "What can you say, it's the Sagittarius in you."

    show isabelle neutral:
        xalign 0.0
        linear 0.5 xalign 0.5
    isabelle "So I’m thinking that I want a drown down some dry biscuits with a shot of tequila?"
    malik "Nice to know you don’t drink much."

    show isabelle annoyed

    isabelle "Yeah, not much of a drinker. I dabble more in the COOL drug scene. Nothing crazy! Just the shit growing from the earth."

    scene bg to_be_continued
    window hide
    pause
    return
