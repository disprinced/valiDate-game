
image bg isa_bar_gameover:
    "endings/ISAGAMEOVER1.jpg"

image bg isa_malik_rap:
    "endings/ISAGAMEOVER2.jpg"

image bg isa_malik_loser:
    "endings/ISAGAMEOVER3.png"

image bg isa_malik_inside:
    "endings/ISAGAMEOVER4.png"

image bg isa_malik_good:
    "endings/isabelle_end_scene_draft1.png"

label IsabelleMalik:
    scene black
    #play theme_music isabelle_theme

    reader "You aren't sure where you're going as you leave your house. Not really in the mood to deal with public transit or taxis, you walk into the buiser part of your neighborhood with no real destination in mind."
    reader"You don't have to be in the theater until late this afternoon for a dress rehearsal. You love the theater life, but god damn, you are just *not* in the mood to deal with people like yourself -- people who refused to grow out of their theater phase of high school."

    show isabelle neutral:
        xalign 0.0
        linear 0.5 xalign 0.5

    reader "Your name is Isabelle Morrigan, you are 27 years old, and the rumble in your stomach suddenly reminds you that you had ditched the breakfast your abuela made you."
    reader "You should probably get something to eat before you make the walk to the theater. Or maybe you'll see a friend on the way."
    reader  "Your mind is cluttered, you're unsure on where to focus your attention to. For once in your life, you feel yourself being unsure of -- well, yourself. Unsure of what you're doing. Unsure of where your life is headed."
    reader "You don't even realize you're standing in the middle of the sidewalk, spaced out as you run through whatever thoughts were in your head. You snap back to reality when you hear the clearing of a throat behind you and begin to walk towards...somewhere. You're not sure where that somewhere is."
    reader "Do you need a drink? Some food? Both? Can you get both at 11 AM?"
    reader "In a city as big as this? Probably. The city might sleep, but it's too early for an afternoon siesta. "

    hide isabelle with dissolve

    reader "It's half past noon by the time you finally figure out where you want to spend your afternoon and grab that drink you desperately need. Or, maybe the food will be enough to put you back into your usual chipper mood."

    # TODO maybe cycle through bobeyes and bar scene until choice is made.
    reader "You enter the Bopeyes/Bar fusion not too far from the park you were seated at, making sure to close the door quietly behind you so you won't draw too much attention. You don't want your bad mood to become even worse."
    reader "Taking a step forward, you stand in the intersection of the Bopeyes and the bar, contemplating which direction you would rather take."

    menu:
        "Enter the Bopeyes.":
            jump IsaMalikBopeyes
            return
        "Enter the Bar":
            jump IsaMalikBar
            return

    return

