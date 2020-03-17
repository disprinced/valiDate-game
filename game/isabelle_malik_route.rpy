
image bg isa_bar_gameover:
    "endings/ISAGAMEOVER1.jpg"

image bg isa_malik_rap:
    "endings/ISAGAMEOVER1.jpg"

label IsabelleMalik:
    scene black
    play theme_music isabelle_theme

    reader "You weren’t sure where you were going as you left your house this morning."
    reader "Not really in the mood to deal with public transit or Ubers. So you walked. You walked into the buiser part of your neighborhood with no destination. "
    reader "You didn’t have to be in the theater until late this afternoon for a dress rehearsal. And you love the theater life."
    reader "But god damn were you just not in the mood to deal with people like yourself, people who refused to grow out of their theater phase of high school."

    show isabelle default1:
        xalign 0.0
        linear 0.5 xalign 0.5

    reader "Your name is Isabelle Morrigan, you are 27 years old, and you suddenly remember you ditched the breakfast your abuela made as you felt the rumble in your stomach."
    isabelle " You should probably get something to eat before you make the walk towards the theater. Or maybe you’ll see a friend on the way."

    show isabelle default2

    reader "Your mind is cluttered, you’re unsure on where to focus your attention to. For once in your life. You feel yourself being unsure of yourself. Unsure of what you’re doing. Unsure of where to go on with your life."

    reader "You didn’t even realize you were standing in the middle of the sidewalk, spaced out as you run through whatever thoughts were in your head."
    reader "Coming back to reality when you hear the clearing of a throat behind you. Snapping back and beginning to walk towards, somewhere. You’re not sure where that somewhere is."
    reader "Do you need a drink? Some food? Both? Can you get both at 11 AM?"
    reader "Probably, you do live in a rather big city. The city sleeps, but it is too early for an afternoon siesta."

    reader "12:30 PM is the time you finally figure out where you want to spend your afternoon and grab that drink you desperately need. Or maybe the food will be enough to put you back in the usual chipper mood."

    scene bg bobeyes with dissolve

    reader "You enter the Popeyes/Bar fusion that was not too far from the park you were seated at. Making sure to allow the door to close quietly behind you so you wouldn’t cause too much of a scene. You didn’t want your bad mood to become even worse. "

    reader "Taking a step forward, you stand in the intersection of the Popeyes and the bar. Pondering which direction you would rather go first."

    menu:
        "Enter the Popeyes.":
            jump IsaMalikPopeyes
            return
        "Enter the Bar":
            jump IsaMalikBar
            return

    return

