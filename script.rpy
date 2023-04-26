# The script of the game goes in this file.

# Define characters that can be typed in. We allow:
# - Uppercase letters (In ascii_letters)
# - Lowercase letters (In ascii_letters)
# - Numbers 0 to 9 (In digits)
# - A space
init python:
    import string
define allowedChars = string.ascii_letters + string.digits + " "

# Black image
image black = Solid("000") 

# Custom input screen
screen nameInput(prompt):

    # Transparent Background
    add "black":
        alpha 0.5

    # Frame in the middle
    frame:

        align (0.5,0.5)
        xysize (480, 180)

        # Vbox inside the frame
        vbox:

            align (0.5, 0.5)
            spacing 30

            # Prompt passed to the screen
            text prompt:
                xalign 0.5
                size 26
            
            # Input
            input: 
                id "input" # needed for default argument
                xalign 0.5
                size 26
                pixel_width 440
                allow allowedChars

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default preferences.text_cps = 40
default mcname = "Okumuru Tadashi"
define trainannounce = Character("Train Announcer", color="#ff0000")
define mc = Character("[mcname]", callback = name_callback, cb_name = None)
define myst = Character("???", color="#ff7373")
define ta = Character("Kazumi Tashiro", callback = name_callback, cb_name = "tashiro", color="#83fbff")
define ik = Character("Kazumi Isa", callback = name_callback, cb_name = "isa", color="#83fbff")
define ma = Character("Muramoto Madoka", callback = name_callback, cb_name = "muramoto", color="#83ffb0")
define na = Character("Natsuki Sakura", callback = name_callback, cb_name = "natsuki", color="#ff21c9")
define se = Character("Sebastian Atkins", color="#ffc921")
define ha = Character("Harumi")
image ocean=("images/ocean.jpg")
image street=("images/street.jpg")
image gate=("borrowed/school.png")
image street2=("borrowed/street.png")
image outside=("borrowed/school_outside.png")
default twinslunch = False #ate lunch with the twins
default madokalunch = False #ate lunch with madoka
default answeronecorrect = False #answered one question correct
default talktonatsuki = False #talked to natsuki on day 2
layeredimage harumi:
        group outfit:
            attribute dresshandsdown:
                "harumi/poses/1c.png"
            attribute dresshandscrossed:
                "harumi/poses/3c.png"
            attribute dressonehand:
                "harumi/poses/2c.png"
        group face:
            attribute smileclosedmouth default:
                "harumi/expressions/a.png"
            attribute speaking:
                "harumi/expressions/c.png"
            attribute happyopenmouth:
                "harumi/expressions/h.png"
            attribute happysmile:
                "harumi/expressions/i.png"
            attribute satisfied:
                "harumi/expressions/k.png"
            attribute happyclosedmouth:
                "harumi/expressions/j.png"
            attribute speakinghappy:
                "harumi/expressions/e.png"
layeredimage natsuki:
        at sprite_highlight('natsuki')
        group outfit:
            attribute uniformhandsdown:
                "kamuko/blank/school1.png"
            attribute uniformhandsup:
                "kamuko/blank/school2.png"
            attribute uniformbehindback:
                "kamuko/blank/school3.png"
            attribute uniformonehand:
                "kamuko/blank/school4.png"
            attribute uniformcheer:
                "kamuko/blank/spec.png"
            attribute casualhandsdown:
                "kamuko/blank/casual1.png"
            attribute casualhandsup:
                "kamuko/blank/casual2.png"
            attribute casualbehindback:
                "kamuko/blank/casual3.png"
            attribute casualonehand:
                "kamuko/blank/casual4.png"
        group face:
            attribute smileclosedmouth default:
                "kamuko/blank/01.png"
            attribute smileclosedeyes:
                "kamuko/blank/02.png"
            attribute speaking:
                "kamuko/blank/03.png"
            attribute concern:
                "kamuko/blank/04.png"
            attribute bleh:
                "kamuko/blank/05.png"
layeredimage tashiro:
        at sprite_highlight('tashiro')
        group outfit:
            attribute uniformpockets:
                "tashiro/poses/1.png"
            attribute uniformcrossed:
                "tashiro/poses/2.png"
            attribute casualpockets:
                "tashiro/poses/1b.png"
            attribute casualarmscrossed:
                "tashiro/poses/2b.png"
        group face:
            attribute neutral default:
                "tashiro/expressions/a.png"
            attribute sad:
                "tashiro/expressions/a1.png"
            attribute smile:
                "tashiro/expressions/b.png"
            attribute speakinghappy:
                "tashiro/expressions/c.png"
            attribute speaking:
                "tashiro/expressions/e.png"
            attribute thinking:
                "tashiro/expressions/h1.png"
            attribute smileclosedeyes:
                "tashiro/expressions/l1.png"
layeredimage isa:
        at sprite_highlight('isa')
        group outfit:
            attribute uniformhandsdown:
                "femc/1/1.png"
            attribute uniformhandup:
                "femc/1/2.png"
            attribute uniformpeacesign:
                "femc/1/2a.png"
            attribute uniformarmscrossed:
                "femc/1/3.png"
            attribute casualhandup:
                "femc/casual1.png"
            attribute casualhanddown:
                "femc/casual2.png"
            attribute casualarmscrossed:
                "femc/casual3.png"
        group face:
            attribute smileclosedmouth default:
                "femc/1/a.png"
            attribute neutral:
                "femc/1/b.png"
            attribute tears:
                "femc/1/aa.png"
            attribute tearssmile:
                "femc/1/ab.png"
            attribute irritated:
                "femc/1/ag.png"
            attribute sus:
                "femc/1/ai.png"
            attribute speaking:
                "femc/1/c.png"
            attribute speakinghappy:
                "femc/1/f.png"
            attribute smile:
                "femc/1/j.png"
            attribute smileclosedeyes:
                "femc/1/x.png"
            attribute smilesweat:
                "femc/1/z.png"   
            attribute blushclosedmouth:
                "femc/1/t.png"
            attribute blushopenmouth:
                "femc/1/u.png"
