label chapter6:

    scene bg windmill_whole
    pause 3
    show c angry
    c "Oof. We’ve been working very hard all year!!!"
    hide c
    show b neutral
    b "At least we’re working for ourselves and not for humans."
    hide b
    show c angry
    c "But Boxer, we’re even working on Sundays!!!"
    hide c
    show b neutral
    b "If Napoleon says it, it must be right!!!"
    hide b
    show c angry
    c "The harvest is less successful this year and even the windmill presents difficulties. "
    c "It takes a whole day of exhausting effort to drag a single boulder to the top of the quarry and even when we push it over the edge it fails to break. Fortunately, we have you Boxer. "
    c "Your strength equals to that of all the animals put together! But you must be careful to not overstrain yourself…"
    hide c
    show b neutral
    b "No Clover! The windmill is a slow and laborious process, and I must work harder! I’ll ask a cockerel to call me three-quarters of an hour earlier from now on."

    scene bg meeting
    pause 3
    scene bg barn_in
    pause 3
    show sar troubled
    sar "Comrade Napoleon, I have noticed that we have some unforeseen shortages on necessities that the farm cannot produce. What are we going to do?"
    hide sar
    show n nonchalant
    n "That is why I announce to you that from now onwards Animal Farm will engage in trade with the neighboring farms. This is simply to obtain certain necessary materials."
    n "The needs of the windmill must override everything. That is why I am making arrangements to sell a stack of hay and part of this year’s wheat crop."
    n "If more money is needed, it will have to be made by the sale of eggs. You hens should welcome this sacrifice as your own special contribution towards the building of the windmill!"
    hide n
    show sq frustrated
    sq "Never to have any dealings with human beings, never to engage in trade, never to make use of money - had not these been among the earliest resolutions passed at that first triumphant Meeting after Jones was expelled?"
    hide sq
    show d neutral
    d "Rawrrrrrr!!!!!!!!!!!!!!!!!!!!!"
    hide d
    show sh neutral
    sh "Four legs good, two legs bad"
    hide sh
    scene bg elon_mask
    scene bg windmill_whole
    show n nonchalant
    n "I have already made all the arrangements."
    n "There is no need for any of you to communicate with human beings, something that I know is clearly undesirable."
    n"I intend to take the whole burden up on my shoulders."
    n "Mr. Whymper, a solicitor living in Willingdon has agreed to act as intermediary between the Animal Farm and the outside world."
    n "He will visit the farm every Monday to receive his instructions. Long live Animal Farm!!!!!!!!!"
    hide n


    "Should Sarlot say something to Squealer?"
    menu:
        "Yes":
            show sar troubled
            sar "Wasn’t there a rule against engaging in trade with humans?"
            hide sar
            show sq neutral
            sq "I assure you Comrades that the resolution against engaging in trade and using money was never passed or even suggested."
            sq "It was pure imagination, probably traced in the beginning to lies circulated by Snowball. "
            sq "Are you certain that this is not something that you have dreamed, comrades? "
            sq "Have you any record of such a resolution? Is it written down anywhere?"
            hide sq
        "No":
            show sar "…"
            hide sar
            

    scene black_screen
    centered "Days later.."
    scene bg commandments
    scene barn_in
    show sar neutral
    sar "Clover, what are you doing?"
    hide sar
    show c neutral
    c "I am trying to read the Fourth Commandment."
    c "Squealer said that it is absolutely necessary for the pigs to live in the house because they need a quiet place to work in but I am sure there was a Commandment that forbade it."
    c "I can’t read more than individual letters though…"
    hide c
    show sar neutral
    sar "Why don’t we get Muriel to read them?"
    hide sar
    show c neutral
    c "That’s a great idea! Muriel, come here. Read me the Fourth Commandment. Does it not say something about never sleeping in a bed?"
    hide c
    show mur neutral
    mur "It says ‘No animal shall sleep in a bed with sheets’."
    hide mur
    show c neutral
    c "I do not remember the Fourth Commandment mentioning sheets but if it’s on the wall then that must be it…"
    hide c
    show sq neutral
    sq "You have heard then, comrades, that we pigs now sleep in the beds of the farmhouse? And why not? You did not suppose, surely, that there was ever a ruling against beds?"
    sq "A bed merely means a place to sleep in. A pile of straw in a stall is a bed, properly regarded. The rule was against sheets, which are a human invention. "
    sq "We have removed the sheets from the farmhouse beds, and sleep between blankets."
    sq "And very comfortable beds they are too! But not more comfortable than we need, I can tell you, comrades, with all the brainwork we have to do nowadays."
    sq "You would not rob us of our repose, would you, comrades?"
    sq "You would not have us too tired to carry out our duties? Surely none of you wishes to see Jones back?"
    hide sq
    show c neutral
    c "I guess not..."
    hide c
    scene bg black_screen
    centered "Some months later.."
    scene bg black_screen
    centered "BAMM"

    scene bg windmill_semidestroyed
    show n angry
    n "Comrades!!! do you know who is responsible for this?"
    n "Do you know the enemy who has come in the night and overthrown our windmill? SNOWBALL!!! Snowball has done this thing!"
    n "In sheer malignity, thinking to set back our plans and avenge himself for his ignominious expulsion, this traitor has crept here under cover of night and destroyed our work of nearly a year."
    n "Comrades, here and now I pronounce the death sentence upon Snowball. 'Animal Hero, Second Class,' and half a bushel of apples to any animal who brings him to justice."
    n "A full bushel to anyone who captures him alive!"

    n "No more delays, comrades! There is work to be done."
    n "This very morning we begin rebuilding the windmill, and we will build all through the winter, rain or shine. We will teach this miserable traitor that he cannot undo our work so easily."
    n "Remember, comrades, there must be no alteration in our plans: they shall be carried out to the day."
    n "Forward, comrades! Long live the windmill! Long live Animal Farm!"
    hide n
    return