label IsaMalikPopeyes:
    reader "You decide you need food in you more than you needed a drink. The growl of your stomach nearly loud enough for people in passing to hear. And that was embarrassing to say the least."
    reader "You haven’t felt this hungry in a while. Or maybe your bad mood is pushing you to eat for comfort. Either way, you enter the Popeyes. Glancing over the menu before glancing at the tall man who stood behind one of the registers."

    show malik distracted with dissolve:
        xalign 0.9

    reader "Wow, this man was… so fucking hot. You find yourself staring longer than you should. Thankfully he is busy with another customer and wasn’t paying much attention to you."
    reader "The mood that had previously been sour had dispensed into thin air. The theater nerd who never grew up came back in full force as you approached his register."

    show isabelle default1:
        xalign 0.0
        linear 0.5 xalign 0.2

    isabelle "So I’m thinking that I want a drown down some dry biscuits with a shot of tequila? "

    malik "Nice to know you don’t drink much."

    reader "That was a callout, you really don’t, and when you do, it’s typically something light like a Mike’s hard lemonade or some wine cooler your friend brought to the after parties."

    isabelle "Yeah, not much of a drinker. I dabble more in the COOL drug scene. Nothing crazy! Just the shit growing from the earth."

    reader "Jesus lord you’re so fucking lame. Maybe you need to stop spending all your time around 12 year olds and spend more time with your friends."

    malik "So what can I get for you? It’s Tuesday, we’re having that 2 wings, a fry and a biscuit for $3."

    isabelle "$3? Damn that’s a steal! At theater camp, they give the counselors discounts but I’m really over those dry sandwiches."

    malik "I bet they got y’all with those dry ass turkey and ham sandwiches with expired mayo and mustard."

    show isabelle sad
    reader "You make a face of disgust, thankfully you’re not alone with this shitty camp food experience."

    show isabelle default2
    isabelle "I KNEW THE MUSTARD WAS EXPIRED! Mustard isn’t supposed to be spicy."

    malik "Dijon mustard is spicy."

    isabelle "Really? I can’t really handle spicy food. My abuela makes fun of me for it all the time."

    malik "Abuela? Eres Latina?"

    isabelle "Oh! I don’t speak much spanish. I mean I do, but my spanish is pretty ugly so I try not to speak too much of it! Every time I do, people always have something to say."

    reader "You’ve always been embarrassed by the fact that you can’t speak it that well. Mostly because you were the only one in your family who didn’t. But to be fair, it wasn’t your fault that your parents didn’t decide to teach you how to speak it until you were 18 and made you take French classes until you were in college."

    malik "There isn’t any judgement here, I hardly speak English."

    reader "Reassuring, at least he wasn’t judging you like most people do. You assume he’s a non Spanish speaker. And even they judged you for not knowing how to speak your native tongue. Which doesn’t make sense because they can’t speak it too so they have no room to judge?"

    reader "He points to his name tag, and you notice he is the only one wearing a name tag. Maybe he has importance here?"

    # TODO make name unknown before this
    malik "Name’s Malik, manager of this five star establishment."

    reader "One of his co-workers snorts. Walking towards the back in attempt to hide it. He doesn’t pay it much attention. Instead, he leans forward, resting his elbow on the table as he rests his chin in his hand."

    show isabelle default1
    reader "You find yourself laughing as well, your normal laugh. The laugh you have been told fills up a room, causes other people to tune in. Or at least a couple of frowns to turn upside down."

    isabelle "Isabelle, everyone calls me Isa! And I’m the greeeeatest singer on the east coast!"

    reader "Singing at random times was a hobby of yours. It was just the theater girl in you. You adjust your glasses as you felt your high note shift them slightly on your face. You didn’t mean to tilt your head back that far."

    malik "Singing? So like, you musical and shit?"

    reader "Your face lights up like a Christmas tree in a rich neighborhood. It’s rare for random strangers to ask you about your musical pro-ness. People typically laughed at you or gave you an eyeroll. You don’t care for either of those reactions. Honestly, the only person who can ruin your self esteem is yourself. And sometimes your Abuela if she really pushes your buttons."

    isabelle "YEAH! Musicals! I do musicals! I run theater camps and perform on the weekends at the theater nearby?"

    malik "Bellacalisus? The one with the giant bird statue in front?"

    isabelle "Yeah! There! I can’t believe you know the name! Many people just call it the bird place."

    malik "Oh yeah, I performed there a couple of times."

    menu:
        "You’re a performer too? OH! What kind of things do you perform?":
            jump IsaMalikPerform
            return
        "Do you like rap too? I know sooo many rappers, a lot of them are… pretty bad.":
            jump IsaMalikRap
            return

    return

label IsaMalikBar:
    reader "You decide you could go for a drink first. Grab some overly greasy chicken afterwards to help sober you up before you have to deal with a bunch of elementary school kids mess up their lines they should have memorized a month ago."
    reader "The bar is mostly empty. So you take a seat near the bartender, sparking up some conversation after ordering your drink. Something light, a Grapefruit Mimosa to keep the day tarte. Whatever the fuck that means, your bartender recommended it to you."
    reader "You sip at your drink as you glance out the window, watching the world pass you by.
    Maybe having a bad day won’t kill you, maybe it is healthy for life to not be so perfect all the time."

    scene bg isa_bar_gameover
    play theme_music bad_end
    show text "Isabelle + Malik Bar Bad End"
    window hide
    pause
    return