layeredimage muramoto:
        at sprite_highlight('muramoto')
        group left:
            attribute uniformarmdownl:
                "blonde/1l.png"
            attribute uniformonhipl:
                "blonde/2l.png"
            attribute uniformarmupl:
                "blonde/4l.png"
            attribute uniformpenl:
                "blonde/5l.png"
            attribute casualarmdownl:
                "blonde/1bl.png"
            attribute casualonhipl:
                "blonde/2bl.png"
            attribute casualarmupl:
                "blonde/4bl.png"
            attribute casualpen:
                "blonde/5bl.png"
        group right: 
            attribute uniformarmdown:
                "blonde/1r.png"
            attribute uniformonhip:
                "blonde/2r.png"
            attribute casualarmdown:
                "blonde/1br.png"
            attribute casualonhip:
                "blonde/2br.png"
        group outfit: 
            attribute uniformcrossed:
                "blonde/3.png"
            attribute casualcrossed:
                "blonde/3b.png"
        group face:
            attribute neutral default:
                "blonde/heterochromia/b.png"
            attribute smiling:
                "blonde/heterochromia/a.png"
            attribute speakinghappy:
                "blonde/heterochromia/c.png"
            attribute ditz:
                "blonde/heterochromia/l.png"
            attribute pout:
                "blonde/heterochromia/n.png"
            attribute smileclosedeyes:
                "blonde/heterochromia/v.png"
            attribute hit:
                "blonde/heterochromia/_3.png"
            attribute dizzy:
                "blonde/heterochromia/_4.png"
            attribute concentrate:
                "blonde/heterochromia/k.png"
            attribute phew:
                "blonde/heterochromia/_10alt.png"
            attribute cat:
                "blonde/heterochromia/_11.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/train.ogg"
    myst "{i}Per aspera ad astra.{/i}"
    myst "Latin. It means 'through hardships to the stars'."
    myst "One who has experienced hardships will perhaps overcome everything and attain enlightenment."

    scene ocean

    "I've been moving around for a long time now. After the accident happened, there was hardly any place I could call home."
    "After so long of dealing with courts and social services, I've been assigned to live in a house by the countryside owned by my aunt and uncle."
    "It had been decided that I would be living alone as I would soon be an adult, and my aunt and uncle's work schedule meant that they would check on me every few months."
    "Looking out the train windows and staring at the ocean, I feel a strange sense of Deja vu."
    "For some strange reason, I feel like I've ridden this train many times before."
    "The faint scent of the salt reaching my nose was like an old friend to me."
    "..."
    "At the same time though, I know that this is a new beginning for me."
    "I sat in a trance thinking. Who was I? What am I doing here?"
label .nameChange:

        # Let player type it in
        $ typedIn = renpy.input("Who are you?",
        default = "Okumuru Tadashi",
        screen = "nameInput").strip()

        # If they typed in nothing, go back to .nameChange
        if typedIn == "":
            jump .nameChange

        # Change the name variable to the player typed in
        $ mcname = typedIn
        mc "Of course. The one and only"

label nameChanged:
    play audio "audio/announcement.ogg"
    pause 3

    trainannounce "Attention please: we are approaching the last stop."
    trainannounce "All riders please disembark and remember to take all personal belongings."

    mc "..."
    mc "Guess it's time then."

    stop music
    play music "audio/mainstreetstroll.ogg"

    "By the time I departed from the station, the sun had completely risen and the sky was a bright blue."
    "My new home was only a few extra minutes walk from the exit, so I decided to walk along the street there."
    "The chilly Fall air blew around me, the leaves starting to turn completely."

label home:
    
    scene countryside1 with fade

    "Transferring to another school after the year already started was nowhere near ideal and normally wouldn't be considered, but due to my circumstances an exception was made."
    "Luckily, the school was having a brief holiday so students could attend a local festival, giving me time to unpack and settle into my new home."
    "After about an hour of walking, I finally arrived at the path to my home."
    "The house, despite not being directly in the city, was close enough to the point where I could receive the basic commodities like running water, electricity, and internet."
    "I walked down the path and arrived at the front door, taking out a key and unlocking and opening the door."

    scene room with fade

    "Turning the lights on, I saw that the house had clearly not been lived in for a while, with a thin layer of dust covering everything."
    "Despite the dust, the whole place was still in good condition, and I was glad that I wouldn't have to worry about any major repairs."
    "I made my way to the single bedroom and began to unpack my things."
    "I had only taken with me the essentials and a few personal items, so it didn't take long to unpack everything."
    "After that was done, I decided to clean around the house."
    "I had few thoughts going through my head as I cleaned, but I did feel a sense of peace as I worked. It almost seemed to serve as a distraction from painful thoughts of being alone in a new city."
    scene room with fade
    "The cleaning had taken a few hours, with the sun already set by the time I was done."
    "Grabbing some food I had brought, I started eating while thinking."
    mc "Will everything really be okay...?"
    "I had to accept that things would be different from now on."
    "Tomorrow, I would be attending a new school."
    "After setting my alarm and getting into bed, I soon drifted off to sleep."

