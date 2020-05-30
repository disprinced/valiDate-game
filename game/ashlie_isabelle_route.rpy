
label AshlieIsabelle:
    scene black
    stop music fadeout 1.0
    play theme_music isabelle_theme
    $ renpy.movie_cutscene("gui/main_menu/openingcredits.webm")
    scene bg subway with dissolve

    reader "It's approximately 1:00 PM, and you're exhausted. You've been awake for twenty hours already, and you're tempted to glare at everyone around you right now. Your stream went for longer than you'd expected, and you have another one in six hours."

    reader "Your name is Ashlie Kolum, you're twenty four years old, and your job is wearing you down. It doesn't help that you have no boyfriend or friends to complain to about your struggles -- you've been without those for around two weeks now, and it's really starting to get to you."
    reader "You wonder if your life is always going to be like this: unable to keep a relationship or friendship for longer than a year."

    show ashlie angry with dissolve:
        xalign 0.5

    reader "But you have shit to do, so there's no time for another existential crisis. Six hours is enough time to get in a cat nap, but first, you need to buy some energy drinks. Come to think of it, you could use some real groceries too. Either way, that requires a trip to the store, so you walk over and try your best to seem chipper."

    reader "So, now that you’re here, you can either make this a grocery trip or just an energy drink trip. Your patience is running thin, but your fridge is also looking awfully empty."

    menu:
        "Just get the energy drinks.":
            jump AshlieIsaEnergyDrinks
            return
        "Buy some real food.":
            jump AshlieIsaRealFood
            return
    return

label AshlieIsaEnergyDrinks:
    scene bg convi_store with dissolve
    reader "You grab the energy drinks from the store, get them to self check out, and leave the store as quickly as you can. You’re famished by the time the stream starts, but you’re a professional."
    reader "You can be extra bitchy because you’re hungry, and you’ll probably get more views. You still regret your choice once everything’s done, but who cares. You can get groceries another time."

    scene bg isa_bar_gameover
    play theme_music bad_end
    window hide
    pause
    return

