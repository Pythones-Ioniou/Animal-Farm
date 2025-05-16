label ending4:
    scene bg barn_out
    show sq frustrated at center 
    w "That’s enough!"
    w "This madness should come to its end!"
    hide sq
    show n irritated at center 
    n "What are you talking about?"
    hide n 
    show sq frustrated at center 
    r "You know very well what he’s talking about."
    r "We were promised equality, yet we starve while you grow fat!"
    mar "He’s right! If we wait any longer, there will be nothing left of us!"
    hide sq
    show n angry at center 
    n "This nonsense of yours will end now!"
    hide n 
    show sq frustrated at center 
    mar "We will not keep living under your hoof."
    hide sq
    show n angry at center 
    n "You have no other choice. I, leader Napoleon, sentence you to death."
    hide n 
    show sq excited at center 
    r "Comrades, if we stand together, he cannot break us!"
    hide sq
    "What will the animals do?"
    menu:
        "Will not invade":
            jump beforepathing

        "Defend the pigs":
            jump defend_path

label beforepathing:
    scene bg barn_out
    show n irritated at center 
    n "Comrades, please ignore these fools. They don’t know what they’re talking about."
    hide n
    show sq happy at center 
    sq "That’s right. Besides where would we all be without our leader Napoleon? These pigs have been brainwashed by Snowball."
    hide sq
    call pathing

label defend_path:
    scene bg ending_nefelhs5
    pause 3
    scene bg barn_in
    show n worried at center 
    n "What do you think you’re all doing?"
    hide n
    show sq frustrated at center 
    mar "That’s enough Napoleon. This is your end!"
    hide sq
    show n angry at center 
    n "Dogs!"
    hide n
    show sar shocked at center 
    sar "Be careful everyone!"
    hide sar
    show b angry at center 
    b "Don’t worry. I can take care of them."
    hide b 
    show c angry at center 
    c "I’ll help you out."
    hide c
    scene bg gamane_skulia
    pause 3
    scene bg barn_in 
    show n worried at center 
    n "..."
    scene bg ending_nefelhs7
    pause 3
    scene bg ending_nefelhs6
    pause 3
    scene bg barn_in
    pause 0.1
    scene bg barn_in
    show bet closeup at center
    pause 2
    bet "Where do you think you are going?"
    hide bet 
    scene bg ending_nefelhs5
    pause 3
    n "Comrades, calm down. Obviously there has been a misunderstanding-"
    b "I trusted you, Napoleon. I thought you knew better than this. But this? This is too much."
    n "Boxer, my good and loyal- wait what are you doing-"
    scene bg ending_nefelhs4
    pause 3
    show sq frustrated at center  
    r "Don’t let him get away!"
    hide sq
    scene bg ending_nefelhs3
    pause 3
    scene bg barn_in
    scene bg black_screen
    pause 3
    scene bg barn_out
    show sar troubled at center 
    sar "What happened?"
    hide sar
    show c neutral at center 
    c "He got away..."
    c "He jumped down a hole that I considered dangerous for us to go."
    c "A couple of hens tried to follow him, but to not avail."
    hide c
    show sq neutral at center 
    w "Well, at last he’s gone."
    show sq excited at center 
    r "We’re finally free again!"
    hide sq
    scene bg celebrating
    pause 3
    scene bg barn_out
    show c neutral at center 
    c "Wait, a second…where is Squealer?"
    hide c
    show sar troubled at center 
    sar "While you were gone searching for Napoleon, I tried to look for Squealer."
    sar "I found him hiding behind a bush. Not that he couldn’t be seen but-"
    sar "Anyway, when he got aware of my presence, he saw the entry unguarded and ran away as well."
    hide sar
    show c happy at center 
    c "At least he won’t be any more trouble."
    hide c
    show ria neutral at center  
    ria "But what are we going to do now without a leader?"
    hide ria
    show sq neutral at center 
    mar "Do not worry about that!"
    mar "We will just do what we did before, but this time we won’t have Napoleon stealing our food and telling us to do things for his sake and waste our time."
    hide sq
    scene bg some_days_later
    pause 3
    scene bg barn_in
    show sar neutral at center 
    sar "The animals seem to be happy again."
    sar "I sometimes listen to some of them sing the Beasts of England."
    sar "I’m glad to see everyone back to their old habits and joys."
    sar "Even the food is now divided fairly."
    sar "Oh, I see the pigs over there standing upon the wooden crate in the middle of the barn."
    sar "Maybe they want to say something."
    sar "I’ll go closer to listen"
    hide sar
    show sq happy at center 
    mar "Comrades, we are free at last! Free from the chains of oppression!"
    mar "Free to live as we were meant to live."
    show sq suspicious
    r "But comrades, our work is not done. Without a leader, we must ensure that this farm remains in order."
    r "We must govern ourselves wisely so that no one else takes advantage of us again!"
    hide sq
    show sar neutral at center
    "Should Sarlot say something about this idea?"
    menu:
        "Yes":
            jump yes_pathing

        "No":
            jump no_pathing

