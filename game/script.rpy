# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character(None, kind=nvl, what_color='#000000', size=12)


label end:
    return
    
# The game starts here.

label start:
    define menu=nvl_menu

    scene todo

    "There is this book, you see, and it says that our civilization sucks. Not that it's news to anybody with a pair of eyes, what with all the climate change, sexism and African child soldiers."
    "The weird part is that it all has to do with technology. Think of it: why does the climate change even exist? Because we burn a few tons of oil every time some rich asshole wants to chill at Goa or something."
    "Why is Congo such a hellhole? Because they mine something called coltan in there, which is really useful for making electronics, and slaves are cheaper than all that mining machinery. Yep, you can have an iPhone because some child was whacking stones with a pickaxe all day long, while a slightly older child kept him at gunpoint."
    "And then some other child in China assembled them all day for a bowl of rice. That's capitalism for you."
    "As for the sexism, well, you're not sure, but it probably has something to do with capitalism, which very definitely has something to do with technology."
    "But the book does more than just state the obvious. Well, it doesn't mention the iPhones either, because they weren't around back in eighties."
    nvl clear
    "The book says that this shitty civilization of ours can be destroyed pretty easily."
    "Not like \"burned in the nuclear flames\", that would do nobody any good. More like rebooted, started anew. You just need to find the vulnerable spots. Those oil pipelines, for example."
    "Blow up one of them and half the Europe has no more oil, which means that in two weeks all the cars and tanks and stuff would be just sitting there gathering dust."
    "Or take power plants. They take years to build, but can be blown up in a minute. Bang, good news everyone, welcome back to the pre-Industrial age."
    "Of course, there is redundancy. But if enough of these things are hit at once, the entire system overloads and collapses. The humanity gets a chance to build something better the next time."
    nvl clear
    "And that's what you set out to do."
    "Not alone, of course. But the Internet is definitely among the better inventions of a capitalist civilization. There are about a thousand of you, all over Europe."
    "Sure, some of them are pretty weird. The Belarussian who erects Perun totems in his dacha. Or the guy who believes that he met Stanley Kubrik in Byla Reka. That one Goth girl who once sacrificed a cat to her late grandmom."
    "Basically, half of your co-conspirators belong in a madhouse. But whatever, so would Ghandi, come to think of it. Their bombs are as good as yours."
    nvl clear
    "Now, the thing about bombs. They blow up exactly once, if they blow up at all, so you only get one shot."
    "If you build your bomb right, you get to choose where and when that happens. Not how big the explosion is, not what it does or doesn't damage. Not even whether it kills you or not."
    "Which is actually a concern. You can't just mail the bomb to the nearest hydroelectric dam and expect them to kindly place it under the generator. Therefore, you need to walk (or drive, or whatever) to where you need it to be, place a bomb, run away and send the SMS. Skip the running away part if the place has no reception. So it goes."
    "If you really need to break some eggs to make omelet, it's only fair for these eggs to be yours."
    "By the way, in Russian that would be a really bad pun. Very unsuitable for a civilization-shattering terrorist."
    "No. Really."
    "You also have a dead man's switch. The moment your fitness tracker stops reporting heartbeat, the bomb goes off."
    "Hopefully."
    nvl clear
    scene plant
    "You take the last bus to Crvona Gora, wait for any overtimers from day shift to jump in and start walking."
    jump perimeter
    