label IsaMalikBopeyes:
    scene bg bobeyes with dissolve
    reader "You decide you need food in you more than you need a drink. The growl of your stomach is nearly loud enough for people in passing to hear, and that's embarrassing to say the least."
    show malik distracted with dissolve:
        xalign 0.5

    reader "You haven't felt this hungry in a while. Maybe your bad mood is pushing you to eat for comfort. Either way, you enter the Bopeyes. You take a quick glance over the menu before eyeing the tall man who stood behind one of the registers."
    reader "Wow, this man is... so fucking hot. You find yourself staring longer than you should. Thankfully, he's busy with another customer and isn't paying much attention to you."
    reader "The previously sour mood has dispersed into thin air by now. As you approach his register, you can feel the repressed theater nerd in you rising up full force."

    show malik distracted:
        linear 0.5 xalign 0.75

    show isabelle amused with dissolve:
        xalign 0.0
        linear 0.5 xalign 0.1


    isabelle "So I’m thinking that I want a drown down some dry biscuits with a shot of tequila? "

    show malik distracted
    unknown "Nice to know you don’t drink much."

    reader "That’s a callout -- you really don’t, and when you do, it’s typically something light like a Mac’s hard lemonade or some wine cooler your friend brought to the after parties."


    isabelle "Yeah, not much of a drinker. I dabble more in the *cool* drug scene. Nothing crazy! Just the shit growing from the earth."

    reader "Jesus lord, you're so fucking lame. Maybe you need to stop spending so much time around 12 year olds and more time around your friends."


    show malik casual
    unknown "So what can I get for you? It's Tuesday, we've got a special - 2 wings, fries and a biscuit for $3."

    show isabelle disgust
    isabelle "$3? Damn, that's a steal! At theater camp, they give the counselors a discount but I'm really over those dry sandwiches."

    unknown "I bet they got y'all with those dry ass turkey and ham sandwiches with expired mayo and mustard."

    reader "You make a face of disgust. At least you're not alone with this shitty camp food experience."

    isabelle "I KNEW THE MUSTARD WAS EXPIRED! Mustard isn't supposed to be spicy."

    show malik smug
    unknown "Dijon mustard is spicy."

    isabelle "Really? I can't really handle spicy food. My abuela makes fun of me for it all the time."

    show malik surprised
    unknown "Abuela? Eres Latina?"

    show isabelle surprised
    isabelle "Oh! I don't speak much spanish. I mean I do, but my spanish is pretty ugly so I try not to speak too much of it. Every time I do, people always have something to say."

    reader "You've always been embarrassed by the fact that you can't speak it that well. Mostly because you were the only one in your family who didn't. But, to be fair, it's not your fault that your parents didn't decide to teach you how to speak it until you were 18 -- they even made you take French classes until you were in college."

    show malik amused
    unknown "There isn't any judgement here, I hardly speak English."

    reader "Reassuring, at least he's not judging you like most people do. You assume he's not a Spanish speaker. Even *they* judge you for not knowing how to speak your native tongue -- which doesn't really make sense to you. They can't speak it either, so really, they have no room to judge."
    reader "He points to his name tag, and you notice he's the only person wearing one. Maybe he's important around here?"

    show malik happy
    malik "Name's Malik, manager of this five star establishment."

    reader "One of his co-workers snorts, walking towards the back in an attempt to hide it. Malik doesn't pay it much attention. Instead, he leans forward, resting his elbow on the table and propping his chin up on his hand."
    reader "You find yourself laughing as well. To your surprise, it's your normal laugh, the laugh you have been told fills up a room and causes other people to tune in. Or, you know, at least gets a couple of frowns to turn upside down."

    show isabelle singing
    isabelle "Isabelle, but everyone calls me Isa. And I'm the greeeeatest singer on the east coast!"

    reader "Singing at random times is a hobby of yours. Maybe it's just the theater girl in you. The high note shifts your glasses ever so slightly, and you push them back up the bridge of your nose. You didn't mean to tilt your head back that far."

    show malik casual
    malik "Singing? So like, you do musicals and shit?"

    reader "Your face lights up like a tree in a Christmas card. It's rare for random strangers to ask you about your musical talents. People typically laugh or, in worse cases, give you an eyeroll."
    reader "You don't care for either of those reactions. Honestly, the only person who can ruin your self esteem is yourself -- and sometimes your Abuela if she really pushes your buttons."

    isabelle "YEAH! Musicals! I do musicals! I run theater camps and perform on the weekends at the theater nearby!"

    show malik amused
    malik "Bellacalisus? The one with the giant bird statue in front?"

    isabelle "Yeah, that one! I can't believe you know the name! Most people just call it the bird place."

    show malik smug
    malik "Oh yeah, I performed there a couple times."

    menu:
        "Oh, you’re a performer too? What kind of shows do you do?":
            jump IsaMalikPerform
            return
        "Do you like rap too? I know sooo many rappers, a lot of them are… pretty bad.":
            jump IsaMalikRap
            return
    return

label IsaMalikBar:
    # TODO change to bar scene.
    scene bg bobeyes with dissolve
    reader "You decide you could go for a drink first, maybe grab some overly greasy chicken afterwards to help sober you up before you have to deal with a bunch of elementary school kids messing up the lines they should have memorized a month ago."
    reader "The bar is mostly empty. You take a seat near the bartender, sparking up some conversation after ordering your drink. Maybe you'll go for something light, a Grapefruit Mimosa to keep the day tarte. Whatever the fuck that means - your bartender recommended it to you."
    reader "You sip at your drink as you glance out the window, watching the world pass you by."
    reader "Maybe having a bad day won't kill you. After all, it can be healthy for life to be imperfect every now and then."

    scene bg isa_bar_gameover
    play theme_music bad_end
    window hide
    pause
    return