label dream:
    scene black with fade
    hide room
    pause 4
    play music "audio/At our parting.mp3" fadein 3.0
    mc "..."
    mc "..."
    mc "...hmm?"
    "When I opened my eyes, I was not awoken to my alarm clock."
    scene kitsune with pixellate
    "Instead, what pierced my vision was the silhouette of someone sitting in front of me."
    "They were sitting in front of an open door overlooking several hills, with the sun setting behind them."
    "No matter how hard I gazed at them, they were nothing more than a shadow in front of me, with only their body features visible."
    "Examining them, I saw that they had the features of a fox, with a long tail and pointed ears."
    myst "Hehe~"
    myst "Don't worry, I'm not going to hurt you."
    "The figure in front of me was drinking from a cup of tea. The voice was clearly feminine, and I felt an odd sense of comfort upon hearing it, easing my tension."
    mc "...who are you?"
    myst "Oh, you'll find out in due time~"
    "She took a sip from her cup, speaking calmly. I could almost feel a smile on her face, despite not being able to see it."
    myst "...you've had a rough life, haven't you?"
    myst "Losing your parents before becoming an adult..."
    myst "Moving to another city and having to start over..."
    myst "It's all very tough, isn't it?"
    myst "..."
    myst "But don't worry, so long as you live in this house, you'll always be under my protection."
    "As she said those words, my vision started to fade, the figure receeding from me. Before I woke up, I tried to ask one more question."
    mc "W-wait! Will I see you again?"
    scene black with fade
    hide kitsune with fade
    "My vision was almost completely black as the figure spoke once more."
    myst "..."
    myst "Yes, I'm sure we will meet again."
    myst "Until then, farewell..."

    
    stop music fadeout 2.0
    pause 3
    play sound "audio/alarm.mp3"
    pause 3
    stop sound fadeout 2.0
    scene room with pixellate
    play music "audio/mainstreetstroll.ogg" loop

label day2morning:

    "The shrill sound of my alarm clock pierced my ears, and I quickly sat up in bed."
    "Turning the alarm off, I sat in bed thinking about the dream I had just awoken from."
    mc "Who was that...? And was it really just a dream?"
    "Chalking it off to nerves and being in a new place, I pushed the dream to the back of my mind and got out of bed, heading to the bathroom to take a shower."
    show steamoverlay with fade

    play sound "audio/shower.ogg"

    "I thought about the upcoming day I would have at school soon."
    "I was hoping that I would be able to slip into the background, avoiding any attention from others."
    "It wasn't necessarily my intentions to make friends or be the center of attention, and I mostly just wanted my last year in school to be over."
    "I also knew that if I was probed about my circumstances I would have to explain what had happened, and I wasn't too keen on reliving that."
    mc "Well, there's no point in worrying about it now."

    stop sound fadeout 2.0
    hide steamoverlay with dissolve

    "Turning off the shower, I stepped out and dried myself off."
    "I wrapped a towel around my waist and started to brush my teeth, making myself presentable for the day."
    "I walked back into the bedroom, searching for the uniform I had been given before I arrived at my new home. Putting it on, I walked into the kitchen, looking in the fridge for a sandwich I had grabbed before getting on the train."
    "I grabbed my bag and started walking out the door, making my walk to the school."

    scene street2 with dissolve
    hide room

    "The walk was a relatively short one, only taking about 30 minutes from my house."
    "On my way there, I made my way through a residential area, the road lined with modern looking houses with stores littered around."
    "I saw a few people wearing the same uniform as me walking to school, some of them talking to each other."
    "Already I could see the personalities of a few of them: a group of boys laughing as they pestered some girls, another group of girls giggling at the sight."
    "Since the school was relatively large, it was likely these students were in the same class, perhaps in mine."
    "Fortunately, nobody seemed to notice me despite wearing the same uniform as them, and I continued my walk alone and uninterrupted."
    "More and more students started to fill the streets as I drew closer to the school, and eventually I arrived at the gates."
    scene gate with dissolve