label perimeter:
    "The Crvona Gora power plant is surrounded by one of those Soviet concrete walls, covered in dirt and graffiti. Rusty barbed wire runs on top, but the lights are mostly out."
    "The perimeter defense appears to be just a single old lady sitting in her booth, watching TV."
    menu:
        "Approach the booth":
            jump guard_dialogue
        "Walk along the perimeter":
            "The guard looks out of her window and shouts:"
            " — Hey you! The tourist! Come over here."
            "You don't see any tourists around, so she probably means you."
            jump guard_dialogue
        "See if you can climb a wall":
            "The barbed wire seems to be broken in a spot about five meters from the booth. Do you try and climb there?"
            menu:
                "Yes":
                    "You notice a flash from somewhere inside the walls and everything goes dark. At least maybe the dead man's switch will work."
                    jump booth_blown
                "No":
                    "Maybe it's a single old lady, but she doesn't have to be a genius to see some guy on the wall and raise alarm."
                    jump perimeter
    label guard_dialogue:
        nvl clear
        "From a distance the guardwoman seemed almost senile, but on closer inspection she turns out to be about fifty, and probably ex-police."
        "She doesn't carry a gun, but somehow you feel that she would know what to do with one."
        " — So what exactly are you doing around here in the middle of the night?"
        menu:
            " — You see, my uncle works here, in the HR department...":
                " — You see, my uncle works here, in the HR department..."
                " — HR? At half past midnight? Now stay where I can see you while I call the police."
                menu:
                    "Blow up the bomb":
                        jump booth_blown
                    "Wait":
                        jump early_arrest
            " — Well, I was looking for the bus station...":
                " — Well, I was looking for the bus station..."
                " — The last bus was an hour ago. Now, you turn left from the post, walk along the trail, turn right when it forks, and in five minutes you'll be on the road. Turn left, the town is about ten kilometers that way. Maybe you'll get lucky and catch a car. And don't hang around unless you want to tell the police what's your business with the facility."
                "..."
                "Yes, they probably won't like it if you do. You thank the guard, leave her booth and turn left."
                jump arrest
            "Blow up the bomb":
                jump booth_blown
            
    jump arrest
    
label booth_blown:
    nvl clear
    "You blow up the booth, the guard and yourself. It's not exactly destroying the industrial civilization, but it's better than nothing."
    "You don't live to know it, but two minor Islamic terrorist organisations claimed responsibility for your attack. ISIS, Al-Qaeda and all the big boys did not."
    "Conspiracy theorists spend the next decade debating whether or not this explosion was related to three other attacks in Eastern Europe that night."
    jump end

label early_arrest:
    nvl clear
    "You get ten years for the attempted terrorist attack."
    "It's a weird sentence. On one hand, it is too much. All you ever wanted was to help the humanity, and now you have to spend a decade with common murderers."
    "On the other, some of these murderers have gotten a decade for a bar brawl gone wrong. Is a man who aspired to change the world really the same as some lame trigger-happy alcoholic?"
    "You spend your days writing letters to Unabomber. After a fourth one, he calls you an idiot and stops responding."
    jump end
    
label arrest:
    nvl clear
    "You do as she says, but turn left at the fork. In fifty meters, the trail comes to a hole in the wall; by the look of it, it was here since before you were born."
    "It's obviously still in use, probably by workers who don't want to ask their boss every time they go for cigarettes."
    "Inside the walls it's dark and empty. A single soldier without a gun stands smoking by the main office. Again, that's capitalism for you."
    "All this barbed wire, all the TV talk about security, all the millions spent on counter-terrorism, and what stands between you and a critical piece of infrastructure? The fourty-year-old concrete wall. With a hole in it."
    "You stick to the shadows and make your way inside the plant."
    nvl clear
    "The generator room is huge and oddly quiet. Somehow you expected the station that powers half the country to be deafening. Like a roaring evil dragon, or, better yet, like a car with a drunk driver, blasting hip-hop at 100 decibel and as many kilometers an hour, charging towards the crowd."
    "But it's not. Immense well-oiled machinery makes about as much noise as a truck engine. There is no hissing steam, smoke or flying sparks, not even that much dirt. The entire place is what your computer would seem to a bug that has climbed inside. Large and efficient."
    "Of course, that's about to change. You start creeping towards the generators, avoiding rare night-shift workers."
    nvl clear
    "Except they are not dressed in blue workers' uniforms. Something green?"
    "Not green. Camo."
    "Is that a pistol in his hand?"
    menu:
        " — The bomb explodes the moment you shoot!":
            " — The bomb explodes the moment you shoot!"
            " — Really? A Bluetooth heartbeat tracker, I presume?"
            "An old man appears from behind the guards. He must be at least seventy, dressed in an old-fashioned jacket and narrow glasses."
            " — Then I guess it will also go off if we take your backpack away. So pick it up and follow me at the distance of twenty meters."
            " — If you care about leaving the station alive, that is. Otherwise do as you please, blow it up if you want. The generators are reinforced way better than you apparently thought. Keep your distance, boys."
            "The man turns his back to you and starts walking."
            menu:
                "Follow him":
                    jump recruitment
                "Blow up the bomb":
                    jump generator_blown
        "Surrender":
            "You drop your backpack on the ground and raise your hands."
            "An old man appears from behind the guards. He must be at least seventy, dressed in an old-fashioned jacket and narrow glasses."
            " — Pick up your stupid toy and walk behind me at the distance of twenty meters."
            " — If you care about leaving the station alive, that is. Otherwise do as you please, blow yourself up if you want. The generators are reinforced way better than you apparently thought. Keep your distance, boys."
            "The man turns his back to you and starts walking."
            jump recruitment
        "Blow up the bomb":
            jump generator_blown