label IsaMalikPerform:
    show isabelle amused
    isabelle "You're a performer too? OH! What kind of things do you perform?"

    show malik smug
    malik "I rap in my spare time. I'm pretty popping in the neighborhood. They play my stuff like every Saturday night."

    isabelle "Oh shit! I have to listen to your stuff one day, I'm not super into rap, I'm more of a showtunes person. But I'm always willing to try new things!"

    show malik embarrassed
    malik "Oh shit, yeah. Uh."
    show malik casual
    malik "Uh, so I don't have a copy on me today. But, uh. If you give me your number or, snapchat I can send you a link to my soundcloud so you can take a listen."

    show isabelle happy
    isabelle "Oh fuck yes! Here."

    reader "You reach into your bag a bit too fast. A hot guy asking for your number? You're not about to pass up the opportunity. Hell, you're not here to block your own blessings."
    reader "You unlock your phone and hand it over to him."

    show isabelle texting
    isabelle "Save your number and text yourself so you can have mine!"

    show malik casual
    malik "Oh shit, yeah. Sure I will. Hey, order whatever you want. It's on me. I guess you can get a manager's discount. Anything for a future fan."

    show isabelle happy2
    isabelle "Thanks!"


    scene black with fade


    reader "You've got a bit of an internal battle going on as you try to decide whether or not to text him first. Are you being too eager? Is it just your anxiety speaking?"
    reader "Are you having an panic attack?"

    show malik texting:
        xalign 0.75

    malik "hey, its malik from bopeyes, this is isa right"
    malik "or was i just catfished irl"
    malik "catfished irl? that dont make no damn sense lol"

    reader "Okay. Maybe you're overthinking this. It takes you a bit to actually reply -- more specifically, about 20 tries before you finally force yourself to press send."

    show isabelle texting:
        small_y_bounce

    isabelle "OH NO!!!! ITS ME ISA!!!! Sorry i was in the shower."

    reader "You can lie over text. That's what most people do right?"

    show isabelle texting:
        small_y_bounce
    isabelle "oh don't bother with that \"oh without me\" shit, i'm not with it."
    isabelle "ANYWAYS, SEND THAT LINK OVER!"

    malik "[soundcloud.com/malikdegoots]"

    reader "Okay. Music. You listen to music all the time. So why are you so nervous to listen to this? It isn't like this is a voicemail from an ex you've been dying to get away from. It's soundcloud music. Which usually goes hard -- but then again, you did meet this guy at a Bopeyes."
    reader "It actually isn't as bad as you thought it would be. It is actually pretty good. For your standards at least. And you've been told you have pretty high standards when it comes to music."
    reader "You decide to pick some of your favorite lyrics, writing it in your journal so you wouldn't forget."

    show isabelle texting:
        small_y_bounce
    isabelle "i got my daughter my son and my baby mas"
    show isabelle texting:
        small_y_bounce
    isabelle "sittin back and lookin at the sight in awe"
    show isabelle texting:
        small_y_bounce
        small_y_bounce
    isabelle "ON GOD ill punch a n**** in the jaw!"
    show isabelle texting:
        small_y_bounce
    isabelle "and then go back and chill at the spa"

    malik "so you're a rapper now"

    show isabelle texting:
        small_y_bounce
    isabelle "those are your lyrics!!!! I would never say the n word in my music!"
    isabelle "even when we were doing hip hop rap i never said it!"

    malik "yknow i would let you say it around me"

    isabelle "I WOULD NEVER!!!!!"

    reader "You do your fair share of policing when it comes to reclaiming slurs. Theater life is rough."

    malik "lmfao, it was just a test"

    show isabelle texting:
        small_y_bounce
    isabelle "anywayssss, i would LOVE to hear you rap in person."
    isabelle "maybe we can do a lil collab or something!"
    isabelle "*little oops! Caught myself in rap mode."

    malik "oh you be recordin? thas crazy......"

    isabelle "YEAH! I record in the studio with some of my friends! I can get us a spot whenever, just say the word!"

    reader "Nothing but covers of musical songs. And pretty damned good covers too."

    malik "shit, i didn't know you were on it like that."
    malik "hey maybe we should hang out a bit more before we head to the stu"
    malik "how about i take you somewhere, nice."
    malik "like pink lobster, then we can walk around for a bit and you can tell me about your theater life."

    show isabelle texting:
        small_y_bounce
    isabelle "FUCK YES!!!!!!!!!"
    isabelle "i'm free... i think on thursday?"
    isabelle "how about i meet you at pink lobster at like... 8?"

    malik "sure, why not"

    isabelle "see you then!"

    reader "A date. You haven't been on a date in... years probably. And with a guy you met less than 24 hours ago? Maybe today wasn't as bad of a day as you thought it would be."

    ### DATE 1
    scene bg red_lobster_outside with fade

    reader "You're late. And on purpose too. You're unsure why you decided you wanted to be late. Maybe it was fear of being early and being left alone to your own devices. You'd hate to look like a loser, alone at a Pink Lobster."
    reader "You may just have to go see a therapist. Your anxiety has been getting worse and worse as of late. Or, maybe it's always been this loud, but you've just attempted to push it away all this time."
    reader "Pink Lobster. The last time you were here, it was with your theater friends after a show. It's a bit out of your typical price range, but it was a special night -- your show had sold out and no one fucked up during stage production and cues."
    reader "It was a good time."
    reader "You exit your Oober a few paces down the street from the restaurant. It gives you some time to breathe, some time to decide if this is what you really want -- or if you want to get on the nearest bus and go home."

    show malik distracted with dissolve:
        xalign 0.5
    reader "Ultimately, you decide it's for the better and walk up to the steps. As you get closer, you see a familiar face."
    reader "Checking his breath? Shit, at least he's aware."


    show malik distracted:
        linear 0.5 xalign 0.75
    show isabelle amused with dissolve:
        xalign 0.0
        linear 0.5 xalign 0.1
    isabelle "Need a mint? You know we're about to eat some cheddar biscuits right?"

    show isabelle amused:
        linear 0.5 xalign 0.7
        small_y_bounce
        pause 0.7
        linear 0.4 xalign 0.2

    reader "You hug him as a greeting. People do that on a first date right? It was nice, comforting. And you were always one to give a good hug no matter what situation or who the person is. He doesn't seem to take it badly, though, he even hugs you back."
    reader "Now there's a sense of comfort you haven't felt in a long time."

    show malik smug:
        small_y_bounce
    malik "Nah, we good."

    show isabelle amused
    isabelle "We?"

    malik "Haha, nah I just meant we as in. Me. I'm good."

    reader "You may hang around teenagers and preteens for your camp, but there's still some slang you haven't picked up on yet."

    show isabelle surprised
    isabelle "Never been here before?"

    show malik flustered
    malik "Uh..."

    show malik casual
    malik "No, I really don't eat much seafood. My dad didn't really let us when we were younger and I never grew out of it."

    show isabelle happy:
        small_y_bounce
    isabelle "Oh shit! Okay so I can help you, my friends and I come here all the time after shows!"

    scene bg red_lobster_inside with fade

    reader "Despite you only being here a few times, you've memorized the menu pretty well. It's a talent of yours, you don't even go out to eat that often but menus have always fascinated you."
    reader "It's kind of embarrassing though, hence why you take a bit to pretend to look over the menu."

    show isabelle happy2 with dissolve:
        xalign 0.2

    show malik happy with dissolve:
        xalign 0.75
    isabelle "So, how about...the Ultimate grab fest? We can share! It comes with like four sides and we can just eat off each other's plates."


    malik "Uh, yeah. That sounds nice."

    reader "Maybe you're being too eager. Or maybe he is just as confused as you once were when you lost your Pink Lobster virginity."
    reader "You call over the waiter rather loudly, almost forgetting that you aren't in a theater. Then again -- it *is* as dark as the places you typically perform in, with the only light coming from right above your table."

    show isabelle disgust
    isabelle "God, it's so dark in here."
    isabelle "It's almost like they don't want you to see what they're feeding you."
    isabelle "What is up with restaurants with dark lighting, they could put a rat in your food and you wouldn't even notice."
    show isabelle disgust:
        x_bounce
    isabelle "Enjoying some good pasta and then it's like, OH SHIT! ITS A RAT!"
    isabelle "That would be a great ad-lib for one of your songs."
    isabelle "Maybe not the rat part but the \"oh shit!\" Could work wonders."
    isabelle "How do you choose your beats anyways?"
    isabelle "Actually! When did you start rapping?"

    reader "You pause, squinting at him from behind your glasses. You just made a joke and he isn't laughing? How rude."
    reader "But with further inspection you realize he isn't paying attention. Maybe he spaced out? You wave your hand in front of his face."

    show isabelle annoyed
    isabelle "Helloooooo, Earth to Malik?"

    malik "Oh, shit. Sorry, I was too lost in your eyes. You are so beautiful, queen."

    reader "You nearly blurt out \"gross\" but you have a lot more self control than usual. Maybe it's because he's a stranger and you don't really want to fuck up so early in your friendship."

    show isabelle amused:
        small_y_bounce

    isabelle "I was ASKING about your rap life! When did you start... doing it?"

    show malik smug
    malik "It was back in high school. Me and my friends would just cut class to go to this guys house down the street. He was some retired DJ but always played beats loud enough to be heard from the classrooms. He always welcomed us and gave us weed. We would stay there for hours, freestyling n' shit."

    show isabelle annoyed
    isabelle "You cut class too? God, I hated high school."

    reader "You didn't hate high school. You loved it actually."
    reader "Wait did you peak in high school?"
    reader "Is that why your life is so wack now?"

    malik "Ain't we all? Why'd you skip school?"

    show isabelle flustered
    isabelle "WELL... I don't know if you would count it as skipping school, we were still technically in the school. Just not in class-."

    malik "So you were a fake rebel huh."

    isabelle "NO! No, I was bad as hell. We were just in the theater room all the time. Practicing for plays outside of school, watching musicals -- you know, theater stuff."

    malik "I don't, if we're being real, tell me about the theater life."

    menu:
        "SO! Theater life was just, it was so awesome.":
            jump IsaMalikAwesome
        "You don't know about theater life? Are you one of the types who think us theater folks are a bunch of fucking losers?":
            jump IsaMalikLoser