label IsaMalikPerform:
    isabelle "You’re a performer too? OH! What kind of things do you perform?"

    malik "I rap in my spare time. I’m pretty popping in the neighborhood. They play my stuff like every Saturday night"
    isabelle "Oh shit! I have to listen to your stuff one day, I’m not super into rap, more into musicals themselves. But I’m always willing to try new things!"
    malik "Oh shit, yeah. Uh."
    malik "Uh, so I don’t have a copy on me today. But, uh. If you give me your number or, snapchat I can send you a link to my soundcloud so you can take a listen."
    isabelle "Oh fuck yes! Here."
    reader "You reach into your bag a bit too fast. A hot guy asking for your number? Why wouldn’t you cease the opportunity. Hell, you’re not here to block your own blessings."
    reader "You unlock your phone and hand it over to him."
    isabelle "Save your number and text yourself so you can have mine!"
    malik "Oh shit, yeah. Sure I will. Hey. Whatever you want. It’s on me. I guess you can get a manger’s discount. Anything for a future fan."
    isabelle "Thanks!"
    reader "You scan the menu before deciding on getting one of their new sandwiches. It doesn’t look terrible. And something light for the road."

    scene black with fade

    reader "There is a constant battle you have with yourself as you try to decide if you were going to text him first. Was it being too eager? Or maybe that was just your anxiety speaking."

    reader "Are you having an anxiety attack?"

    # TODO Switch text color for these
    malik "hey, its malik from popeyes, this is isa right"
    malik "or was i just catfished irl"
    malik "catfished irl? That dont make no damn sense lol"

    reader "Okay. Maybe you are having on. It takes you a bit to actually reply. Mostly because it takes you at least 20 tries before you finally force yourself to press send."

    isabelle "OH NO!!!! ITS ME ISA!!!! Sorrys i was in the shower."

    reader "You can lie over text. That’s what most people do right?"

    isabelle "oh don’t bother with that “oh without me” shit, i’m not with it."
    isabelle "ANYWAYS, SEND THAT LINK OVER!"

    malik "[soundcloud.com/malikdegoots]"

    reader "Okay. Music. You listen to music all the time. So why were you so nervous to listen to this? It isn’t like it’s a voicemail from an ex you’ve been dying to get away from. It’s soundcloud music. Which usually goes hard but you did meet this guy at a Popeyes."
    reader "It actually isn’t as bad as you thought it would be. It is actually pretty good. For your standards at least. And you were told to have pretty high standards when it came to music."
    reader "You decide to pick some of your favorite lyrics, writing it in your journal so you wouldn’t forget."

    isabelle "i got my daughter my son and my baby mas"
    isabelle "sittin back and lookin at the sight and awe"
    isabelle "ON GOD ill punch a n**** in the jaw!"
    isabelle "and then go back and chill at the spa"

    malik "so you’re a rapper now"

    isabelle "those are your lyrics!!!! I would never say the n word in my music!"
    isabelle "even when we were doing hip hop rap i never said it!"

    malik "yknow i would let you say it around me"

    isabelle "I WOULD NEVER!!!!!"

    reader "You do your fair share of policing when it comes to reclaiming slurs. Theater life is rough."

    malik "lmfao, it was just a test"

    isabelle "anywayssss, i would LOVE to hear you rap in person."
    isabelle "maybe we can do a lil collab or something!"
    isabelle "*little opps! Caught myself in rap mode."

    malik "oh you be recordin? Thas crazy……"

    isabelle "YEAH! I record in the studio with some of my friends! I can get us a spot whenever, just say the word!"

    reader "Nothing but covers of musical songs. And pretty damned good covers too."

    malik "shit, i didn’t know you were on it like that."
    malik "hey maybe we should hang out a bit more before we head to the stu"
    malik "how about i take you somewhere, nice."
    malik "like red lobster, then we can walk around for a bit and you can tell me about your theater life."

    isabelle "FUCK YES!!!!!!!!!"
    isabelle "i’m free… i think on thursday?"
    isabelle "how about i meet you at red lobster at like… 8?"

    malik "sure, why not"

    isabelle "see you then!"

    reader "A date. You haven’t been on a date in… years probably. And with a guy you met less than 24 hours ago? Maybe today wasn’t as much as a bad day as you thought it would be."

    ### DATE 1
    scene bg red_lobster with fade

    reader "You’re late. And on purpose too. You’re unsure why you decided you wanted to be late. Maybe it was fear of being early and be left alone to your own devices. Looking like a loser, alone at a Red Lobster."
    reader "You may just have to go see a therapist. Your anxiety has been getting worse and worse as in late. Or maybe it has always been this loud but you have attempted to push it away for so long."
    reader "Red Lobster. The last time you were here, it was with your theater friends after a show. A bit out of your typical price range. But it was a special night,  your show had sold out and no one fucked up during stage production and cues."
    reader "It was a good night."
    reader "You exit your Uber a bit of away from the restaurant. Some time to breathe, some time to decide if this is what you really want or if you want to get on the nearest bus and go home."

    show malik distracted with dissolve:
        xalign 0.9
        yoffset 100
        linear 0.5 yoffset 0

    reader "Ultimately, you decide it is for the better and walk up to the steps, seeing a familiar face."
    reader "Checking his breath? Shit, at least he's aware."

    show malik distracted:
        linear 0.5 xalign 0.5

    isabelle "Need a mint? You know we’re about to eat some cheddar biscuits right?"

    reader "You hug him as a greeting. People do that as a first date right?  It was nice, comforting. And you were always one to give a good hug no matter what situation or who the person is. He doesn't seem to take it badly, he even hugs you back."
    reader "And there was a sense of comfort you haven't felt in a long time."

    malik "Nah, we good."

    isabelle "We?"

    malik "Haha, nah I just meant we as in. Me. I’m good."

    reader "You may hang around teenagers and preteens for your camp, but there are still some slang you haven't picked up on yet."

    isabelle "Never been here before?"

    malik "Uh…"
    malik "No, I really don’t eat much seafood. My dad didn’t really let us when we were younger and never grew out of it."

    isabelle "Oh shit! Okay so I can help you, my friends and I come here all the time after shows!"

    reader "Despite you only being here a few times, you memorized the menu pretty well. A talent of yours, you don't even go out to eat that often but menus have always fascinated you. It is kind of embarrassing, hence why you take a bit to pretend to look over the menu."

    isabelle "So, how about, the Ultimate grab fest? We can share! It comes with like four sides and we can just eat off each other’s plates."

    malik "Uh, yeah. That sounds nice."

    reader "Maybe you were too eager. Or maybe he is just as lost as you once were when you lost your Red Lobster virginity. You call over the waiter rather loudly, nearly forgetting that you aren't in a theater."
    reader "But then again, it is as dark as the places you typical perform in. With the only light coming from right above your table."

    isabelle "God it's so dark in here."
    isabelle "It's almost like they don't want you to see what they're feeding you."
    isabelle "What is up with restaurants with dark lighting, they could put a rat in your food and you wouldn't even notice."
    isabelle "Enjoying some good pasta and then it's like, OH SHIT! ITS A RAT!"
    isabelle "That would be a great ad-lib for one of your songs."
    isabelle "Maybe not the rat part but the \"oh shit!\" Could work wonders."
    isabelle "How do you choose your beats anyways?"
    isabelle "Actually! When did you start rapping?"

    reader "You pause, squinting at him from behind your glasses. You just made a joke and he wasn't laughing? How rude."
    reader "But with further inspection you realize he isn't paying attention. Maybe he spaced out? You wave your hand in front of his face."

    isabelle "Helloooooo, Earth to Malik?"

    malik "Oh, shit. Sorry, I was too lost in your eyes. You are very beautiful queen."

    reader "You nearly blurt out \"gross\" but you have a lot more self control than normal. Maybe because he was a stranger and you didn't want to fuck up so early in your friendship."

    isabelle "I was ASKING about your rap life! When did you start… doing it?"

    malik "It was back in high school. Me and my friends would just cut class to go to this guys house down the street. Who was some retired DJ but always played beats loud enough to be heard from some classrooms. He always welcomed us and gave us weed. We would stay there for hours, freestyling n’ shit."

    isabelle "YOU CUT SCHOOL TOO? God, I hated high school."

    reader "You didn't hate high school. You loved it actually."
    reader "Wait did you peak in high school?"
    reader "Is that why your life is so wack now?"

    malik "Ain’t we all? Why’d you cut school?"

    isabelle "WELL… I don’t know if you would count it as cutting school, we were still technically in the school. Just not in class-."

    malik "So you were a fake rebel huh."

    isabelle "NO! No, I was bad as hell. We were just in the theater room all the time. Practicing for plays outside of school. Watching musicals, you know theater stuff."

    malik "I don’t if we’re being real, tell me about the theater life."

    menu:
        "SO! Theater life was just, it was so awesome.":
            jump IsaMalikAwesome
        "You don't know about theater life? Are you one of the types who think us theater folks are a bunch of fucking losers?":
            jump IsaMalikLoser

