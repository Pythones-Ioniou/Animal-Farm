#ending2_chapter2.rpy
#chapter 2 (ending 2)

label ending2_chapter2:
    scene bg barn_in
    show sar evil at center
    sar "Everything's going according to plan..."
    sar "They're finally rebelling against Jones!"
    sar "Such foolish animals..."
    sar "They really think that this rebellion of theirs is going to save them from Man!"
    sar "That they'll truly be free!"
    sar "It never crossed their mind that this all is orchestrated!"
    sar "There is no way this farm could be led successfully by animals."
    sar "It would all crumble and fall to pieces and I can't allow that to happen!"
    sar "It's not false that we lead a hard, laborious and sometimes ravenous life whle led by Jones..."
    sar "...But it's what we've known for ages!"
    sar "I doubt a single animal will be able to be a better leader..."
    sar "That is why I made a deal with Jones, the moment Old Major gave that speech"
    sar "The rebellion was inevitable."
    sar "Our living conditions were horrible and sooner or later some animal would lose it."
    sar "Hunger causes peculiar actions to be taken."
    sar "So, I told him that if he were to trust me, I'd help him regain the farm and ensure that no other rebellion would even happen again."
    sar "In return, I expect better treatment than what we are facing."
    sar "At first, he was against it and almost crushed me to death."
    sar "But he came around..."
    sar "It was hard to convince him but he finally realized that he had no other choice."
    sar "He didn't stand a chance against those ravenous and angry animals."
    sar "Not only that, even if he killed them, he had no money to make up for the loss, since he lost it all in a lawsuit."
    sar "All Jones had to do it trust me and the farm would be his again."
    sar "The plan is to pick a suitable leader and manipulate them to be worse than Jones ever was."
    sar "That way, the animals will think that rebelling against Jones was a horrible idea and they'll beg for him to come back."
    hide sar
    scene bg running 
    pause 3
    scene bg celebrating
    all "We did it!"
    scene bg celebrating_too
    all "WOOOOOO!"

    call exploring

    scene bg mollie_ribbons
    pause 3
    scene bg finding_mollie
    pause 3
    scene bg farmhouse_room
    show s skeptical at center
    s "Mollie, what are you doing?"
    s "Ribbons, should be considered as clothes, which are the mark of a human being."
    hide s 
    show s neutral at center
    s "All animals should go naked."
    show s excited at center 
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
    scene bg entrance
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
    sar "It seems that the pigs are good leaders..."
    sar "That's a huge advantage for me."
    sar "The search for a supposed leader won't be too difficult after all!"
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
    show ria neutral at center
    ria "What is going to happen to all that milk?"
    hide ria
    show mixed sarlot_napoleon at center
    sar "Napoleon, I believe you should keep the milk for yourself."
    n "Sarlot!"
    n "Are you out of your mind?"
    sar "I know it sounds crazy but let me explain."
    sar "You pigs are more intelligent than any animal on this farm."
    sar "It is only right that you're fed better than them as well."
    sar "That is the only reason I speak of this."
    sar "For your own good."
    n "I should at least tell the other animals why!"
    sar "That is not necessary."
    sar "They wouldn't understand."
    n "This doesn't feel right, but I'll trust you on this."
    n "Just once though..."
    hide mixed
    show n nonchalant at center
    n "Never mind the milk!"
    n "That will be attended to."
    n "The harvest is more importand!"
    n "Snowball will show you the way and I shall follow in a few minutes."
    n "Forward comrades!"
    n "The hay is waiting!"
    jump ending2_chapter3
    return


    #exploring parts of the farm 
label exploring:
    "Where do you want to explore?"
    menu:
        "Barn":
            jump barnn
        "Wilderness":
            jump wildernesss 
        "Farmhouse":
            jump farmhousee

#exploring the barn
label barnn:
    scene bg feasting
    jump exploration

#exploring the wilderness
label wildernesss:
    scene bg happy_animals
    jump exploration

#exploring the farmhouse
label farmhousee:
    return