label IsaMalikRap:
    isabelle "Do you like rap too? I know sooo many rappers, a lot of them are… pretty bad."

    show malik annoyed
    malik "Wow, you hardly know me but you're already making assumptions."

    reader "Fuck, you really fucked this one up already. He genuinely looks hurt. Maybe you shouldn't have subtly insulted his art."

    show isabelle flustered
    isabelle "I- uh. I didn't mean to! I uh..."

    show malik annoyed
    malik "You meet a black man and think all I do is rap? Pretty racist of you."

    isabelle "I wasn't trying to be! I was just saying there are a lot of men who come down and rap! And most of them aren't good!"

    malik "Whatever. Listen, do you want anything or are you just taking up space? We have a no loitering policy here."

    reader "You're embarrassed, but you order a $5 box to go. You don't want to make more of an ass out of yourself than you already have."
    reader "You've got a habit of letting your mouth work faster than your brain, and for once, you block your own blessings."

    scene bg isa_malik_rap
    play theme_music bad_end
    window hide
    pause
    return

label IsaMalikLoser:
    isabelle "You don't know about theater life? Are you one of the types who think us theater folks are a bunch of fucking losers?"

    show malik annoyed
    malik "What? No. I didn't say that."

    isabelle "You assumed it!"

    malik "Now you're just making shit up."

    isabelle "You're the one making shit up! I didn't judge you for being a fucking SoundCloud rapper, you can't judge me for being into theater!"

    malik "Wait, what's wrong with being a Soundcloud rapper?"

    isabelle "How many Soundcloud rappers make it big? How many of the, are at the same place five years later because no one picks up their beats or songs? Do you *really* think you're all that special, Malik?"

    reader "Ouch. You hurt your own feelings with that one."
    reader "No time to focus on that though, you're too busy grabbing your purse and existing the restaurant. You're unsure where you're going, all you know is that you're definitely not crying."
    reader "Definitely not crying."

    scene bg isa_malik_loser
    play theme_music bad_end
    window hide
    pause
    return