label IsaMalikRap:
    isabelle "Do you like rap too? I know sooo many rappers, a lot of them are… pretty bad."
    malik "Wow, already making assumptions of me and you hardly know me."
    reader "Fuck, you really fucked this one up already. He genuinely looks hurt. Maybe you shouldn’t have subtly insulted his art."

    show isabelle sad
    isabelle "I- uh. I didn’t mean to! I uh…"
    malik "Judging a black man and thinking all we do is rap? How racist of you."
    isabelle "I wasn’t trying to be! I was just saying there are a lot of men who come down and rap! And most of them aren’t good!"
    malik "Whatever, do you want anything or are you just taking up space? We have a no loitering policy here."
    reader "You’re embarrassed, but you order a $5 box and get it to go. You don’t want to make more of an ass out of yourself than you already have."
    reader "You often let your mouth work faster than your brain, and for once, you block your own blessings."

    scene bg isa_malik_rap
    play theme_music bad_end
    show text "Popeyes bad end"
    window hide
    pause
    return

label IsaMalikLoser:
    isabelle "You don't know about theater life? Are you one of the types who think us theater folks are a bunch of fucking losers?"

    malik "What? No. I didn't say that."

    isabelle "You assumed it!"

    malik "Now you're just making shit up."

    isabelle "You're the one making shit up! I didn't judge you for being a fucking SoundCloud rapper, you can't judge me for being into theater!"

    malik "Wait, what's wrong with being a Soundcloud rapper?"

    isabelle "How many Soundcloud rappers make it big? How many of the, are at the same place five years later because no one picks up their beats or songs? Do you really think you're all that special Malik?"

    reader "Ouch. You hurt your own feelings with that one."
    reader "But you're too busy grabbing your purse and existing the restaurant. You're unsure where you're going, all you know is that you're definitely not crying."
    reader "Definitely not crying."