label AshlieIsaRealFood:
    scene bg liquor with dissolve
    reader "Okay, fuck it. You might not get a lot of sleep tonight, but you need to eat. Your shopping trips are efficient as usual. You know your way around the store, and you know what you need to stay functional throughout the day."
    reader "What you don't know how to deal with, however, is the singing woman in the spice aisle."

    show isabelle happy2 with dissolve:
        xalign 0.5

    unknown "Paprika rika rika~ Come into my basket~"

    show isabelle happy:
        linear 0.5 xalign 1.0

    show ashlie confused with dissolve:
        xalign 0.0
        linear 0.5 xalign 0.2

    ashlie "Uh, excuse me?"

    reader "You try and use your sweetest voice on this absolute weirdo. She turns around with a broad smile, not embarrassed at all."

    unknown "Did my singing bother you?"

    ashlie "Uhm, not really. I was just confused."

    unknown "My bad! I get like that sometimes! It's so annoying. I run some theater camps around town, if that explains anything."

    show ashlie normal
    ashlie "Yeah, it explains a lot. Now, could I just get-"

    show isabelle neutral
    unknown "Did you want some paprika too?"

    ashlie "I was actually looking for the vanilla extract."

    show isabelle neutral2
    unknown "Oh! Okay! Cool! It's right over there."

    reader "She points right to where the vanilla extract is. You move to grab it, and she stares at you for a moment."

    show ashlie confused
    ashlie "Can I help you with something?"

    reader "You sound a little more irritated than you intended to, and you immediately regret it. You don't like letting strangers see your real self, even if they're just grocery store weirdos."

    show isabelle confused
    unknown "You just look like, really familiar. Do you stream on Twitch or something?"

    show ashlie surprised:
        small_x_bounce
    ashlie "How did you know?"

    reader "Oh shit. You might be talking to a fan? You're bare faced, and you look like you got hit by a truck."

    show isabelle happy2:
        small_y_bounce
    unknown "Oh, my kids really like you! I mean, they're not my kids, but they're the kids I teach. I saw them watching you when they were supposed to be at practice. Oh! I should introduce myself. I'm Isabelle, though everyone calls me Isa, it's nice to meet you!"

    show ashlie casual
    ashlie "I'm Ashlie, it's nice to meet you too."

    reader "You smile at her, and she smiles back. She might be weird, but she has a killer presence. You could use some of that in your life."

    show isabelle neutral2
    isabelle "Sorry to bother you this whole time though, I was hoping things would magically come to me if I just sang them into existence."

    ashlie "Oh, I'm sorry to hear that. What's going on?"

    reader "Isabelle chuckles sadly, and her energy seems to fill the entire store."

    show isabelle sad
    isabelle "Just work and family stress, mostly. I sing whenever I need to let some of that energy go. Has anyone told you you're like, really kind before?"

    reader "People have, but their opinions never lasted. Afterwards, you were often called a nosy bitch, or a shit starter, or something similar. You wish people appreciated your kindness more. Maybe that's why, for some reason, you don't want to quit talking to this stranger."

    ashlie "Not really, no. I appreciate it though, I kind of make a living being rude to people, so it's nice to see my good side being acknowledged for once."

    show isabelle happy
    isabelle "Well, I'm glad I could help!"

    ashlie "You did. Anyways, if I could just grab that-"

    show isabelle neutral3:
        linear 0.75 xoffset 80 yoffset -30
        linear 0.3 xoffset 0 yoffset 0
    isabelle "Yeah, of course! Sorry I was in your way. Can I ask what you're planning on cooking?"

    ashlie "I don't really know yet, to be honest. I'm just going to sleep for a few hours, stream, and figure out dinner after I sleep again. I just happened to remember I was out of vanilla extract."

    isabelle "Do you bake a lot?"

    ashlie "I do, actually...it was probably pretty obvious from my basket, huh?"

    isabelle "A little. But that's a nice hobby! I don't really cook or bake on my own that much, so I admire that."

    ashlie "Oh, thank you."

    reader "She really is stroking your ego in all the right places. You haven't gotten that in a long while, and you have to admit, it feels pretty nice. In recent times, you've been constantly treated like you were secondary, like your feelings didn't matter for some reason."
    reader "Especially by your ex, who tended to prioritize blurting out his feelings instead of thinking anything through."

    isabelle "Yeah, mostly my abuela takes care of those things. Everyone says I should be a little more self sufficient, but I have a lot going on. Theater's kind of my life, you know? It's where my career is, and it's where I made most of my friends."

    ashlie "I get it. I feel the same way about games. That's where I've made most of my friends."

    reader "Video games have always been your main source of comfort, and you're glad you could make them your source of income too. All you have to do is look cute and curse some people out, what could be better than that?"

    show isabelle:
        small_x_bounce
    isabelle "That makes sense. Can I be weird for a second?"

    ashlie "I did, yeah. And go ahead."

    show isabelle neutral2
    reader "This whole interaction has been pleasantly weird already, so you suppose you can stick with it for a little while longer. Isabelle cocks her head to the side, looking away from you for a moment. Her expression is a mystery to you once she turns back around."

    isabelle "You seem like someone with a lot of friends."

    show ashlie surprised:
        small_y_bounce
    ashlie "Really? Uh...thank you?"

    reader "You're a little annoyed, to be honest. It's not her fault, she's got no way of knowing, but your friendship situation is still a sore spot for you."

    show ashlie normal:
        linear 0.25 xoffset 10
    ashlie "I can't say you're right about that, though."

    show ashlie happy
    reader "You smile your very best smile, even though you have approximately zero friends right now. Your most recent friend group only lasted a few months, and it all fell apart when you broke up with your ex. You won't lie, it was pretty explosive, but them calling you emotionally irresponsible was a little much."

    show isabelle happy:
        slow_y_bounce
    isabelle "No problem~ I'm sure you'll get some good friends in no time!"

    show ashlie tired
    reader "She sings this last bit a little too loudly, and one of the shoppers coughs loudly. Isabelle does not take the hint. You look around at the other shoppers, a handful of which are looking back at the two of you."

    show ashlie happy
    show isabelle happy2
    reader "When Isabelle makes eye contact with anyone for a moment too long, she smiles at them as if singing in public is a totally normal thing to do. You're not gonna lie, you admire her confidence quite a bit."

    menu:
        "Thank her.":
            jump AshlieIsaThank
            return
        "Dismiss her.":
            jump AshlieIsaDismiss
            return
    return