label IsaMalikAwesome:

    show isabelle happy:
        small_x_bounce
    isabelle "SO! Theater life was just -- it was so awesome. God I loved high school actually. I got to do what I loved and didn't have to worry about paying bills. I was a choir director for the musicals, but I starred in a lot of them!"
    isabelle" Typically had the main role but sometimes I gave it to someone else. You know, there aren't that many humble people in theater! Everyone is like ME ME ME! And they don't really realize that for theater to work... people have to like. Collaborate? Unlike rap, it's kind of just a solo thing right?"

    show malik smug
    malik "I mean, it can be. I've done some collabs with my friends and that was cool or whatever. But sometimes it's a relationship between the producer and the rapper. I don't make my own beats, my mans does that for me."

    isabelle "I tried to make music once, I understand why you don't make your own."

    show malik casual
    malik "Haha, yeah. So I do more of the scene shit. I write all my raps, no influence from anyone. Well. I guess the women I interact with are my muse."

    show isabelle flirty:
        small_y_bounce
    isabelle "Oh? So does that mean I'll be in one of your songs?"

    show malik smug
    malik "We'll see."

    isabelle "I was serious about that collab. I would love for you to be in one of my shows."

    malik "I don't do free gigs, there better be moolah attached."

    isabelle "I mean, maybe! Or I could pay you in something better..."

    reader "Sex already? Were you really that desperate for affection or some touch that wasn't platonic?"
    reader "Platonic sex isn't a thing right?"

    show malik smug
    malik "You can't bed me that easily."

    show isabelle happy:
        small_x_bounce
    isabelle "Huh? OH! Gross, no I meant free tickets to our shows! I could give you a summer pass!"

    malik "Shit, that sounds even better than some pussy."

    isabelle "I mean..."

    reader "What the fuck, this man is already making you blush? Are you that easy, or has it really been that long since anyone paid any attention to you? You hate how vulnerable he makes you feel -- but, you know, maybe vulnerability isn't a bad thing."
    reader "He allows himself to be vulnerable around you as well, which is a bit of a surprise to you considering you two just met not too long ago. Maybe he's in the same boat as you and just wanted some attention too."
    reader "You doubt it though, this man is hot as hell. Even if he does work at Bopeyes, you know he's getting some action."
    reader "...that doesn't stop you from resting your hand on top of his own, your nails slightly digging into the back of his fingers. They're nice, manicured. Thank god for a man who cares about his hygiene."
    reader "Thankfully, the food arrives and you pull your hand away to make room for the plates."

    show isabelle happy2
    isabelle "Here, let me do the honors."

    reader "You forgot to wash your hands before sitting, whoops. Thank god for those little towelettes they offer."
    reader "After you clean the day's dirt from your hands, you grab a crab leg, flexing your muscles as you crack it open without using the tool provided, offering him the meat inside the leg."

    isabelle "Here! You eat the inside meat not the shell. Well -- I'm sure people *can* eat the shell? But I wouldn't! Oh, also you can like, dunk it in butter and sauces like. Hot sauce. This isn't really the place for GOOD crabs, I have to take you to a real seafood spot."

    reader "He leaned over to take a bite, classy. Maybe he's into you. Or maybe he just has poor table manners, which isn't very classy."

    show malik surprised
    malik "Not bad."

    isabelle "I remember the first time I had crab."
    isabelle "It was after some performance in middle school."
    isabelle "One of the rich mom's wanted to take us somewhere fancy, so we went to some fancy seafood restaurant."
    isabelle "The food sucked, it was super unseasoned and dry."
    isabelle "But the crab was good! I had a bunch of crab legs that night."
    isabelle "God... theater life really is just about going to as many restaurants as you can before you get sick of it."
    isabelle "Because it's tradition! After a show you go to whatever restaurant the gang is feeling."
    isabelle "And usually it's Benny's. God I HATE Benny's."
    isabelle "I've been there so much they practically know my order now!"

    show isabelle upset
    isabelle "..."

    reader "You pause for a moment, reflecting on your theater experience. It really is about doing something over and over again to get pretty much the same results. No matter the production, no matter the cast. It's always the same thing."
    reader "You've been doing this for well over 20 years. How are you not tired of it? Why did you throw your dreams of being on Broadway away to become a theater teacher?"
    reader "Is there more to yourself that you couldn't achieve because you thought you weren't good enough?"
    reader "Is your boring and unsatisfying life your fault?"

    show isabelle disgust
    isabelle "Theater is just hard? And people don't understand? Like I've been working on a script for the LONGEST TIME, and I hardly have time to work on it these days because I'm directing and teaching young kids how to act."

    show isabelle happy
    isabelle "Like, I love my job! I do! But I wish I could maybe not do my job, just do my own thing and have the money to support myself."

    malik "I get that, I wish I could stop working at Bopeyes and just pursue music full time. But I ain't making Travis Scott money so I can't do that yet."

    show isabelle upset
    isabelle "Being a creative is hard. It's hard and no one understands."

    reader "Maybe it is your fault, but you can't have an anxiety attack over it right now. You're in the middle of Pink Lobster."

    show isabelle:
        linear 0.2 xoffset 10
        linear 0.2 xoffset 0
        repeat 4
    reader "Your leg is shaking under the table as you attempt to calm your thoughts, before you know it, there is a hand on your cheek. And you find yourself leaning into it more than you would like."
    reader "You hope he cleaned them beforehand, you have very sensitive skin."

    show malik happy
    malik "How about we get out of here?"

    ### DATE 2
    scene bg car with fade

    reader "You weren't expecting him to have a car. Does Bopeyes pay enough for him to afford a car? Maybe he's making money off his Soundcloud music. Or maybe he has another job on the side."
    reader "Hey, if he has money, you're not complaining."
    reader "You asked him to take you home, not wanting to ruin the night with your anxiety -- which is probably evident with how hard you were shaking your leg on the car ride home. Once you two approach your apartment building, though, it seems to disappear. Or at least manifest into something else."
    reader "Regret? No, that's not it."
    reader "Sadness? Are you sad? If you were really sad, you would've been blasting the soundtrack to Chicago by now."
    reader "For once, you can't figure out what you're feeling, but you know one thing for sure."
    reader "Overlaying the night sky, the glow from the slightly opened windows shines down on the street below. It's nearing the end of spring, the air cool and light."
    reader "Your siblings and cousins are probably in the living room arguing over video games, but the sound of 70's salsa music drowns them out. You hear the distant sound of your grandmother singing along loudly, probably in the kitchen folding laundry or looking through her Tarot cards."
    reader "You realize you had zoned out for majority of the car ride. You snap back to reality, glancing over at him and realizing the sound of Salsa music and your grandmother's singing can't be heard anymore. Could he hear it? Or was that just a sound so familiar that it became associated with your home?"
    reader "You realize the sound of old school hip-hop fills the silence. Next to you, Malik is quietly rapping along. It's nice, it soothes your nerves in a way you never thought was possible."
    reader "How have you become so comfortable around him in so little time?"

    show malik casual with dissolve:
        xalign 0.5
    malik "So, here we are."

    show malik casual:
        linear 0.5 xalign 0.75

    show isabelle surprised with dissolve:
        xalign 0.0
        linear 0.5 xalign 0.1
        linear 0.4 xoffset 50
        linear 0.2 xoffset 10

    isabelle "Yeah. Here we are."

    malik "Uh..."

    menu:
        "Do you live alone?":
            jump IsaMalikLiveAlone
            return
        "I should probably head inside.":
            jump IsaMalikHeadInside
            return