label IsaMalikAwesome:
    isabelle "SO! Theater life was just, it was so awesome."
    isabelle "God I loved high school actually. I got to do what I loved and not have to worry about paying bills. I was a choir director for the musicals. But I starred in a lot of them! Typically had the main role but sometimes I gave it to someone else."
    isabelle "You know, there isn’t that many humble people in theater! Everyone is like ME ME ME! And don’t really realize that for theater to work… people have to like. Collaborate? Unlike rap, it’s kind of just a solo thing right?"

    malik "I mean it can be. I’ve done some collabs with my friends and that was cool or something. But sometimes it’s a relationship between the producer and the rapper. I don’t make my own beats, my mans does that for me."

    isabelle "I tried to make music once, I understand why you don’t make your own."

    malik "Haha, yeah. So I do more of the scene shit. I write all my raps, no influence from anyone. Well. I guess the women I interact with are my muse."

    isabelle "Oh? So does that mean I’ll be in one of your songs?"

    malik "We’ll see."

    isabelle "I was serious about that collab. I would love for you to be in one of my shows."

    malik "I don’t do free gigs, will there be mula attached."

    isabelle "I mean, maybe! Or I could pay you in something better..."

    reader "Sex already? Were you that desperate for affection or some touch that wasn't platonic."
    reader "Platonic sex isn't a thing right?"

    malik "You can’t bed me that easily."

    isabelle "Huh? OH! Gross, no I meant free tickets to our shows! I could give you a summer pass!"

    malik "Shit, that sounds even better than some pussy."

    isabelle "I mean…"

    reader "What the fuck, this man is already making you blush? Are you that easy or has it really been that long since anyone has paid any attention to you. You hate how vulnerable he makes you feel. But maybe vulnerability isn't a bad thing."
    reader "He allows himself to be vulnerable around you as well. Which is somewhat a surprise to you because you two just met not too long ago. Maybe he's in the same boat as you and wanted some physical attention too."
    reader "You doubt it, this man is hot as hell and even if he does work at Popeyes, you know he's getting some action."
    reader "...that doesn't stop you from resting your hand on top of his own, your nails slightly digging into the back of his fingers. They're nice, manicured. Thank god for a man who cares about his hygiene."
    reader "Thankfully, the food arrives and you pull your hand away to make room for the plates."

    isabelle "Here, let me do the honors."

    reader "You forgot to wash your hands before sitting, whoops. Thank god for those little towelettes they offer."
    reader "After you clean the filth from your hands, you grab a crab leg, flexing your muscles as you crack it open without using the tool provided, offering him the meat inside the leg."

    isabelle "Here! You eat the inside meat not, the shell. Well, I’m sure people can eat the shell? I wouldn’t! Oh, also you can like, dunk it in butter and sauces like. Hot sauce. This isn’t really the place for GOOD crabs, I have to take you to a real seafood spot."

    reader "He leaned over to take a bite, classy. Maybe he is into you. Or maybe he just has poor table manners which is not very classy."

    malik "Not bad."

    isabelle "I remember the first time I had crab."
    isabelle "It was after some performance in middle school."
    isabelle "One of the rich mom’s wanted to take us somewhere fancy, so we went to some fancy seafood restaurant."
    isabelle "The food sucked, it was super unseasoned and dry."
    isabelle "But the crab was good! I had a bunch of crab legs that night."
    isabelle "God... theater life really is just about going to as many restaurants as you can before you get sick of it."
    isabelle "Because it's tradition! After a show you go to whatever restaurant the gang is feeling."
    isabelle "And usually it's Denny's and god I HATE Denny's."
    isabelle "I've been there so much they practically know my order now!"
    isabelle "..."

    reader "You pause for a moment, reflecting on your theater experience. It really is about doing something over and over again to get pretty much the same results. No matter the production, no matter the cast. It is always the same thing."
    reader "You've been doing this for well over 20 years. How are you not tired of it? Wy did you throw your dreams away of being on Broadway to become a theater teacher?"
    reader "Is there more to yourself that you couldn't achieve because you thought you weren't good enough?"
    reader "Is your boring and unsatisfying life your fault?"

    isabelle "Theater is just hard? And people don’t understand? Like I’ve been working on a script for the LONGEST TIME, and I hardly have time to work on it now a days because I’m directing and teaching young kids how to act. Like I love my job! I do! But I wish I could do my job, or. Maybe not do my job. But do my own thing and have the money to support myself."

    malik "I get that, I wish I could stop working at Popeyes and just pursue music full time. But I ain’t making Travis Scott money so I can’t do that yet."

    isabelle "Being a creative is hard, it’s hard and no one understands."

    reader "Maybe it is your fault, but you can't have an anxiety attack over it right now. You're in the middle of Red Lobster."
    reader "Your leg is shaking under the table as you attempt to calm your thoughts, before you know it, there is a hand on your cheek. And you find yourself leaning into it more than you would like."
    reader "Hopefully he cleaned them beforehand, you have very sensitive skin."

    malik "How about we get out of here?"

    ### DATE 2
    scene bg car with fade

    reader "You weren't expecting him to have a car. Does Popeyes pay that much for them to buy a car? Maybe he is making money off his Soundcloud music. Or maybe he has another job on the side."
    reader "Hey if he has money, you're not complaining."
    reader "You asked him to take you home, not wanting to ruin the night with your anxiety. Which is probably evident with how hard you were bouncing your leg on the car ride home. But once you two approach your family apartment building, it seems to disappear. Or at least manifest into something else."
    reader "Regret? No that wasn't it."
    reader "Sadness? Are you sad? If you were really sad, you would've been blasting the soundtrack to Chicago by now."
    reader "For once, you can't figure out what you're feeling, but you know one thing for sure."
    reader "In the night sky, the glow from the slightly opened windows shined through. It was only 10 near the ends of Spring. Your siblings and cousins were probably in the living room playing video games, arguing. But the sound of 70s Salsa music drowns them out."
    reader "You hear the distant sound of your grandmother singing along loudly, probably in the kitchen folding laundry or looking through her a Tarot cards."
    reader "You realize you had zoned out for majority of the car ride. You snap back to reality, glancing over at him. Realizing the sound of Salsa music and your grandmothers singing couldn't be heard anymore. Could he hear it? Or was that just a sound so familiar that it became associated with your home."
    reader "You realize the sound of 80s Hip Hop has been filling the silence. And he was quietly rapping along. It was nice, it soothed your nerves in a way you never thought it was possible."
    reader "How have you become so comfortable around him in so little time?"

    scene bg isa_house with dissolve

    malik "So, here we are."

    isabelle "Yeah. Here we are."

    malik "Uh…"

    menu:
        "Do you live alone?":
            jump IsaMalikLiveAlone
            return
        "I should probably head inside.":
            jump IsaMalikHeadInside
            return