label madokaintro:

    "I looked at the school in front of me, the somewhat large building having a few floors and a courtyard that had a lot of room and continued on around the sides of the school."
    "More students were walking around in front of the school building, talking amongst each other and making various sounds as they waited for the bell to ring."
    "I pulled a piece of paper out of my pocket, examining the schedule I had been given."
    "I searched for the room my homeroom was in and checked the time, with only a few minutes left until the bell rang."
    "I started to make my way towards the building, but suddenly I heard a noise coming from my left side. And fast."
    "Before I could react, the sound and the person it belonged to were already on me."
    play sound "audio/impact.ogg"
    myst "Excuse me! Coming through! Watch out! Hey, get out of the-"
    "I felt a force crash into me, being knocked onto the ground as I saw the other person fall as well."
    "I slowly started to get back up and looked over the figure on the ground."
    show muramoto uniformarmupl uniformarmdown hit with moveinbottom
    myst "O-ow..."
    "The figure on the ground was a blonde girl, with a uniform that was similar to mine."
    "They looked to be the same age as me, and she was rubbing her head as she winced her eyes."
    show muramoto uniformarmupl uniformarmdown dizzy
    mc "Are you alright? Seems like you hit me pretty hard."
    "I picked up her belongings that had fallen on the ground and offered a hand to her, with her finally opening her eyes and looking up at me."
    show muramoto uniformarmdownl uniformarmdown concentrate
    "The first thing I noticed about her was that her eyes were two different colors: her left eye was a bright blue, while her right eye was an almost golden color."
    "I couldn't tell if they were contacts or if it was her natural eye color, but it was definitely something I hadn't seen before."
    myst "Y-yeah, I'm fine. Thanks for helping me out."
    show muramoto uniformarmdownl uniformarmdown phew
    myst "I just didn't want to be late to my class today, so I ran all the way to school. Guess I should pay more attention to where I'm going, ehehe..."
    show muramoto uniformarmdownl uniformarmdown neutral
    myst "Hey, wait a minute..."
    "She looked at me for a moment, and I could see her eyes darting around my face."
    "For some reason, I felt slightly nervous, like she was trying to get a read on me."
    "She continued this for a few seconds, making me more and more uncomfortable."
    mc "Err..."
    myst "Wait! I've got it. You're new here, right?"
    show muramoto uniformonhipl uniformonhip cat
    "Her expression instantly changed after she asked me that, taking on a more cheerful appearance and smiling at me."
    mc "Uhh- y-yeah! I got here yesterday, actually. It was lucky the school was on holiday whenever I got here, or else I'd have to start in the middle of a week..."
    "She nodded as she listened to me, still maintaining eye contact with me."
    myst "I see, I see... hmm hmm..."
    show muramoto uniformpenl uniformonhip smiling
    ma "Well, it's good to meet you! I'm Madoka, last name Muramoto. I'm a student here, as you can tell."
    show muramoto uniformpenl uniformonhip cat
    ma "Well, you're lucky you came across me first! I'll provide all the protection you need, newbie!"
    mc "Thanks..."
    "Despite the girl being clearly smaller than me, she still had a lot of energy and seemed to be able to hold her own if it came to it."
    "Maybe it would be wise to keep someone like this by my side for a bit, at least until I got used to the school."
    mc "Well, my name is [mcname]. It's good to meet you."
    play audio bellsound
    "Suddenly I heard the sound of the bells ringing, indicating that the school day had started."
    show muramoto uniformpenl uniformonhip hit
    ma "Ah! I need to get to my classes before I'm late again! Well, I'll be seeing you again soon! Bye!"
    hide muramoto with moveoutright
    "The energetic girl took off with a quick goodbye, practically sprinting across the courtyard to get into the school."
    "I sighed and walked towards the school, heading to my new homeroom."
    mc "Well, that was certainly an interesting first experience..."
    stop music fadeout 4.0
    scene classroomfunny1 with fade
    play music "audio/basemusic.mp3" fadein 3.0 loop
    "As I entered the school, I looked for my new homeroom. Following the plaques above the doors, I walked down the hallway filled with students until I found it."
    "Falling behind the other students, I entered the classroom, looking around for an open seat."
    "As I did so, I noticed a hand waving. Realizing it was directed towards me, I turned and looked to see that Madoka was waving towards me."
    show muramoto uniformarmupl uniformarmdown smileclosedeyes
    ma "Heey! Over here!"
    "As soon as I looked towards her, she motioned to an empty seat next to her."
    "Despite the noise of several students talking in the classroom, I could hear her voice clearly. I made my way over to her, taking a seat next to her and setting my bag down."
    # keep yourself safe :)
    mc "So, we're in the same homeroom, huh?"
    mc "Guess I'll be taking up your offer of protection, whether I want it or not..."
    hide muramoto 
    show muramoto uniformcrossed speakinghappy
    ma "Well, it wasn't an offer... but I'm glad you've accepted it!"
    "She smiled as I talked with her, clearly engaged in our conversation. It was like this was the first time someone had ever interacted with her with the way she was excited."
    mc "I hope you don't mind me asking, but... are you wearing colored contacts? Or are those your, er, actual eyes? No offense."
    show muramoto uniformcrossed cat
    ma "Well, as long as you're respectful, I don't mind at all! Truthfully, these are my real eye colors. No contacts necessary!"
    show muramoto uniformcrossed phew
    ma "To be honest, you're the second person who hasn't treated me different or given me a strange look."
    show muramoto uniformcrossed neutral
    ma "So... thank you."
    "This time her expressions was much more somber, behind her cheerful expression lying the face of someone who has clearly never fit in."
    mc "Well, consider it a thanks for helping me around here."
    mc "So, second person, huh? Who would be the first?"
    show muramoto uniformcrossed speakinghappy

label natsukiintro:

    ma "Well, why not meet her yourself?"
    "At that moment, another person had walked towards the area we were sitting, clearly going to talk to Madoka."
    show muramoto uniformcrossed smiling at right with moveinright
    show natsuki uniformhandsdown at left with moveinleft
    "As with Madoka, she had features that immediately stood out to me. Sitting on top of her head were a pair of cat ears."
    "For obvious reasons, these were easier to tell as being an accessory compared to Madoka's differing eye colors, but nevertheless I was taken aback by the sight."
    "But, as I looked at her, something stirred in the back of my mind. The feeling was similar to the sense of Deja vu I had felt on the train coming here."
    myst "Madokaaa! Hehe, you're here early-"
    show natsuki uniformhandsdown concern at left 
    "The girl noticed my presence, immediately stopping in the middle of her sentence. She stood frozen for a moment before Madoka spoke again."
    ma "Oh, Natsuki! This is someone I met this morning! Well, {b}ran{/b} into, but whatever! Say hi!"
    mc "Uh, hi. Nice to meet you. I'm [mcname]."
    "Natsuki's eyes widened as I said my name, speaking to me in an almost awe-struck tone."
    na "[mcname]?! Is it really you?"
    show natsuki uniformhandsup speaking at left 
    "The girl ran up to me and hugged me tightly as I sat there stunned."
    "Yet again I had the same feeling as earlier, trying desperately to figure out what it was."
    "And then a thought came to me: this hug is familiar. At this moment, I had something I desperately needed to ask her."
    mc "Natsuki... I know you, don't I?"
    show natsuki uniformonehand speaking at left
    na "Y-you remember, right [mcname]? It was so long ago when you moved away... I never thought I'd see you again!"
    "It was then that I finally realized why I had felt that way. Natsuki... was my childhood friend."
    mc "Of course I remember! How could I forget... We were together so often! I remember everything we did together. It's... incredible, seeing you here."
    "I hugged her back, the three of us smiling at this unexpected reunion."
    "Finally, Natsuki let go, taking her seat in front of Madoka and continued our conversation."
    show natsuki uniformbehindback at left
    na "So... what brought you here? I thought you and your parents had gotten that job and moved away?"
    show fade with fade
    $ renpy.music.set_volume(0.10,0,"music")
    "..."
    "I knew this would happen."
    "There's no way I could tell the truth. Not now."
    "I can't ruin this moment. Especially not for Natsuki."
    "It was at this moment I told my first lie."
    hide fade with fade
    $ renpy.music.set_volume(1,0,"music")
    mc "W-well, they had to go overseas for a bit, so I'm living on my own until I finish school."
    "I managed to keep a straight face as I made an excuse, seemingly convincing them."
    hide muramoto
    show muramoto uniformonhipl uniformonhip speakinghappy at right
    ma "Well, aren't you lucky! Living all on your own..."
    play audio bellsound
    "Suddenly, the bell rang, and the remaining students sat down in their desks as they waited for class to begin."
    hide muramoto with dissolve
    show natsuki uniformbehindback bleh at left
    na "Talk to you later, okay?"
    hide natsuki with dissolve
    "Natsuki smiled at me and turned around to the front, where we all waited for the teacher to enter."