label IsaMalikHeadInside:
    show isabelle nervous:
        small_y_bounce
    isabelle "I should probably head inside."

    malik "You sure? You know I don't have a curfew so I can stay out here as long as I want."

    reader "You can't help but laugh, you don't have a curfew either. But you know your siblings will mess with your things if you don't come home by a certain time."

    show isabelle annoyed
    isabelle "As much as I would love to do that, I have annoying little siblings who love to play with my shit when I'm gone too long."

    show malik casual
    malik "Yeah. I understand."

    reader "He looks a little upset, and you immediately feel bad. You can tell he's really feeling you, and you're really feeling him. It's a bond you don't want to ruin, but something seems to be forcing you to."
    reader "Maybe it's your own issues that you have to deal with first -- you don't want to get him involved in all that. He seems nice, despite his fuckboy facade. You feel like you've met someone genuine for once in your life."

    show isabelle disappointed:
        linear 1 xalign 0.7
        small_y_bounce
        pause 0.3
        linear 1.5 xalign 0.2
    reader "You're quiet for a few minutes before you grab your purse, leaning over to press a kiss to his cheek before exiting the car."

    show isabelle upset:
        linear 0.2 yoffset -10
        linear 1.5 xalign -0.1
    isabelle "I'll see you around, Malik."

    reader "You'll let your guard down one day. For now, you don't even wait for a reply as you make your way inside."

    scene bg isa_malik_inside
    play theme_music bad_end
    window hide
    pause
    return