label AshlieIsaDismiss:
    show ashlie tired
    ashlie "Let's just say I'm not that great at keeping friends."

    reader "Oh. That was a lot harsher sounding than you intended it to be. You aren't above being a little bitchy, but to someone you just met? Really?"

    show isabelle sad
    isabelle "Oh...I'm sorry to hear that."

    reader "There's an awkward beat of silence between the two of you. Maybe you shouldn't speak like that to fans. You never know what they're gonna post on Reddit."

    isabelle "Well, I guess I should get going, huh?"

    ashlie "Yeah...."

    show isabelle disappointed:
        linear 2.0 xoffset 200
    reader "Isabelle starts to walk off. You suddenly feel the urge to at least apologize to her, if only so you can save face."

    show ashlie normal:
        linear 0.3 xoffset 100
    ashlie "Wait."

    isabelle "Hm?"

    show ashlie tired
    ashlie "I'm so sorry for lashing out at you. You really didn't deserve that."

    show isabelle sad
    isabelle "Oh! It's okay, really! I'm used to being on the other end of that kinda stuff. Theater is usually high pressure, and teenagers can be pretty mean so..."

    show ashlie sad
    reader "Ouch."
    reader "You're a little insulted she's comparing you to a teenager. You won't let it fracture your ego though."

    show ashlie normal
    ashlie "Still, is there any way I can make it up to you? Maybe I can treat you to something?"

    reader "You need a new friend before you get a new boyfriend, so what's the harm in asking?"

    show isabelle neutral2
    isabelle "Maybe we can get coffee later this week! Ooh! This'll be fun, I just know it!"

    # TODO i think they're missing an ending here

    scene bg isa_bar_gameover
    play theme_music bad_end
    window hide
    pause
    return