label generator_blown:
    nvl clear
    "A fire at the Crvona Gora power plant has caused a short blackout that night. The official investigation went for two years, eventually blaming it on a leaky fuel pipe."
    "Four members of the night shift, including chief of security M.A. Konstantinov, have perished in the fire."
    jump end
    
label recruitment:
    nvl clear
    $ konstantinov_opinion = 0
    $ unabomber_discussed = 0
    "You follow the old man across the generator hall, down a corridor and finally through a heavy steel door. When you're both inside, the door swings shut."
    "Even if you blow up the bomb right now, the walls are too thick and the generators are too far."
    " — So what are you? Some jihadist trying to leave infidels without electricity?"
    menu:
        " — No, I'm trying to leave {i}everyone{/i} without electricity.":
            " — No, I'm trying to leave {i}everyone{/i} without electricity."
            " — Really? And what's the point of that?"
            jump unabomber_discussion
        " — I'm trying to save the world.":
            " — I'm trying to save the world."
            " — From what? The horrors of having an electric station?"
            jump unabomber_discussion
        " — A failed terrorist, apparently.":
            " — A failed terrorist, apparently."
            " — Apparently so, but humor me. What was your goal?"
            jump unabomber_discussion
        " — It's none of your business.":
            $ konstantinov_opinion -= 1
            " — It's none of your business."
            " — You try to blow up the generators. Since it's my job to keep them unblown, it is obviously my business."
            " — Now, either press the damn button and let's see if it works, or start talking."
            menu:
                "Start talking":
                    jump unabomber_discussion
                "Press the damn button":
                    jump room_blown
        " — Fuck you!":
            " — Fuck you!"
            " — {i}I tebya nakhuy.{/i}. Fuck you too, I mean."
            menu:
                "Explain your ideology":
                    jump unabomber_discussion
                "Blow up the bomb":
                    jump room_blown
        "Blow up the bomb":
            jump room_blown
    label unabomber_discussion:
        "You spend some time speaking about the evils of capitalism."
        " — Yes, sure. And how exactly does blowing a generator help with that?"
        " — If electricity goes down, sure, people die, folks in intensive care and such. But more importantly, the entire civilization collapses. There are no corporations anymore, no armies, no police to keep the man down. A better society will eventually get built."
        nvl clear
        " — A better society? It would probably be like that american movie, the one with the ridiculous cars."
        menu:
            " — Mad Max? It's Australian.":
                " — Mad Max? It's Australian."
                " — American, Australian, it doesn't matter. What matters is that it's what society without the laws looks like."
            " — Mad Max? It's propaganda.":
                " — Mad Max? It's essentially a propaganda piece. Humanity is not just a bunch of barbarians."
                " — No, it's not. Humanity, I mean. But there are enough, as you call them, barbarians to make the life horrible for everyone else. Either way, the world is ruled by psychopaths. But with the law, it's ruled by the kind of a psychopath that thinks {i}before{/i} shooting."
            "Blow up the bomb":
                jump room_blown
        " — Now tell me this. Are you aware that it's not the only generator on the planet?"
        menu:
            " — It's not just me.":
                $ konstantinov_opinion -= 1
                " — It's not just a single generator. Tonight, infrastructure all around the Europe will go up in flames. Even if you kill me, the world still won't be the same tomorrow."
                " — That little forum of yours? Don't be ridiculous. Ninety percent of these kids won't go beyond talking, half of the rest can't make a bomb, and half of those who can are actually people like me."
                menu:
                    " — That still leaves a few tens of people.":
                        " — That still leaves a few tens of people."
                        " — Most of whom were arrested before they left their houses. Did you think you'll plan your attack in plain sight and nobody will notice? I have let you come here, though."
                    " — So why I was not arrested?":
                        $ konstantinov_opinion += 1
                        " — So you knew I was coming. Maybe you even knew who I am. But somehow I'm still alive and not in police custody. Why?"
                    "Blow up the bomb":
                        jump room_blown
            " — One generator today, the other tomorrow...":
                " — Yes, I am. I was planning to hit the other ones later."
                $ konstantinov_opinion += 1
                " — So you don't surrender the others just yet. That's good, but I've read your little forum."
            "Blow up the bomb":
                jump room_blown
        " — I knew someone will come to blow up the station, but I didn't have your name or adress. So you're probably not a complete moron. And you don't look suicidal, which is also good."
    label offer:
        nvl clear
        " — Now, back in the day, if you survived your so-called attack, we would give you to the Soviets. To keep it clear: I was a citizen of this fine country and an officer of the Security Commitee, not directly under Soviet command. Although I happen to be Russian."
        menu:
            " — You fucking Stasi!":
                $ konstantinov_opinion -= 1
                " — You fucking Stasi!"
                " — Learn your history. The Stasi were in East Germany."
            " — So you're an ex-Sec.":
                $ konstantinov_opinion += 1
                $ sec_mentioned = True
                " — So you're an ex-Sec."
                " — If there is such a thing as {i}ex-{/i}Sec. Some say there isn't."
            " — You fucking collaborator!":
                $ konstantinov_opinion -= 1
                " — You fucking collaborator!"
                "..."
            " — You're the reason we didn't have the democracy for half a century!":
                " — You're the reason we didn't have the democracy for half a century!"
                " — Somehow I thought you hated status quo?"
            "Stay silent":
                "..."
            "Blow up the bomb":
                jump room_blown
        " — Anyway, the Soviets. They would tell you that from now on you'll be doing their work. That's certain, but there is a question of what work it will be. You may shovel irradiated snow at Novaya Zemlya for the next ten years, or you may help fight imperialism somewhere in Africa. Your choice. Of course, they wouldn't actually let you within a thousand kilometers of their test sites, but \"cutting trees in Siberia\" just doesn't have that ring to it."
        " — I'm about to make you a similar offer. I may tell my friends at the police that you're a junkie trying to steal some copper wire. You pay the fine, go home and live your life. Or I may tell them that you wanted to leave the entire capital without electricity. Your choice."
        menu:
            " — And why would I trust you?":
                " — And why would I trust you?"
                " — Why not? Consider your options. If you do as I say, maybe you will get in trouble later, maybe you will not. If you don't, you are definitely in trouble right now. As I said, your choice."
            " — And why would you trust me?":
                " — And why would you trust me?"
                $ konstantinov_opinion += 1
                " — Why not? If you really wanted to blow yourself up, you would've done it already. So you probably want to stay alive and free, which is just what I offer you."
                menu:
                    " — Assuming I don't run away.":
                        " — Assuming I don't run away."
                        " — To where exactly? To your safehouse where you've already prepared a clean passport and tickets to Hong Kong?"
                    " — Assuming I don't blow you up right now.":
                        " — Assuming I don't blow you up right now."
                        " — Assuming that, yes."
                    "Blow up the bomb":
                        jump room_blown
            "Blow up the bomb":
                jump room_blown
        nvl clear
        " — Now, here's what I want from you. I tell you a password to a certain Bitcoin wallet. You go to certain people and tell them it's for the hostage. They wanted more, but that would be for {i}two{/I} hostages."
        " — When the hostage is released, I call you, you tell them the password and come back here. I call the police, you get your fine for unauthorised entry and go home."
        menu:
            " — What if I don't come back?":
                " — What if I don't come back?"
                " — You mean if you run away? I don't think you're that stupid."
            " — What if they don't like your offer?":
                " — What if they don't like your offer?"
                " — It's non-negotiable. Use your diplomatic skills and your bomb to make sure they understand."
            " — What if they just beat me?":
                " — What if they just beat me until I tell them the password?"
                " — Use your diplomatic skills and your bomb."
            " — So you just need someone disposable?":
                " — So you just need someone disposable?"
                " — Yes."
        if konstantinov_opinion >= 0:
            "The man knocks on the door. A guard immediately swings it open."
            "The moment you step across, a young man in glasses hands you two pieces of paper."
            " — Here's the password. Try not to forget it, you'll have to leave the paper in here. The other one is the address so that they can check what's there. It's seven Bitcoin and some change, in case you were wondering."
            " — Your car waits at the bus stop. Now to the directions..."
            "The password is of the correct-horse-battery-staple variety, four words long. The directions are much more difficult to remember, but they don't let you go until you're certain that water tower is before the burned truck, not after."
            jump bandits
        if konstantinov_opinion < 0:
            "The man kicks the door twice. You hear some talk otside before a soldier swings it open."
            "The moment you step across, two thugs jump on you. Old man steps over you, grabs the backpack and throws it inside. Another guard promptly locks the door, and after about a minute you hear a muffled thud."
            menu:
                " — What the fuck?":
                    " — What the fuck?"
                " — What about your offer?":
                    " — What about your offer?"
            " — I wanted to see if you can be trusted to pass my message. You're not. Boys, keep him down while I call the police."
            jump early_arrest
            