label harumiintro:
    show harumi dresshandsdown with dissolve
    ha "Hello everyone, I hope everyone had a good break."
    show harumi dresshandsdown speaking
    ha "Today, before class starts, I'd like to make an announcement."
    "The teacher looked back towards me, smiling."
    show harumi dressonehand speakinghappy
    ha "I would like everyone to meet our new student. Mr. [mcname], if you would please stand up and introduce yourself."
    show harumi dressonehand happysmile
    "I stood up, thinking for a moment before speaking."
    mc "Hello everyone. My name is [mcname]. I just moved here, so I'm new to this area. I hope that you will all accept me and that we can all get along. Thank you."
    "I sat down, the class clapping after I finished speaking. Madoka looked at me and smiled, reassuring me."
    show harumi dressonehand speakinghappy
    ha "Thank you, Mr. [mcname]. Now that's sorted, I would like to ask you all a question, to see if any of you actually did your homework."
    show harumi dresshandscrossed speaking
    ha "Between music, theater, and chariot racing, which sport did Nero win when he participated in the Olympics?"
    "The classroom was quiet for a moment before two people a few rows in front of me raised their hand. The teacher looked between them and eventually called on one."
    ha "Yes, Mr. Kazumi?"
    show harumi dresshandscrossed speaking at left with moveinleft
    show tashiro uniformcrossed speaking at right with moveinright
    ta "The answer is that he won all of them."
    show harumi dresshandscrossed speakinghappy at left
    show tashiro uniformcrossed smile at right
    ha "Very good! Nero did in fact win every sport he participated in, though whether or not he {i}deserved{/i} to win those is a different story. Now, I want everyone to turn to page 143..."
    hide harumi
    hide tashiro
    show muramoto uniformcrossed pout with dissolve
    ma "Geez, Tashiro, save some for the rest of us..."
    mc "Who was that?"
    show muramoto uniformcrossed neutral
    ma "Tashiro Kazumi. Friggin genius is what he is. Him and his twin sister are at the top of everything they participate in. Me, I'm half convinced they're just aliens with really good social skills."
    mc "I see..."
    hide muramoto with dissolve
    "The lesson continued like usual, and despite the fact that I started in the middle of the year, I somewhat understood the topics of the lesson."
    play audo bellsound
    "Finally, the bell rang, signalling me to go onto my next class, which would be my gym class."
    stop music fadeout 3.0
    scene outside with dissolve
    play music "audio/mainstreetstroll.ogg" fadein 3.0

label isaintro:
    
    "I walked around outside the school for a bit, trying to find where the changing rooms where. I had been in several directions, but always ended up back in this same spot."
    "I stood in front of the tree, muttering under my breath."
    mc "Where else could it be...?"
    mc "Suddenly, I felt a presence behind me. As I turned around to face the presence, I heard them speak."
    myst "Are you lost?"
    show isa uniformarmscrossed neutral with dissolve
    mc "Oh, uh... yeah, I'm trying to find the changing rooms. Do you know where they are?"
    show isa uniformarmscrossed 
    myst "Ah, I was just heading there. If you'd like, I can lead you there. I don't blame you for being lost, the school has them in a weird spot."
    ik "I'm Isa Kazumi by the way. Nice to meet you. Heard you were a new transfer student, right?"
    mc "Oh, are you in my home room as well? I think I'm in the same one as your brother. Good to meet you as well, I'm "
    show isa uniformhandsdown sus 
    ik "Yeah, I'm in the same class as Tashiro. How do you know him by the way?"
    mc "Oh, er, someone I was sitting next to told me. Said he was a genius."
    show isa uniformarmscrossed neutral
    ik "Well, if you lived with him, you certainly wouldn't think that way... Yeah, I saw who you were talking to when you sat down. Sorry you got put with the weirdos. Anyway, lets go."
    hide isa with dissolve
    scene schoolcorridor with fade
    "I followed her to the changing area, where there were separate rooms for boys and girls."
    show isa uniformhandsdown with dissolve
    ik "Here we are. See you later. If you see my brother, don't be afraid to say hi."
    hide isa with dissolve
    "We parted ways as I walked into my changing room, changing into more athletic clothes."
    scene schoolcorridor with fade
    "After working out during the class, I changed again and stepped back outside, waiting around before it was time to go back to my homeroom and eat lunch."
    "Leaning against a pillar, I could see people walking around, with boys doing similar things as me and waiting around."
    "However, as I was scanning all of the crowd, my eyes fell on the person who had answered the question during class, with their eyes also looking at me."
    "As we made eye contact, they waved and said something to the people they had been talking to before walking over to me."