label AshlieIsaThank:

    ashlie "Thank you! I'm sure someone like you would be a great friend."

    reader "You're laying it on a little thick, and it doesn't help that this has been the first positive person to person contact you've had in days. But whatever. It's harmless chatting, what can possibly come out of it?"

    ashlie "It was nice chatting with you. I guess we should both get going, huh?"

    show isabelle happy:
        small_y_bounce
    reader "You're surprised that it's actually the truth. Isabelle seems to shine under the compliment. You honestly wouldn't mind talking to her again, but you don't want to seem weird and ask for her number. She stares at you for a moment before perking up and talking once again."

    show isabelle happy2
    isabelle "Say, I know this is crazy, but do you want to get coffee or something? As friends!"
    show isabelle neutral3
    isabelle "You just seem like a really cool person, and I'd love to talk to you more!"

    show ashlie texting
    ashlie "Here, I'll give you my number if you take your phone out. Just text me and I'll see if I can reply after my stream."

    show isabelle texting:
        move_right
    reader "Isabelle takes her phone out and unlocks it. You plug in your information into her contacts. You know this is completely impulsive, and she isn't usually the kind of person you'd be friends with, but it's worth a shot."

    show ashlie happy
    show isabelle happy
    isabelle "Okay, cool! I'll text you later~"

    show isabelle singing:
        linear 2.0 xoffset 400
    reader "Isabelle continues to sing on her way to the next aisle. Vanilla extract was the last thing you needed, so you head to the checkout line. You get back home exhausted, but ready to get through the rest of your day. You put your groceries away, make yourself something to eat, take a nap, and get to streaming once you're done."

    scene black with fade
    scene bg ash_apartment with dissolve

    show ashlie normal with dissolve:
        xalign 0.1
    reader "By the time you're done with your stream, you see a text from an unknown number in your notifications."

    show isabelle texting with dissolve:
        xalign 0.95
        small_y_bounce
    # TODO make texting laksdglkfsj
    unknown "hey! It's isa from the store, how are you?"

    reader "You save her number quicker than you anticipated you would. Why are you so excited to befriend her?"

    show ashlie happy:
        small_y_bounce
    ashlie "hi 8) I just finished my stream so i'm pretty tired how are you :0"

    show isabelle texting:
        small_y_bounce
    isabelle "GOOD!! Just finished up with the kids today, so that was fun!!"

    reader "Wow, she sounds enthusiastic."
    reader "You can see yourself getting used to this."

    show isabelle texting:
        small_y_bounce
    isabelle "anyways, that must've been WEIRD!! Suddenly getting accosted by me at the grocery store and all that. Thanks for letting me talk your ear off!"

    show ashlie happy:
        small_y_bounce
    ashlie "it was no problem 8) it's really nice having potential friendships again"

    show isabelle texting:
        small_y_bounce
    isabelle "yea me too!! Sooo, about that coffee...do you still wanna do that?"

    show ashlie happy:
        small_y_bounce
    ashlie "definitely C8 I usually stream every tuesday thursday and saturday and create videos whenever my best days are monday and wednesday does that work for you :0"

    show isabelle texting:
        small_y_bounce
    isabelle "YAY!!! Monday works for me too, it's a long weekend so i don't have work that day"

    show ashlie happy:
        small_y_bounce
    ashlie "when do you want to meet :0"

    show isabelle texting:
        small_y_bounce
    isabelle "how about 12:00? I know this SUPER cute cafe near the grocery store. It's called angel wings bakery and cafe. Have you been?"

    reader "You went once with an ex boyfriend, they have good macarons, but they aren't as good as yours."

    show ashlie happy:
        small_y_bounce
    ashlie "yeah, they have good pastries! I'm down to go over there >8)"

    show isabelle happy:
        small_y_bounce
    isabelle "okay!!"

    ### HANG 1
    scene bg cafe with fade

    reader "Your uber driver switches a grand total of three times as you're trying to get out of the house, and you wind up a full seven minutes late. You're frustrated, mostly because you hate being late to things. "

    show isabelle happy with dissolve:
        xalign 0.5
    reader "You also hate when others are late, so you're glad to see Isabelle waiting for you, already set up at a table in the back. You approach her with a killer smile."

    ashlie "Hey! Sorry to keep you waiting, uber troubles."

    show isabelle happy:
        small_y_bounce

    reader "Isabelle smiles at you and waves."

    show isabelle happy2:
        linear 0.7 xalign 0.9
    show ashlie excite:
        xalign 0.0
        linear 1.0 xalign 0.2

    isabelle "No problem! Come on, have a seat once you've ordered something!"

    reader "Isabelle starts out speaking normally, but breaks into song when she gets to the word \"have.\" She grins at that, clearly satisfied with herself. Everyone else around her looks unnerved at best, and you kinda like that. You quickly go to the counter and order your usual: a cafe mocha (hey, you like 'em sweet), and then sit across from Isabelle."

    menu:
        "I prefer when people bring things to me.":
            jump AshlieIsaIPrefer
            return
        "I was just focused on talking to you.":
            jump AshlieIsaFocused
            return
    return