label room_blown:
    nvl clear
    "You blow up yourself and the old man. Whether it harms or helps the humanity, you don't change the course of history that much."
    "When next morning the entire Internet starts talking about three explosions in Eastern Europe, nobody mentions Crvona Gora."

label bandits:
    nvl clear
    scene hangar
    "You keep repeating the password all the way down to the road. Correct horse battery staple correct horse battery staple DAMN THESE ROOTS correct horse battery staple correct horse... "
    "It is a bit like meditation. Except that it's not some mantra of total equanimity, it's a pile of money send by one bunch of psychopaths to other bunch of psychopaths to save somebody, presumably also a psychopath. Although honestly, look who's talking."
    "Sure enough, a dirty grey Niva stands at the bus stop, keys in the ignition. Not exactly a James Bond car, but then you need to, quote, go along the creek for about two kilometers, hopefully it's still passable, unquote."
    "The less is said about the travel, the better, but eventually you find yourself in some kind of abandoned garage or hangar in the countryside."
    "Suddenly you're blinded by the flashlights. You have expected some thugs, but the voice from behind the light clearly belongs to an educated man, maybe a professor or a politician."
    nvl clear
    " — Now walk out of the car. What's in the backpack, our money?"
    menu:
        " — No.":
            " — Not quite."
            " — Then why the hell are you here? A hostage dies, so they send us a replacement? That would be awfully nice of them."
            " — It's a bomb and it goes off if you shoot me. So don't do that, please."
        "Blow up the bomb":
            jump hangar_blown
    " — Yet we are still alive, so I guess they're still interested in talking. Who are you?"
    menu:
        " — A messenger.":
            " — A messenger. I guess they won't risk sending one of their own, so here I am."
            " — Then what's the message?"
        " — Someone who doesn't want to die.":
            " — Someone who will be happy just to get out of here alive. I guess they won't risk sending one of their own, so here I am."
            " — You just try and save your own life? By showing up here with a whole backpack of C4 or whatever you got there, instead of our money? How is it supposed to work?"
        "Blow up the bomb":
            jump hangar_blown
    " — There is a wallet with seven Bitcoin in it, or so I'm told. I can tell you the number, check it yourself. The moment the hostage safely gets wherever he needs to, they call me and I tell you the password. The offer is non-negotiable."
    nvl clear
    " — Seven? Fuck you, your fucking car and your fucking hostage. And it's she, you halfwit. The hostage is she."
    menu:
        " — You're talikng to the wrong guy":
            " — You're talking to the wrong guy. I'm just a walking SMS here, you may listen to me or not, but that wallet contains as much money as it contains."
            " — Point taken. You may wait in your car while we think."
        " — Fuck you, too":
            " — Fuck you too. You know what, I don't even care anymore. Take the money, leave the money, shoot the hostage, marry the fucking hostage, I don't care. Only if you shoot me too early, you explode and also get no money, so fuck you twice."
            " — It's more Ian Fleming than Guy Ritchie, so mind your language. But we'll think about what you say. Get in the car and wait."
        "Blow up the bomb":
            jump hangar_blown
    nvl clear
    "The thinking apparently takes some time. You would never expect to find yourself playing 2048 while sitting on a bomb in a middle of some spy drama, but here you are. Hopefully they'll decide something before the battery in a tracker dies."
    "That would be really stupid."
    "Eventually they do. You get a call from an old man, shout the password and start the car. Come to think of it, you never told him your number."
    "The debriefing is to happen at your apartment. Of course, you didn't tell him your address either, but you are no longer surprised. Hopefully, in a year or two you'll be allowed to scratch your nose without his permission."
    "Hopefully."
    jump end
label hangar_blown:
    "The explosion in the abandoned tractor repair station doesn't draw media attention. As far as the whole world is concerned, some village drunkard was playing with something. Whatever."
    "You have no idea what was really saved or destroyed. The hostage definitely wasn't saved, though. Maybe it's bad."