label tashirointro:
    show tashiro uniformpockets speakinghappy with dissolve
    ta "Hey! You're that new kid right? I saw you out there... you're surprisingly athletic! Nice to meet you, I'm Tashiro."
    mc "Uh, thanks? I'm [mcname]. It's good to meet you too."
    "Talking to him, Tashiro was surprisingly tall, likely standing around 5 feet and 11 inches or even 6 feet tall. He was lean, not quite thin. His voice was unsuprisingly deep, yet it also sounded gentle."
    show tashiro uniformcrossed 
    ta "So, how are you finding it here? Pretty nice school, huh? Pretty easy to find everything?"
    mc "Well, overall it's been good. Had some trouble finding these changing rooms though. Luckily, I ran into your sister and she pointed me in the right direction."
    show tashiro uniformpockets thinking
    ta "Ah... well, at least you found it."
    show tashiro uniformpockets smileclosedeyes
    ta "And sorry you had to deal with Isa! Haha-"
    show tashiro uniformpockets sad 
    ta "Ow!"
    show tashiro uniformpockets sad at left with moveinleft
    show isa uniformarmscrossed neutral at right with moveinright
    ik "Didn't anyone tell you to speak like someone is always listening?"
    "The two twins stood in front of me, bantering with each other. Well, mostly Isa was doing the insults, with Tashiro being the unfortunate recepient."
    "Isa stopped messing with her brother and turned to me, speaking."
    show isa uniformhandsdown at right 
    ik "Sorry you have to deal with {i}him{/i}. Hopefully he hasn't been a bad influence long enough and you can still be saved."
    show tashiro uniformcrossed thinking at left
    ta "If anyone is a bad influence, it's you, beloved sister..."
    "He lightly chopped her on the head, his height difference preventing her from doing the same."
    play audio bellsound 
    "Before Isa could respond, the bell rang, signaling lunch break."
    show tashiro uniformcrossed speakinghappy at left
    ta "Well, it was good to meet you [mcname]. Oh, one more thing!"
    ta "We've got an extra space for you if you want to eat lunch with us! We'd be happy to welcome you on your first day!"
    ta "See you later!"
    hide tashiro with dissolve
    "He waved at me as he walked away, heading back with the group he was in before he left to talk to me."
    show isa uniformhandsdown smile
    ik "Well, guess it's the same for me. Be seeing you. Don't sleep on his offer."
    hide isa with dissolve
    "The encounter with the siblings was certainly unique. Though they seemed to constantly be at odds with another, I could tell that deep down they still shared that special bond of siblings."
    "I headed back to my homeroom, my stomach rumbling and ready to eat."
    scene classroomfunny1 with fade
    stop music fadeout 3.0
    play music "audio/basemusic.mp3" fadein 3.0 loop

label lunchchoice:
    "I went back into the classroom, ready to eat my lunch. I made my way back to my seat and pulled out my lunch, thinking about what to do next. Madoka and Natsuki weren't in the class yet, and I assumed they would eat in their usual seats."
    "In that case, I could either stay here and eat with them, or go over to eat with Tashiro and Isa."
    menu:
        "Eat lunch with the twins.":
            "I felt it would be interesting to eat with twins on my first day, so I stood up and headed over there."
            $ twinslunch = True
            jump lunchtwins
        "Eat lunch with Madoka and Natsuki.":
            "Since the two had welcomed me into their small group already, I felt it would be safe to stay here and socialize with them more."
            $ madokalunch = True
            jump lunchmadoka

    label lunchtwins:
        show isa uniformhandsdown speakinghappy at left with dissolve
        show tashiro uniformpockets speakinghappy at right with dissolve
        "Walking over there, the two were seemingly already in a conversation. However, Tashiro soon saw me walk up, and stopped talking to speak to me."
        show tashiro uniformpockets smileclosedeyes at right
        ta "Hey [mcname]! Good to see you again. Glad you took me up on my offer."
        show isa uniformpeacesign smileclosedmouth at left
        ik "Hey, don't leave me out of this too. Good to see you as well [mcname]."
        mc "Well, I thought I'd take you up on the offer. Not every day I get to speak with people as high ranking as you two."
        show tashiro uniformcrossed speakinghappy
        show isa uniformarmscrossed blushclosedmouth
        ta "Well, there's no need to speak so highly of us, heh. We're all students here after all!"
        "Tashiro laughed and smiled at me while Isa smiled, all of us sharing a moment together."
        "Surprisingly, I seemed to be getting along well with these two, despite only being here for one day. Tashiro seemed to be the kind of person who goes out of their way to talk to everyone, making sure they felt welcome."
        "Isa seemed to be a mix of both introverted and extroverted, as while she seemed to be okay with my presence she only responded in single sentences."
        "Though, this did seem to change as all three of us 'warmed up' to each other, as she gradually started to talk more and more."
        play audio bellsound
        "Inevitably, the bell rang, a sign of the end of lunch break."
        mc "Well, it was nice to chat with you two for a little bit. See you later?"
        show tashiro uniformpockets smile
        show isa uniformpeacesign smile 
        ta "Of course! If you ever need anything, let me know!"
        ik "Same thing here. See you later, [mcname]."
        hide isa with dissolve
        hide tashiro with dissolve
        jump postlunch

    label lunchmadoka:
        "After all, it would be nice to get to know Madoka better, and I'm sure me and Natsuki have a lot to catch up on."
        "Shortly after, Madoka and Natsuki walked over, taking a seat in their usual spots."
        show muramoto uniformonhipl uniformonhip speakinghappy at left with dissolve
        show natsuki uniformbehindback at right with dissolve
        ma "Well well! If it isn't Tashiro in the flesh! Decided to have lunch with little old me and Natsuki, huh?"
        mc "Well, is that not the first rule of life? Always pay back your debts."
        show muramoto smileclosedeyes
        ma "Attaboy! I see you are already wise beyond your years."
        show natsuki speaking 
        na "Well, he's always been like this! I remember when we were younger, he always used to act like an old wise sage with mystical powers!"
        mc "Haha, well... That was a while ago, Natsuki. I don't act like that anymore... right?"
        show natsuki bleh
        na "We'll see about that!"
        "We all laughed at the same time, me and Natsuki reminiscing about the past as Madoka laughs at our youthful silliness."
        show muramoto phew
        ma "This is the first time in a while I've eaten with people other than Natsuki..."
        show muramoto smiling
        ma "You seem like a really nice guy [mcname]. And I'm sure Natsuki can back me up on this."
        show natsuki uniformonehand smileclosedeyes
        na "I can. Tashiro was always looking out for me back when we went to the same school."
        show natsuki smileclosedeyes uniformcheer
        na "Hehe, you better be doing the same now!"
        play audio bellsound
        ma "Well, thank you for eating with us. See you later alligator!"
        hide muramoto with dissolve
        show natsuki uniformbehindback
        na "Yep, we'll be seeing you!"
        hide natsuki with dissolve
        jump postlunch
    
