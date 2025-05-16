#chapter2.rpy
#chapter 2 (main story)

label chapter2:
    scene bg black_screen
    "Three days later, Old Major died peacefully in his sleep."
    scene bg barn_in
    show sar neutral at center
    sar "For the next three months, three of the pigs,"
    hide sar
    show n nonchalant at center
    sar "Napoleon,"
    hide n 
    show s neutral at center 
    sar "Snowball,"
    hide s 
    show sq neutral at center
    sar "and Squealer"
    hide sq
    show sar neutral at center
    sar "organized Old Major's teachings into an ideology called Animalism."
    sar "They didn't know when the revolution would come,"
    sar "but they knew it was their duty to educate the other animals."
    sar "Secret meetings were held by the three pigs several nights a week, to spread Animalism."
    sar "At the beginning, they were met with stupidity and apathy."
    sar "The most faithful disciples were the two horses"
    hide sar
    show b neutral
    sar "Boxer"
    hide b
    show c neutral
    sar "and Clover."
    hide c 
    show sar neutral
    sar "Through them, other animals-"
    hide sar
    show bet angry at center
    bet "Oh my god, I'm so hungry!"
    hide bet
    show ria neutral at center
    ria "Yes, I'm starving!"
    ria "Where is Jones?!"
    ria "Do you think he'll feed us?"
    hide ria
    show sar sad at center
    sar "I don't think he wil..."
    sar "I saw him go to sleep drunk again."
    hide sar
    show bet angry at center 
    bet "WHAT?!"
    bet "I've had enough!"
    scene bg cow_shaped_hole
    pause 3
    scene bg barn_in
    show sar shocked at center 
    sar "Everybody out!"
    sar "There's food in the bins! Go eat before Jones wakes up!"
    scene bg eating
    pause 3
    scene bg jones_awake
    pause 3
    scene bg barn_out
    show sar shocked at center
    sar "Jones is awake!"
    scene bg jones_whips
    pause 3
    scene bg barn_in
    show s determined at center
    s "Now's the time!"
    hide s 
    "What should Sarlot do?"
    menu:
        "Join the battle":
            return
        "Stay hidden":
            jump ending2_chapter2
    scene bg fighting
    pause 3
    scene bg deciding
    pause 3
    "What should Snowball do?"
    menu:
        "Take the gun and kill Jones":
            scene bg killing_jones
            pause 3
        "Let him live.":
            s "{i}It's not his time to die yet...{/i}"
    scene bg running 
    pause 3
    scene bg celebrating
    all "We did it!"
    scene bg celebrating_too
    all "WOOOOOO!"

    call exploration

    scene bg mollie_ribbons
    pause 3
    scene bg finding_mollie
    pause 3
    scene bg farmhouse_room
    show s skeptical at center
    s "Mollie, what are you doing?"
    s "Ribbons, should be considered as clothes, which are the mark of a human being."
    hide s 
    show s confident at center
    s "All animals should go naked."
    s "Everyone, let's go outside!"
    s "It is half-past six and we have a long day before us."
    s "Let us have our breakfast and then there is another matter that must be discussed."
    hide s 
    scene bg going_meeting
    pause 3
    scene bg barn_out
    show sq neutral at center 
    sq "For the past three months, we have taugh ourseves how to teach and write from some of Mr. Jones' children's books."
    sq "It is time to make some changes..."
    scene bg farm_entrance
    show sq neutral at center
    sq "Our farm's name is no longer 'Manor Farm'!"
    sq "We have also managed to reduce the principles of Animalism to seven commandments, by which all the animals on this farm must live for even after."
    sq "Snowball, since you are best at writing, go ahead and write them on the tarred wall with great white letters!"
    hide sq 
    scene bg commandments
    pause 3
    scene bg barn_out
    show s neutral at center 
    s "The Seven Commandments:"
    s "Whatever goes upon two legs is an enemy."
    s "Whatever goes upon four legs, or has wings is a friend."
    s "No animal shall wear clothes."
    s "No animal shall sleep in a bed."
    s "No animal shall drink alcohol."
    s "No animal shall kill any other animal."
    s "All animals are equal."
    hide s 
    show sar troubled at center
    sar "Hm..."
    hide sar 
    show sar neutral at center
    sar "Even though friend is mispelled and one of the s's is the wrong way round, they are very neatly written!"
    sar "It's nice that Snowball read it out oud for everyone, since not every animal can read yet!"
    sar "Everyone nodded in agreement and some seemed to already learn them by heart."
    hide sar
    show bet angry at center
    bet "MOOOOOOOOOOO!"
    hide bet
    show sar shocked at center
    sar "Oh no!"
    sar "The cows haven't been milked for twenty-four hours!"
    hide sar
    show sar resent at center
    pig "Someone fetch some buckets!"
    hide sar
    show sar troubled at center
    sar "What is going to happen to all that milk now?"
    hide sar
    show n nonchalant at center
    n "Never mind the milk!"
    n "That will be attended to." 
    n "The harvest is more important."
    n "Snowball will show you the way and I shall follow in a few minutes."
    n "Forward, comrades! The hay is waiting!"
    hide n
    show sar troubled at center
    sar "{i} Where is Napoleon taking all that milk...?{/i}"
    return 


#exploring parts of the farm 
label exploration:
    "Where do you want to explore?"
    menu:
        "Barn":
            jump barn
        "Wilderness":
            jump wilderness 
        "Farmhouse":
            jump farmhouse

#exploring the barn
label barn:
    scene bg feasting
    jump exploration

#exploring the wilderness
label wilderness:
    scene bg happy_animals
    jump exploration

#exploring the farmhouse
label farmhouse:
    return