label AshlieIsaIPrefer:
    show ashlie tired
    ashlie "It's just a little easier when people bring things to me, you know?"

    show isabelle disgust
    isabelle "No, I don't actually."

    show ashlie sly:
        slow_y_bounce
    ashlie "It's nice. Especially with men, when they go out of their way to take care of you. That makes sense, right?"

    show isabelle annoyed
    isabelle "I think those are two very different things! You shouldn't make these people's jobs harder than they already are."

    show ashlie tired
    reader "Shit."
    reader "Isabelle looks vaguely disgusted. You guess you've already burnt this bridge, huh?"

    show ashlie normal
    ashlie "Anyways, about-"

    show isabelle confused:
        small_y_bounce
    isabelle "Anyways! Can I ask you something weird?"

    # TODO missing ending?
    return

label AshlieIsaFocused:
    show ashlie normal
    ashlie "Sorry, I was just too focused on you!"

    show ashlie happy:
        small_y_bounce
    reader "You smile for extra effect, and Isabelle seems placated."

    show isabelle neutral
    isabelle "Oh, okay! Well, you should pay attention when people are calling your name, but I'm glad you're interested in what I have to say! Can I ask you something weird?"

    ashlie "Go ahead."

    show isabelle smug
    isabelle "Are you like, hitting on me or something?"

    show ashlie surprised
    reader "You? Hitting on a girl? No, that's not your thing. Sometimes you've wished you were attracted to women, you've heard they're better at pleasing partners than men, but that's not in the cards for you. At least, you don't think it is."

    show ashlie normal
    ashlie "Oh no, I'm not into women like that. Why do you ask?"

    show isabelle flustered:
        small_y_bounce
    isabelle "I see. I guess I'm just not used to people being...interested in my life like that. Not unless they're trying to get into my trousers."

    show ashlie tired
    ashlie "I get that. One of my exes was like that. He always said we were closest during sex, as if everything else didn't count. Ugh. Anyways, are you into women? I really don't care if you are, I'm just wondering now that you've brought it up."

    reader "You've had your fair share of gay friends in the gaming community, and you were raised to be tolerant, so it really isn't an issue for you."

    show isabelle confused:
        small_y_bounce
    isabelle "Maybe? I'm still figuring this whole thing out."

    show ashlie normal:
        small_y_bounce
    ashlie "That's cool. I hope you manage. I've heard that kind of stuff is hard."

    show isabelle neutral3
    isabelle "Thanks! So, what do you do other than game and bake?"

    reader "You resist the urge to sigh."

    show ashlie tired:
        slow_x_bounce
    ashlie "Usually I'd hang out with friends, but they all sided with my shitty ex boyfriend, so I'm low on those right now."

    reader "You were struggling, fighting to keep your dignity when all your ex did was the bare minimum, and your \"friends\" still chose him over you."

    show ashlie sad
    reader "He wouldn't even listen to you when you asked him for little things like picking you up when you went out on your own, or dropping unnecessary things when you weren't feeling well. He prioritized everything except for you."

    show isabelle sad
    isabelle "I'm sorry, I probably hit a sore spot! I swear I'm usually not like this!"

    show ashlie sad
    ashlie "It's no problem, really."

    show isabelle flustered
    isabelle "Anyways, I've never been much of a baker. Or a cook, really. My one big talent has always been singing."

    show ashlie normal
    ashlie "You mentioned you're a theater teacher, right? How long have you been doing that for?"

    show isabelle happy
    isabelle "A few years! I work at theater camps and perform at this theater, it's called the Bellacalisus."

    ashlie "The bird place?"

    show isabelle happy2:
        small_x_bounce
    isabelle "Yeah!"

    ashlie "I'll have to check you out sometime, when do you usually perform?"

    show isabelle singing
    isabelle "I perform on weekends! Not to toot my own horn, but I'm pretty fun. I'm sure you'd have a good time."

    reader "She sounds confident in herself, and you can't blame her. You could say the same about yourself, when it comes to some things. You're confident in your ability to be a good friend too, if you were given a chance."

    show ashlie happy
    ashlie "You're confident."

    show isabelle confused
    isabelle "Is that a bad thing?"

    reader "She looks a little wary, almost like she's about to bite your head off if you say the wrong thing. You really don't want to say the wrong thing right now."

    ashlie "Not at all. I'm confident too. You know about what I do right?"

    isabelle "I just know you stream games, I assumed it was a side hustle or something. I wish I had energy for something other than theater to be honest. Or, well, I don't actually, it's just nice to say that, right?"

    ashlie "Well, I'm a professional gamer. I know how it sounds, but I'm damn good at my job."

    reader "You know you sound a little defensive, but who can blame you? Your parents always thought gaming was going to be a phase, not your whole career. They're still expecting you to give up and pursue a normal job, something related to your sociology degree. You're sorry to disappoint them, but that isn't going to happen."

    show isabelle sad
    isabelle "Still, that's amazing! I suck at video games, so I can't imagine it. You must be really popular, huh?"

    reader "She looks a little upset at that. What is she, jealous? You suppose you should reassure her -- you're in this to make a friend, after all."

    show ashlie sad
    ashlie "Are you okay?"

    show isabelle flustered
    isabelle "YEAH! Yeah, I'm fine. Sorry about that, it's just personal stuff. Absolutely not you, not at all."

    ashlie "Do you want to talk about it?"

    show isabelle sad
    reader "Isabelle looks sad. Maybe you shouldn't pry into a stranger's personal life. You've had enough of that in your own experience."

    isabelle "Well, it's mostly because I gave up my own dreams to be on Broadway, and now I'm here! Not that i dislike it or anything, but it's just cool to see people actually pull off their dreams. I just wish that was me, you know?"

    show ashlie normal
    ashlie "I'm sure you can too, but what you're doing isn't bad on its own."

    reader "You feel oddly sincere about this. You think it's because you know your own dream is temporary, and it'll fall through when your looks fade and your attitude stops being cute to people. Your exes found it endearing at first until they realized this was who you are, full stop, no acting."
    show ashlie tired
    reader "So did your ex-friends, until you started asking them to take your side on things."

    show ashlie normal
    isabelle "Thank you. I'm sorry for unloading all this on you!"

    show ashlie amused
    ashlie "It's no problem, I'm not much of a singer, but I guess we've got this much in common, at least."

    show isabelle neutral
    reader "Isabelle seems relieved to hear you say that."

    isabelle "You're right about that! I wanted to ask you something else."

    ashlie "What is it?"

    show isabelle neutral2
    isabelle "What kind of music do you listen to, usually?"

    ashlie "Mostly pop music, sometimes heavy metal when I'm feeling angsty."

    reader "Needless to say, you've been playing Baby Metal nonstop for the past few weeks. Your audience seems to like it. Your neighbors? Not so much."

    show isabelle singing
    isabelle "I see! It must be pretty obvious, but I mostly listen to showtunes. There's something about them that's always going to be super charming~"

    show ashlie annoyed
    reader "She starts to sing again. Okay, this is starting to get a little annoying."

    menu:
        "Why do you like to sing so much?":
            jump AshlieIsaWhySinging
            return
        "Don’t say anything.":
            jump AshlieIsaDontSay
            return
    return