label yes_pathing:
    scene bg barn_in
    show sar troubled at center 
    sar "But wouldn’t that cause chaos in the farm?"
    hide sar
    show sq happy at center 
    r "Oh, but of course. How didn’t we think of that before?"
    show sq neutral at center
    mar "Comrades, Sarlot is right."
    mar "We must face the truth. Without structure, we will descend into chaos."
    show sq excited at center
    mar "So, we will be the ones to keep the order."
    hide sq
    show c neutral at center 
    c "But wouldn’t that be the same as it was with Napoleon."
    hide c
    show sq neutral at center 
    w "We won’t be your leaders, Clover."
    show sq excited at center 
    w "We’re going to be your guides, your advisors."
    w "We will simply ensure that everything runs smoothly, that’s all."
    hide sq
    show c neutral at center 
    c "Well… if you say so."
    c "Since you were the ones to take Napoleon down, I’m sure you won’t do the same things as him."
    hide c
    show sq neutral at center 
    mar "That is correct, comrade."
    mar "We are here to make the farm a better place for all the animals."
    w "We will now go in the farmhouse to lend some books and figure out how to guide you all through the best years of your life."
    w "You can all go back to work."
    hide sq
    scene bg end 
    pause 120
    $ renpy.full_restart()


label no_pathing:
    scene bg barn_in
    show sq excited at center 
    w "We cannot allow what happened before to repeat itself. We must all have a say in what happens on this farm."
    w "No more leaders! No more masters!"
    hide sq
    scene bg celebrating
    pause 3
    scene bg some_days_later
    pause 3
    scene bg meeting
    pause 3
    scene bg barn_in
    show sq suspicious at center 
    r "We have noticed some of you being lazy and skipping work or getting more food than you should."
    hide sq
    show sar sad at center 
    sar "Really? I’m pretty sure I saw no one do that from up here…"
    hide sar
    show sq suspicious at center 
    mar "Comrades, calm down. All we want is to help with the farm’s proper function."  
    mar "And to do that we need order."
    show sq frustrated at center
    w "We will now go in the farmhouse to lend some books and figure out how to guide you all through the best years of your life." 
    w "You can all go back to work."
    hide w
    scene bg some_days_later
    pause 3
    scene bg barn_in
    show sar troubled at center 
    sar "What are they plotting…."
    hide sar 
    show c neutral at center 
    c "Oh, there they are."
    hide c
    show sq frustrated at center 
    mar "Did I hear correctly, comrade?"
    mar "You think we are not working for the great future of this farm."
    mar "You think we haven’t spent all this time figuring out what to do with the farm?"
    hide sq
    show sar sad at center 
    s "I didn’t say that."
    s "I just thought that we agreed that no one would live in there!"
    hide sar
    show sq suspicious at center 
    w "We are not living in the farmhouse."
    w "We are only lending its belongings. "
    show sq neutral at center 
    w "It is practical if you think about it, Sarlot."
    show sq frustrated at center
    w "The farmhouse has books, resources that will help us act wisely."
    w "Besides, it’s much more comfortable for us to think and strategize without distractions."
    show sq suspicious at center 
    r "We require more nourishment, comrades."
    r "Our work is difficult."
    r "We think for all of you at once!"
    r "Surely, you would not deny us the energy we need to do what’s best for the farm."
    show sq happy
    mar "Comrades, do not be ungrateful!"
    mar "We work tirelessly to ensure your safety and well-being!"
    mar "Would you rather fall into disorder?"
    mar "Would you rather fall in the chaos?"
    hide sq
    scene bg ending_nefelhs
    pause 3
    scene bg barn_in
    show c sad at center 
    c "Hey, Sarlot."
    c "Why do I get a sense of… deja vu?"
    c "I feel like…. they’re starting to do things exactly like Napoleon did."
    hide c
    show sar shocked at center 
    s "I guess some things will never change…"
    hide sar
    scene bg final_ending3
    pause 120
    $ renpy.full_restart()