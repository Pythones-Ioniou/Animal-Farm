label chapter5:
    scene bg barn_in
    show c sad at center 
    c "Hey, Sarlot." 
    c "Have you noticed anything differnet about Mollie?" 
    hide c
    show sar sad at center 
    sar "Yes, I've noticed that she's often late for work and keeps making weird excuses." 
    sar "Yesterday, I heard her say that she overslept, and she also complained for mysterious pains." 
    hide sar 
    show c neutral at center 
    c "I thought it was just me seeing it!" 
    c "I keep seeing her gaze foolishly at her own reflection in the water." 
    c "Wait, there she is!" 
    c "I'll go talk to her."
    hide c
    pause 1 
    show c neutral at center 
    c "Mollie, I have something very serious to say to you." 
    c "This morning, I saw you looking over the hedge that divided Animal Farm from Foxwood."
    c "One of Mr. Pilkington's men was standing on the other side of the hedge." 
    c "And - I was a long way away, but I am almost certain that I saw this - he was talking to you, and you were allowing him to stroke your nose." 
    c "What does that mean Mollie?" 
    hide c 
    show mol worried at center 
    mol "He didn't!" 
    mol "It wasn't!" 
    mol "It isn't true!" 
    hide mol
    show c angry at center
    c "Mollie!" 
    c "Look me in the face!" 
    c "Do you give me your word of honour that that man was not stroking your nose?" 
    hide c 
    show mol worried at center 
    mol "It isn't true!" 
    hide mol
    show c angry at center 
    c "Mo-"
    c "Wait!" 
    c "Where are you going?" 
    hide c 
    show bg mollie_leaving
    pause 3 
    show bg some_days_later
    pause 3 
    show bg barn_out
    show c sad at center 
    c "Hey Sarlot, have you seen Mollie?" 
    c "I haven't seen her in three days..." 
    hide c 
    show sar sad at center 
    sar "I heard from a pigeon that she's on the other side of Willingdon..." 
    sar "They said that she was standing between the shafts of a dogcart outside of a public-house." 
    sar "They also reported that some man was stroking her nose and feeding her sugar."
    sar "I don't know..." 
    sar "The pigeon said that she seemed to be enjoying herself..." 
    hide sar 
    show c sad at center 
    c "Such a shame..." 
    hide c 
    show bg scene winter 
    pause 3 
    scene bg aragmatikh
    pause 3 
    scene bg barn_in 
    show sar sad at center 
    sar "{i}Winter is hard." 
    sar "{i}It would be easier if Snowball and Naopleon weren't arguing all the time." 
    sar "{i}Snowball seems to have some good and useful ideas to make the farm better." 
    sar "{i}Napoleon always disagrees with him, without proposing anything of his own but he is better at convincing the masses."
    hide sar 
    show sh neutral at center 
    sh "Four legs good, two legs bad!" 
    hide sh 
    show sar resent at center 
    sar "{i}Here we go again..." 
    sar "{i}The sheep always interrupt Snowball's speech by saying that..." 
    hide sar 
    show s neutral at center 
    s "Comrades!" 
    s "For some time now, I have been surveying a small knoll on the highest point of the farm and have decided that it is just the place for a windmill!" 
    s "This windmill can be made to operate a dynamo and supply the farm with electrical power!" 
    s "This would light the stalls and warm them in the winter." 
    s "It would also run a circular saw, a chaff-cutter, a mangel-slicer and an electric milking machine!" 
    hide s 
    show sar neutral at center 
    sar "{i}Wow!" 
    sar "{i}Snowball has done it again with his innovative ideas!" 
    hide sar 
    show s excited at center 
    s "I believe it would be easier if I just showed you the plan-"
    hide s
    show n angry at center 
    n "No!" 
    n "This idea will go nowhere!" 
    hide n 
    "What should Napoleon do?" 
    menu: 
        "Disrespect Snowball and piss on his plans":
            scene bg piss_plans
            pause 3 
            scene bg barn_in
            show sh neutral at center 
            sh "Four legs good, two legs bad!" 
            hide sh 
            show sar resent at center 
            sar "{i}They need to stop saying that!" 
            sar "{i}They made everyone leave the meeting!" 
            hide sar
            scene bg destroyed_plans
            pause 1 
            sar "{i}What is Snowball doing?" 
            sar "Is he remaking the plans?"
            hide sar
        "Respect him and be quiet": 
            show s neutral at center 
            s "Be patient comrade!" 
            s "You'll see that this is what's best for Animal Farm!" 
            hide s 
            show n angry at center 
            n "Hm..."
            hide n 
    scene bg house
    show sar neutral at center 
    sar "{i}After that the farm was deeply divided on the windmill." 
    sar "{i}The animals who sided with Snowball had the slogan 'Vote for Snowball and the three-day week'..."
    sar "{i}...and the animals who sided with Napoleon said 'Vote for Napoleon and the full manger'."
    sar "{i}The only animal who didn't side with anyone was Benjamin."
    sar "{i}When asked, he said:"
    hide sar 
    show ben neutral at center 
    ben "Windmill or no windmill, life would go on as it had always gone on..."
    ben "...and that is badly." 
    hide ben 
    scene bg meeting 
    pause 3 
    scene bg barn_in
    show sar neutral at center 
    sar "{i}There was another meeting held some days later to discuss the defense of the farm." 
    sar "{i}Snowball and Napoleon were arguing again..." 
    hide sar 
    show n nonchalant at center 
    n "We need to produce firearms and train ourselves in the use of them!" 
    hide n 
    show s neutral at center 
    s "No comrade!" 
    s "We should send out more pigeons and stir up rebellion among the animals on the other farms!" 
    hide s 
    show n nonchalant at center 
    n "But if we can't defend ourselves then we are bound to be conquered!" 
    hide n 
    show s neutral at center 
    s "If rebellions happen all over the country, then we have no need to defend ourselves!" 
    hide s 
    show sar neutral at center 
    sar "Forget about that for a minute, let's vote on the windmill first!" 
    hide sar 
    show s excited at center 
    s "I have managed to make the plans for the windmill even better!" 
    s "I found so many benefits to it1" 
    s "Firstly-"
    hide s 
    show n nonchalant at center 
    n "Comrades." 
    n "The windmill is nonsense, and I advise you to vote agianst it." 
    hide n 
    show sh neutral at center 
    sh "Four legs good, two legs bad!" 
    hide sh 
    show s neutral at center 
    s "Comrades!" 
    s "Please quiet down!" 
    s "Allow me to present my ideas!" 
    hide s 
    show sar neutral at center 
    sar "{i}There's no doubt now which way the vote will go." 
    sar "{i}All the animals are now agreeing and cheering that the windmill should be built." 
    hide sar 
    scene bg dogs_attack_snowball 
    pause 3
    "What should the animals do?" 
    menu: 
        "Defend Snowball":
            jump ending3 
        "Freeze and do nothing.":
            return
    scene bg barn_in
    show sar shocked at center
    sar "Oh my god!"
    sar "They are attacking Snowball!"
    hide sar
    show n nonchalant at center
    n "From now on, the Sunday-morning meetings will come to an end."
    n "They are unnecessary and waste time."
    n "In the future, all questions related to the workings of the farm are to be settled by a special committee of pigs, presided over by myself."
    n "This committee is to meet in private and afterwards communicate out decisions to you."
    n "We are all to still assemble on Sunday mornings to salute the flag, sing 'Beasts of England' and receive orders for the week;"
    n "but there will be no more debates."
    hide n 
    show sq suspicious at center
    pig "But-"
    hide sq
    show d neutral at center
    d "GRRRRRRRRRR-"
    hide d
    show sh neutral at center
    sh "Four legs good, two legs bad!"
    hide sh
    show sq neutral at center
    sq "Don't be afraid!"
    sq "The dogs are not here to hurt you, but to protect you."
    sq "They were trained by Napoleon to drive evil away."
    sq "Comrades, I trust that every animal here appreciates the sacrifice that Comrade Napoleon has made in taking this extra labour upon himself."
    sq "Do not imagine, comrades, that leadership is a pleasure!"
    sq "On the contrary, it is a deep and heavy responsibility."
    sq "No one believes more firmly than Comrade Napoleon that all animals are equal."
    sq "He would be only too happy to let you make your decisions for yourselves."
    sq "But sometimes, you might make the wrong decisions, comrades, and then where should we be?"
    sq "Suppose, you had decided to follow Snowball, with his moonshine of windmills-Snowball, who, as we now know, was no better than a criminal!"
    hide sq
    show sar neutral at center
    sar "The animals were not certain what the word mean, but Squealer spoke so persuasively, and the three dogs who happened to be with him growled so threateningly that they accepted the explanation."
    return