label AshlieIsaDontSay:
    show ashlie tired
    ashlie "..."

    show isabelle upset
    isabelle "...Uh, is everything okay?"

    show ashlie tired:
        slow_x_bounce
    ashlie "It's just your singing."

    show isabelle smug:
        slow_y_bounce
    isabelle "What about it? Am I too good for words?"

    reader "Irritation rises from your gut to your throat. You don't know why, but a part of you wants to tell her the truth."

    ashlie "Oh, it's just a lot. That's all. Not saying you're a lot, but the singing is."

    show isabelle angry
    isabelle "What, you don't like it when people express themselves?"

    show ashlie normal
    ashlie "That's not what I'm saying, it's just that-"

    show isabelle angry:
        x_bounce
    isabelle "It's just that you find other people's personal hobbies annoying and beneath you. I've seen bits of your streams you know, you're awfully mean."

    show ashlie angry:
        small_x_bounce
    ashlie "It's for the viewers, not for me."

    show isabelle angry:
        linear 0.3 yoffset -70
        linear 0.3 yoffset 0
    isabelle "That's what you say, but doesn't a part of you feel satisfied tearing into people like this? Isn't that why you do what you do?"

    reader "She's not wrong about that, but you genuinely love gaming. That's why you do what you do. Are you a bitch? Probably, but that doesn't mean you'd be so cruel to someone you genuinely want to be friends with."

    show ashlie angry:
        small_x_bounce
    ashlie "Why do I have to take this from you? We aren't even friends."

    reader "Your pride won't let you take any more of this. Then again, your pride won't let you take anything from anyone. That's the beauty of it."

    show isabelle annoyed
    isabelle "You know what? You're right. I'm done with this. Goodbye."

    show isabelle annoyed:
        linear 4 xoffset 1000
    reader "Isabelle looks close to tears when she walks away, but you don't try to stop her. It was her fault for insulting you in the first place."

    show ashlie tired
    reader "Still, you can't help but think about what ifs. Like -- what if you hadn't fucked up with someone you were actually interested in becoming friends with? You take one last sip of your mocha and sigh, burying your face in your hands once you put your cup down."

    scene bg isa_malik_rap
    play theme_music bad_end
    window hide
    pause
    return