label postlunch:
    "After the lunch period was over, we continued on with the lesson, each bell signalling the end of the day drawing closer."
    "I could see more and more students get restless as they watched the clock tick nearer to the end."
    play audio bellsound
    "Finally, the final bell rang, the school day finally ending."
    "As the students stood up and gathered their things, the teacher spoke once more."
    show harumi dressonehand speakinghappy with dissolve
    ha "Don't forget to finish your assignments due tomorrow! Have a good day everyone~"
    hide harumi with dissolve
    if twinslunch:
        show isa uniformpeacesign with dissolve
        ik "Have a safe trip back. See you tomorrow."
        mc "Thank you Isa, see you tomorrow!"
        hide isa with dissolve
        jump walkhome
    if madokalunch:
        show muramoto uniformpenl uniformonhip cat with dissolve
        ma "Have a safe trip back! See you tomorrow, bud!"
        mc "Hah, thank you Madoka. See you later!"
        hide muramoto with dissolve
        jump walkhome
label walkhome:
    stop music fadeout 3.0
    scene street2 with fade
    play music "audio/mainstreetstroll.ogg" fadein 3.0
    "The walk back home was relaxing after a long day at school."
    "Retracing my steps back to my home was relatively easy, even with the swarms of students on the streets."
    scene countryside1 with dissolve
    "The amount of people started to slow as I reached the road that headed to my house, soon walking on my own back home."
    scene room with dissolve
    "I set my bag down and laid down on my bed, stretching out."
    scene room with fade
    "Before I knew it, I had fallen asleep, and when I woke up I had been asleep for an hour."
    mc "Didn't know I was that tired..."
    "Changing into some more comfortable clothes, I then picked up my bag and moved to my desk, working on the assignments that had been given to me."
    "After doing that for a few hours, I went into the kitchen to cook something with the groceries I had brought."
    "I would need to go to the store tomorrow, but for now these would cut it."
    "After cooking and eating, it was already starting to get late, so I decided to take a shower and get into bed."
    "Setting my alarm, I thought about the dream I had last night."
    "I wondered how my brain could've made something like that up, but I chose not to question it that much."
    "Turning off the lights and lying down, I soon drifted off to sleep once again."

label dream2:
    stop music
    scene black with fade
    stop music
    scene kitsune with pixellate
    play music "audio/At our parting.mp3" fadein 3.0
    myst "My, my..."
    myst "It looks like you've made it here much earlier than I thought you would."
    myst "So, I think we'll have a bit longer to talk about things."
    myst "I'm sure you have many questions, hm?"
    "This dream again... This time, though, I didn't feel as surprised or nervous. I wondered if this would become a recurring dream."
    "Or... was it even a dream? I shouldn't have this much control, unless it was a lucid dream. But even if it was, I can't change anything in here."
    "Nevertheless, I decided to speak to the figure in front of me once again."
    mc "Who are you? You haven't even told me your name."
    myst "Tsk, tsk... Always you humans with these pesky names."
    myst "I do have one, but it has not been used in a very, very long time... Well, perhaps I will tell you in due time."
    mc "I... see."
    mc "...wait, what do you mean by a very long time?"
    myst "Hmm, you really can't tell? Perhaps I have retained my youthful looks, hehe~"
    myst "Well, since you're not sure, I'll go ahead and tell you. I'm a kitsune; that is, a fox spirit."
    mc "A... kitsune? Like, the ones in all those old stories?"
    myst "Well, they're not just stories~ But that's an explanation for another time."
    myst "As long as you're in this house, I will protect you."
    "The spirit spoke in a more serious tone now, speaking firmly yet still retaining her kind aura. Soon, however, she relaxed again, smiling at me."
    myst "Well, it looks like our time is running out again. Perhaps we'll meet again. Farewell~"