label IsMalikHeadInside:
    isabelle "I should probably head inside."

    malik "You sure? You know I don't have a curfew so I can stay out here as long as I want."

    reader "You can't help but laugh, you don't have a curfew either. But you know your siblings will mess with your things if you don't come home by a certain time."

    isabelle "As much as I would love to do that, I have annoying little siblings who love to play with my shit when I'm gone too long."

    malik "Yeah. I understand ."

    reader "He looks a little upset. And you instantly feel bad. You could tell he was really feeling you, and you were really feeling him. And there was a bound you didn't want to ruin, but something was forcing you too."
    reader "Maybe it was your own issues that you had to deal with first, that you didn't want him involved with. He seemed nice, despite his fuckboy facade. You feel like you met someone genuine for once in your life."
    reader "You're quite for a few minutes before you grab your purse, leaning over to press a kiss to his cheek before exiting the car."

    isabelle "I'll see you around Malik."

    reader "You'll allow someone else in one day. For now, you don't even wait for a reply as you make your way inside."

    scene black
    show text "Date 2 bad end screen"
    window hide
    pause
    return

label IsaMalikLiveAlone:
    isabelle "Do you live alone?"

    malik "You want to fuck on the first night? I thought that was against theater code?"

    reader "There was no backing out now. You decided it was time to allow yourself to feel something. To have some fun on your own personal time."
    reader "You were finally going to get laid."

    isabelle "Fuck? Haha, no. I mean. Maybe. I just don’t want to deal with my family tonight. It’s been such a good night! I don’t. Want that ruined?"

    reader "Backtracking, how sexy of you."

    malik "Oh yeah, that ain’t a problem. I’m sure I got a spare toothbrush for you to borrow. And you can take my bed."

    isabelle "God, thank you."

    reader "He already drove you home, the least you can do is smoke him out."
    reader "Reaching into your purse. You pull out a sandwich baggy full of pre-rolled blunts. You're a master of rolling, it's your title at work."

    isabelle "Want to smoke?"

    malik "Where have you been all my life?"

    reader "You light up, your anxiety can wait, you have sex to be had and a blunt to smoke."
    reader "You lose track of time as he pulls up to his apartment, leaning back with your eyes closed as you hold the lit blunt out the window as he parks. Glancing up to see where he took you."
    reader "Not too far from where you live, thankfully. In case shit hits the fan and you need to Uber home. Looks like a 7 dollar Uber, not too bad."
    reader "You don't even notice him on your side of the door until he opens it. Bending down to allow you to climb onto his back. A romantic really, or maybe he really wanted to get laid."

    malik "Your ride awaits."

    isabelle "You don’t have to do all that! I can walk!"

    malik "You’re my queen of the evening, it is my duty to serve you."

    reader "Cheesy, and cute. And you found yourself resting your glasses on your forehead so you wouldn't poke him with them. Making sure to hold that blunt nice and tight."
    reader "His apartment is clean. Thank god. You've had your fair share of dirty apartments. And your room was quite dirty too. But he doesn't have to know that. You're at his place right now. Maybe if this escalates more you can find it in yourself to clean your room."

    malik "So, welcome to casa de-"

    reader "The blunt is put out on an ashtray in the living room before you scout for anything suspicious looking. You seem to be in the clear, hence why you decide to stop thinking. Let your movements speak for you."

    ### END OF SLEEPING
    scene black with fade

    reader "And before you know it, it's 2 AM, and your hair is spread above  your head like a halo."
    reader "A god damn did you feel like you were in heaven."
    reader "A heaven with men getting you blunts? Maybe this is too good to be true. Men can never be that good to you."

    malik "I thought you weren’t trying to fuck."

    isabelle "I said MAYBE, not NO, not YES. It was a MAYBE."

    reader "You feel his arm wrap around your shoulder. And he is kind of sweaty. And kind of gross, but you allow it. Cuddling and smoking is always fun."

    isabelle "This was nice. Thank you."

    malik "No need to thank me, you’re the one who planned this."

    isabelle "Yeah, I guess I should give myself ALL the credit."

    reader "There is a state of bliss and peace you hardly feel. You realize your life is rather chaotic and you don't give yourself enough time to relax."
    reader "You take the your last hit, handing it back to him. Yawning out as you close your eyes."
    reader "For once you feel at peace."

    malik "Someone’s enjoying them self."

    isabelle "Huh? Oh yeah. I don’t really get much peace at home. I still live with my family, three sisters, a brother, my abuela and my parents. Sometimes my tio lives with us but he’s with his girlfriend right now. That doesn’t last long though."

    malik "So you have a big family too?"

    isabelle "Yeah! I love them, but I just need space to myself."

    malik "I feel that, once I got my associates I had to get the fuck out of that house. I have three brothers and a sister. My dad is insane and my mother doesn’t get enough credit for the shit she put up with."
    malik "I want to buy her a house and a car. And get her financially stable enough to leave my dad."

    isabelle "Yeah same! I want to get my family houses so they don’t have to live with us when shit… doesn’t work out."

    malik "Yeah, shit. Doesn’t work out all the time it seems."

    reader "You’re both quiet for a while, allowing him to finish off the blunt."
    reader "There is a crash, somewhere. You're not sure where. Maybe it was outside, but he wasn't reacting to it. Maybe it was in your head, because you felt yourself tense up. Your eyes snap open as you stare up at the ceiling."
    reader "You can't do this."

    isabelle "I know this was nice, and it is nice. Really nice. And I enjoy spending time with you. But."

    malik "But?"

    reader "He cut you off, and for once, you aren't angry about it. It is much needed and it helps you gather your thoughts."
    reader "With the several anxiety attacks you nearly had this evening, you realize that you can't. You literally can't do this."
    reader "You can't fall for this man, you can't pursue any kind of relationship with him. Or continue to sleep with him, no matter how mind blowing the sex was."
    reader "Was it really mind blowing? Or was it just something you needed? Something to take the edge off that no drink or blunt could ever do."
    reader "You have issues of your own to figure out, you have issues with your life, how you feel trapped in a never ending dream. With your home life, how you feel like a slave to your family. At 27 years old, you can't move out because of how much they rely on you."
    reader "You feel as your life isn't your own. You feel as someone is controlling your every move, and everything you think too hard on it, you panic. Anxiety filling your veins, replacing the blood that keeps you alive."

    isabelle "I am in no condition to pursue anything serious with you. It wouldn't be fair to do that to you if I can't commit to you 100\%. I just... I'm not mentally fit enough to pursue anything right now."

    reader "You can't get hurt if you're the one rejecting him."
    reader "Right?"

    malik "Yeah, I get it. We can just be friends though right? I still want to see you perform."

    reader "Friends! You can do friends. Friends are what make the world go around. The only constant in your life that you seem like you can control."
    reader "Or at least they keep you sane."

    isabelle "OF COURSE. Of course, yeah. Friends. I can do that. I still want to take you to some more seafood places. Hell, maybe I can introduce you to my own friend group!"

    reader "That doesn't seem exciting to him despite your tone, he even yawns. But then you realize it's around 3 AM and. Oh god his hand is in your hair, and you find yourself melting against him. Your voice muffled as you burry your face in his chest."

    isabelle "Falling asleep on me already?"

    malik "I’ve been up since like 7. Cut me a break queen."

    reader "He falls asleep before you do. And you don't sleep much that night."
    reader "But for once, that doesn't bother you."
    reader "At least you know you need some therapy."
    reader "You understand the complexities of falling asleep with a stranger. How it wont solve your issues and help you escape the hectic life you have at home. You’re nearing your mid twenties and you still don’t know how to handle the shit going on in your head."
    reader "Find the fine balance between work, theater and your own personal life. You realize you can’t balance them all together and eventually have to dedicate some time to focusing on one, and have the others fall in line. That’s how life works right?"

    scene black
    show text "Good end(?)"
    window hide
    pause
    return