label AshlieIsaWhySinging:
    show ashlie confused
    ashlie "Say, why do you like to sing so much?"

    reader "you mean to say something like: \"Why the fuck are you always singing in public?\" but you think that would leave a bad impression."

    isabelle "Oh! That's just been how I am. Ever since I was a kid, singing was the only thing for me. My dad always used to sing with me too, so I guess I picked it up from him."

    show isabelle happy2:
        slow_x_bounce
    reader "Isabelle takes a visible breath before smiling. She seems comfortable telling this story."

    show isabelle happy
    isabelle "Eventually, I started singing in church, then plays and musicals, and now I'm here! That's a little rundown of my singing life, I'm so happy you're interested!"
    show isabelle happy
    isabelle "Most people I talk to have their own theater stories, so mine's not really out of the ordinary. It's just nice to know someone outside of that circle actually like, cares, you know?"

    show ashlie normal
    reader "Oh. She took that as a compliment. You didn't intend it to be, but you suppose this works."

    isabelle "Anyways, enough about me! What made you decide to be a professional gamer?"

    reader "you’re not sure what answer to give her, mostly because there’s more than one. the first is obvious: you love gaming. The second involves your personality. You're good at insulting people and keeping an audience entertained."
    reader "You learned this when you were younger, playing with your cousins. You never went easy on them, and you were good at taunting them when you needed to. Some might even call you a bully, like you have a superiority complex that never died after high school."

    show ashlie annoyed
    ashlie "It was for a lot of reasons."

    reader "The third is that you always knew you were pretty, and you wanted to use your looks for something that wasn't as stiff as modeling seemed to be."

    isabelle "Like what?"

    show ashlie casual
    ashlie "Like, it just fits where I am in my life right now. It's something I'm good at, and it really suits me. It makes me happy that I'm able to pull this off. I feel really lucky."

    reader "And the fourth reason? That's something you prefer to keep under wraps. You consider yourself a bit of a private person, even when it comes to admitting things to yourself. People have said it's because you're a Scorpio, but you don't really believe in horoscopes."

    show isabelle amused
    isabelle "That's AMAZING! I love that for you, I really do. I know we haven't known each other for very long, but it feels like we're opening up to each other."

    ashlie "Yeah, totally."

    reader "You're not so sure about that. You don't really open up to people until some time has passed, and most people don't like what they see."

    show isabelle neutral
    isabelle "Anyways, how are you doing on time? Do you have anywhere to be?"

    reader "that’s a good question. you quickly check your phone -- it’s 12:45, and you wanted to get home around 2:00. You can afford to hang around a little longer."

    ashlie "I have some time. I just wanted to bake a bit when I got home, before I get to editing."

    isabelle "Wow, you edit your own stuff?"

    ashlie "I'd rather do that than pay someone to do it. I'm pretty okay, if I do say so myself."

    show isabelle texting
    isabelle "I see. I should get back around 1:30 for lunch. It's the first time in a while that my sisters, my brother, and my parents are all home. Or home-ish. I'm obviously not home right now. My abuela keeps insisting we take some time to eat with her, and I want to do that. Family's important, you know?"

    show isabelle neutral3
    ashlie "I get that. I don't get to see my family too often, they're all out west. How many siblings do you have?"

    isabelle "Three sisters and a brother. It's a LOT, but we make it work. Where out west?"

    ashlie "San Diego."

    reader "It's not like that's classified information, but you still feel strange saying it to someone you barely know."

    show isabelle surprised
    isabelle "Ooh, is that where you're from?"

    ashlie "Yeah. What about you? I'm assuming you're from here."

    show isabelle disappointed
    isabelle "YEAH! Never really got a chance to leave, but I'm happy with that. I'm satisfied."

    show isabelle neutral
    reader "You raise your eyebrow, crossing your arms over your chest. She's bluffing. You're not genuinely convinced she is, but that's okay. You can't say you're entirely satisfied with your life either."

    ashlie "That's good to hear. I'm guessing you have to get going soon?"

    isabelle "Yeah, I do. It was great talking to you though! Thanks for going out with me on such a whim. Do you think we can see each other again?"

    show ashlie tired
    reader "You think for a moment. The truth is, your fourth reason for becoming a streamer is because -- well, you're lonely. You're in a perpetual loop of it, always finding people before losing them again."
    reader "If you're feeling extra vulnerable and self hating, you'll admit it's not always their fault. You're destructive to most people around you, and you expect too much from the people around you."
    reader "You're not exactly the best person, but so what? You still deserve friendships, right? You still deserve the chance not to be alone, even though you have flaws. Besides, who doesn't have flaws? You want more than what you have, and you're ready to fight for it. To fight in order to keep it."
    reader "Okay...that's a little dramatic. But circumstances are dire, and you need some kind of companionship in your life that goes beyond just streaming."
    reader "You think about this because despite everything, Isabelle seems earnest and real. You want that in your life."

    show ashlie amused

    ashlie "Yeah, definitely! You can text me when you want, anytime."

    show isabelle happy
    isabelle "Are you sure about that? Not to brag, but I can be quite distracting over text."

    show ashlie surprised
    ashlie "How so?"

    show isabelle flustered
    isabelle "Well, I always have a lot to say. Some people think it's too much, but I like it."

    show ashlie happy
    ashlie "I don't mind that. I just tend to send a lot of memes."

    show isabelle happy2
    isabelle "I'm not too hip with meme culture, but I'll do my best to understand them!"

    ashlie "Wow, you really do sound like a teacher."

    show isabelle happy:
        small_y_bounce
    isabelle "I'm taking that as a compliment~"

    show ashlie happy
    reader "You smile at that, and Isabelle smiles back. You could get used to this."

    isabelle "Anyways, I'll see you around, right?"

    ashlie "Yeah, see you."

    show isabelle happy2:
        linear 4 xoffset 1000
    show ashlie happy:
        linear 4 xalign 0.5
    scene black with fade
    reader "With that, Isabelle walks away. Just like she promised, she texts you with a picture of a flier for her new performance. You manage to get there and still make your Saturday stream, and you get way more into it than you thought you would."
    reader "After the show, you make sure to chat with Isabelle and arrange another time to hang out. It's not quite the friend group you lost, but it's a start."
    reader "You suppose musical theater isn't so bad, and Isabelle comes around to heavy metal. The two of you remain unexpected friends, and this time, you hope it lasts."

    scene bg isa_malik_good
    play theme_music good_end
    window hide
    pause
    return