label day3morning:
    scene black with fade
    stop music fadeout 2.0
    pause 3
    play sound "audio/alarm.mp3"
    pause 3
    stop sound fadeout 2.0
    scene room with pixellate
    play music "audio/mainstreetstroll.ogg" loop
    mc "Urghh..."
    "Rolling over and turning off my alarm, I sat on the side of my bed, thinking."
    "Now, I was sure that this wasn't a dream. I had never really been too into the concept of supernatural things, but I never discounted the possibility."
    "I had always been a bit of a skeptic, but I had to admit that this was a bit too much to be a coincidence."
    "I wasn't exactly sure what she meant by protecting me. This house hadn't exactly been lived in for a while, and I wasn't sure if it had any history."
    "Nevertheless, I brushed it off and decided to get ready for the day. Today was Saturday, which meant I would get tomorrow off."
    "I had no plans for my break, so I thought that it would be a good opportunity to explore the town a bit more."
    "But that was a discussion for tomorrow. For now, I had to get ready for school."
    scene room with fade
    "After taking a shower and brushing my teeth, I got dressed and headed downstairs."
    "I grabbed a granola bar to eat on the way, then headed out the door."
    scene street2 with fade 
    "I started walking down the street, heading towards the school."
    "But on the way there, I saw a familiar figure standing, looking like they were waiting for something."
    "The figure looked up and turned towards me, yelling."
    show tashiro uniformpockets smileclosedeyes with dissolve
    ta "Heey [mcname]! Fancy meeting you here, eh?"
    "I walked over to where he was standing, responding to his greeting."
    mc "Hey Tashiro, what are you doing here?"
    show tashiro uniformpockets speakinghappy
    ta "Well, I live on this street of course. Looks like you do too, huh?"
    mc "Well, more or less. I'm down over that hill on the countryside."
    show tashiro uniformcrossed speakinghappy
    ta "Makes sense. Right now I'm just waiting on my sister to get ready. You know how women are, haha!"
    "He lightly hit my shoulder, laughing and prompting me to smile as well."
    ta "So, mind if we walk with you today? I'm sure she'll be ready soon."
    mc "Sure, no problem. I'm not in a rush."
    "We waited on the street for a little bit longer, and soon Isa met up with us on the street."
    show isa uniformarmscrossed speaking at left with moveinleft
    show tashiro uniformcrossed speakinghappy at right with moveinright
    ik "Thanks for waiting on me."
    show isa uniformarmscrossed speakinghappy
    ik "Hey [mcname], I'm surprised to see you here."
    mc "Well, as I've found out with Tashiro, it looks like we live in the same area."
    show isa uniformhandsdown smileclosedmouth
    ik "Right, I thought I had noticed someone moving into that house down there. Well, shall we head out?"
    ta "Sure, let's go!"
    hide isa with dissolve
    hide tashiro with dissolve
label day3class:
    stop music fadeout 3.0
    play music "audio/basemusic.mp3" fadein 3.0
    scene classroomfunny1 with fade
    "Taking a seat in my chair, I looked around the room."
    "Mostly everyone had arrived, but there were still a few people missing. Most notably, the one who should be sitting in front of me."
    "Just as I started to wonder where she was, she burst through the door right as the bell rang."
    play audio bellsound
    show muramoto uniformarmdownl uniformarmdown phew with dissolve
    "With a satisfied expression, she made her way towards her seat. Out of breath, she spoke to me."
    ma "Haah... I barely made that one!"
    show muramoto uniformarmdownl uniformarmdown speakinghappy
    ma "Well, [mcname], aren't you an upstanding citizen for being early, eh?"
    mc "I wouldn't say it like that, but I appreciate the compliment."
    "She smiled at me, then sat down in her seat."
    "Soon after, the teacher walked into class and started to speak."
    hide muramoto with dissolve
    show harumi dresshandscrossed speakinghappy with dissolve
    ha "Good morning, class. I hope you all slept enough to pay attention today."
    ha "Now, to start off class, I have a question for someone I will randomly pick to answer."
    show harumi dressonehand speaking
    ha "What do we call the phenomenon where believing in a treatment’s power is enough to improve your condition?"
    ha "Now... [mcname], do you have an answer for this?"
    mc "O-oh, of course. It's called..."
label classchoice1:
    menu:
        "The mandela effect.":
            mc "The mandela effect."
            jump wrongchoice
        "Deja vu.":
            mc "Deja vu."
            jump wrongchoice
        "The placebo effect.":
            mc "The placebo effect."
            $ answeronecorrect = True
            show harumi dresshandscrossed happyopenmouth
            ha "That's correct, [mcname]! Good job."
            jump afterclasschoice1
    label wrongchoice:
        show harumi dresshandscrossed speaking
        ha "Good guess, [mcname], but that's not quite right."
        ha "The answer I was looking for was the placebo effect."
        jump afterclasschoice1
label afterclasschoice1:
    show harumi dresshandscrossed speaking
    ha "Some of you may have heard of this before, but it's a very interesting concept."
    ha "In essence, it's the idea that the mind can have a powerful effect on the body."
    ha "For example, if you believe that a certain pill will cure your headache, then on some occasions, it will."
    ha "Often, this is used in medical trials to test the effectiveness of a new drug."
    ha "People undergoing the trial are split into groups, with one group receiving the drug and the other receiving a placebo, which is basically a pill that does nothing."
    ha "The results are then compared to see if the drug is actually effective."
    ha "But it's not just limited to medicine. It can also be used to test the effectiveness of other things."
    ha "Interestingly, the word 'placebo' comes from Latin, which means 'I shall please'."
    ha "It was taken from a 4th century translation of the Bible, in which it is used to describe a deceptive act to please."
    ha "Often, it was used by those who claimed a connection to deceased individuals to get a share of the funeral meal."
    show harumi dresshandsdown 
    ha "Now, take out your textbooks and turn to page..."
    "The rest of the class went by without much incident."
    play audio bellsound
    "The bell rang for the next period, and I moved on with my day."
    play music "audio/mainstreetstroll.ogg" fadein 3.0 loop
    scene schoolcorridor with fade
    "One of my classes was not going on today, so I had a break period."
    "As I was walking to the courtyard, though, I saw someone standing against a pillar, their head turned down looking at their phone."
    "Upon closer inspection, I realized that it was Natsuki."
    "I wasn't sure if I wanted to "
    





    # This ends the game.

    return