label IsaMalikLiveAlone:
    show isabelle flirty:
        small_y_bounce
    isabelle "Do you live alone?"

    show malik smug
    malik "You want to fuck on the first night? I thought that was against theater code?"

    reader "There's no backing out now. You decide it's time to allow yourself to feel something. It's about time you had some fun of your own accord."
    reader "You're finally going to get laid."

    show isabelle flustered
    isabelle "Fuck? Haha, no. I mean. Maybe. I just don't want to deal with my family tonight. It's been such a good night! I don't want that to be over just yet."

    reader "Backtracking, how sexy of you."

    malik "Oh yeah, that ain't a problem. I'm sure I got a spare toothbrush for you to borrow. And you can take my bed."

    show isabelle happy:
        small_y_bounce
    isabelle "God, thank you."

    reader "He already drove you home, the least you can do is smoke him out."
    reader "Reaching into your purse, you pull out a sandwich baggy full of pre-rolled blunts. You're a master at rolling, it's your title at work."

    show isabelle smoking:
        small_y_bounce
    isabelle "Want to smoke?"

    show malik shocked
    malik "Where have you been all my life?"

    reader "You light up. Your anxiety can wait, you've got sex to be had and a blunt to smoke."
    reader "You lose track of time as he pulls up to his apartment, leaning back with your eyes closed as you hold the lit blunt out the window. He parks, and you glance up to see where he's taken you."
    reader "Not too far from where you live, thankfully, just in case shit hits the fan and you need to Oober home. Looks like a 7 dollar Oober, not too bad."
    reader "You don't even notice him on your side of the door until he opens it, bending down to let you climb up onto his back. He's either a romantic, or he *really* wants to get laid."

    malik "Your ride awaits."

    show isabelle flirty
    isabelle "You don't have to do all that! I can walk!"

    show malik flirty
    malik "You're my queen of the evening, it's my duty to serve you."

    reader "Cheesy *and* cute. You find yourself resting your glasses on your forehead so you won't poke him with them. As he adjusts his grip, you make sure to hold that blunt nice and tight."
    reader "His apartment is clean. Thank god. You've had your fair share of dirty apartments, and your room isn't exactly spotless -- but he doesn't have to know that. You're at his place right now. Maybe if this escalates more you can find it in yourself to clean your room."

    malik "So, welcome to casa de-"

    reader "The blunt is put out on an ashtray in the living room before you poke around for anything suspicious looking. You seem to be in the clear, and with that taken care of, you decide to finally stop overthinking and just let your movements speak for you."

    scene black with fade
    reader "And before you know it, it's 2 AM, and your hair is spread above your head like a halo."
    reader "God damn, do you feel like you're in heaven."
    reader "A heaven with men getting you blunts? Maybe this is too good to be true. Men can never be that good to you."

    show isabelle amused with dissolve:
        xalign 0.2
        yalign -0.5
    show malik smug with dissolve:
        xalign 0.7
        yalign -0.5
    malik "I thought you weren't trying to fuck."

    show isabelle neutral2
    isabelle "I said MAYBE, not yes or no. It was a MAYBE."

    show malik:
        linear 0.5 xalign 0.6
    show isabelle:
        linear 0.5 xalign 0.2
    reader "You feel his arm wrap around your shoulder. He's a little sweaty and kind of gross, but you allow it. Cuddling and smoking is always fun."

    isabelle "This was nice. Thank you."

    malik "No need to thank me, you're the one who planned this."

    isabelle "Yeah, I guess I should give myself ALL the credit."

    reader "There is a state of bliss and peace you hardly feel. You realize your life is rather chaotic and you don't give yourself enough time to relax."
    reader "You take the your last hit, handing it back to him and yawning. At ease, you close your eyes."
    reader "For once you feel at peace."

    malik "Someone's enjoying themself."

    isabelle "Huh? Oh yeah. I don't really get much peace at home. I still live with my family -- three sisters, a brother, my abuela and my parents. Sometimes my tio lives with us but he's with his girlfriend right now. That usually doesn't last long though."

    show malik casual
    malik "So you have a big family too?"

    isabelle "Yeah! I love them, but I just need space to myself."

    malik "I feel that, once I got my degree I had to get the fuck out of that house. I have three brothers and a sister. My dad is insane and my mother doesn't get enough credit for the shit she puts up with."
    show malik happy
    malik "I want to buy her a house and a car, hopefully get her financially stable enough to leave my dad."

    show isabelle upset
    isabelle "Yeah same! I want to get my family houses so they don't have to live with us when shit... doesn't work out."

    show malik upset
    malik "Yeah... shit doesn't work out all the time it seems."

    reader "You're both quiet for a while, allowing him to finish off the blunt."

    show isabelle:
        linear 0.1 yoffset 50
        linear 0.1 yoffset 0 xalign 0.1
    reader "There's a crash, somewhere. You're not sure where. At first you think it's outside, but Malik isn't reacting to it. Maybe it's in your head, because you feel yourself tense up. Your eyes snap open as you stare up at the ceiling."
    reader "You can't do this."

    show isabelle:
        linear 0.1 xalign 0.0
    isabelle "I know this was nice, and it is nice. Really nice. And I enjoy spending time with you. But."

    malik "But?"

    reader "He cuts you off, and for once, you aren't angry about it. It's much needed and it helps you gather your thoughts."
    reader "With the several anxiety attacks you nearly had this evening, you realize that you just -- can't. You literally can't do this."
    reader "You can't fall for this man, you can't pursue any kind of relationship with him. Or continue to sleep with him, no matter how mind blowing the sex was."
    reader "Was it really mind blowing? Or was it just something you needed? Something to take the edge off that no drink or blunt could ever do?"
    reader "You have issues of your own to figure out, you have issues with your life, how you feel trapped in a never ending dream. You have your own problems to sort out, like how you feel like a slave to your family. You're 27 years old, and you can't even move out because of how much they rely on you."
    reader "You feel like your life isn't your own. You feel like someone is controlling your every move, and whenever you start to think too hard about it, you panic. Anxiety fills your veins, replacing the blood that keeps you alive."

    show isabelle:
        linear 0.1 xalign -0.1
    isabelle "Look, I like you, but -- I'm really not in condition to pursue anything serious with you. It wouldn't be fair to do that to you if I can't commit to you 100\%. I just... I'm not mentally fit enough to worry about dating right now."

    reader "You can't get hurt if you're the one rejecting him."
    reader "Right?"

    show malik casual
    malik "Yeah, I get it. We can just be friends though right? I still want to see you perform."

    reader "Friends! You can do friends. Friends are what make the world go around. Friendship is the only constant in your life that you feel like you can control."
    reader "Or at least they keep you sane."

    show isabelle:
        linear 0.4 xalign -0.05
    isabelle "OF COURSE. Of course, yeah. Friends. I can do that. I still want to take you to some more seafood places. Hell, maybe I can introduce you to my own friend group!"

    reader "That doesn't seem too exciting to him. Despite your tone, he even yawns. But then you realize it's around 3 AM and -- oh god his hand is in your hair, and you find yourself melting against him. Your voice muffles as you bury your face in his chest."

    show isabelle smug:
        small_x_bounce
    isabelle "Falling asleep on me already?"

    show malik smug
    malik "I've been up since like 7. Cut me some slack, queen."

    reader "He falls asleep before you do. And you don't sleep much that night."
    reader "But for once, that doesn't bother you."
    reader "At least you know you need some therapy."


    scene bg isa_malik_good
    play theme_music good_end
    window hide
    pause
    return
