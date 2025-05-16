#ending2_chapter7.rpy
#chapter 7 (ending 2)

label ending2_chapter7:
    scene bg barn_in
    show sq neutral
    sq "Comrades, it has been a bitter winter..."
    sq "Despite that though, you have all pulled through and managed to make significant progress on building the windmill!"
    sq "As you know, there is a significant shortage in food and the farm is struggling..."
    sq "That is why the hends, who are just coming in to lay, must surrender their eggs!"
    sq "Leader Napoleon has accepted a contract for four hundred eggs a week."
    sq "The price of these will pay for enough grain and meal to keep the farm going until summer comes and conditions are easier."
    hide sq

    "Do the hens protest?"
    menu: 
        "Yes":
            show n nonchalant at center
            n "SILENCE!"
            n "From now on, any animal that gives so much as a grain of corn to a hen is to be punished by death!"
            hide n 
            show ria neutral at center
            ria "No!"
            ria "You can't take out eggs and keep our corn away too!"
            scene bg hens_attacking
            pause 3
            scene bg barn_in
            show n angry at center
            n "Dogs!"
            n "Take these traitors away now!"
            scene bg killing_hens
            pause 3
            scene bg some_days_later
            pause 3
            scene bg barn_out
            show sar troubled at center
            sar "{i}I haven't seen a hen since that meeting..."
            sar "{i}Nine hens have died in the meantime, supposedly from coccidiosis..."
            sar "{i}Napoleon took it too far with this one."
            hide sar
            show sar evil at center
            sar "{i}The animals are starting to form negative opinions over him, just how I want it to be!{/i}"
        "No":
            return
    
    scene bg some_days_later
    pause 3
    scene bg barn_out
    show sar neutral at center
    sar "Napoleon no is on slightly better terms with the other farmers."
    sar "Even though no one had seen Snowball, Squealer informed us that he was secretly frequenting the farm by night."
    sar "Peculiar things were happening all around the farm and the only logical explanation,"
    sar "according to squealer,"
    sar "was that Snowball had come in the night and done them."
    sar "All this led to Napoleon becoming obsessed with going after Snowball, looking everywhere for clues."
    hide sar
    show sar troubled at center
    sar "Is that Clover over there?"
    sar "What could they be talking about?"
    scene bg sarlot_eavesdropping
    show c sad at center
    c "I don't know Boxer..."
    c "Things in the farm are weird lately."
    c "Maybe it's just me and it's all in my head,"
    c "but I'm pretty sure the commandments I remember are different than those written on the wall."
    c "And the pigs!"
    c "The pigs' behaviour has been off..."
    c "It's like they think we're all beneath them."
    hide c
    show b neutral at center
    b "No Clover!"
    b "What is it you're saying?"
    hide b 
    show c sad at center 
    c "I'm saying that the pigs are starting to resemble Jones..."
    hide c 
    show b neutral at center 
    b "That is not true."
    b "Comrade Napoleon wants what's best for us."
    hide b 
    show c sad at center
    c "I'm not sure that's true Boxer."
    c "We word day and night but seem to get nothing in return."
    c "But the pigs, they have everything."
    c "They take all our resources for themselves."
    hide c 
    show b neutral at center
    b "But they must."
    b "They're our leaders and we must keep them healthy."
    hide b 
    show c sad at center 
    c "I don't know Boxer." 
    c "I feel like they're taking advantage of us..."
    c "Also, I saw something that troubled me."
    c "I saw Sarlot and Napoleon speak, and not just once."
    c "I've seen them together several times."
    c "In one meeting, I'm certain that I saw her whisper to his ear."
    hide c 
    scene bg barn_in
    show sar resent at center
    sar "{i}No!"
    sar "{i}What is Clover saying!"
    sar "{i}This cannot be true..."
    sar "{i}She's my friend, she wouldn't suspect that I would do such thing!"
    sar "{i}But on the other hand, I am doing such thing..."
    sar "{i}I am betraying my friends in a way."
    sar "{i}They all think that I'm on their side, that I'm with them in this rebellion but in reality, I am opposed to it."
    sar "{i}It's for their own good though!"
    sar "{i}They can't see it now, but it's true!"
    sar "{i}I am the good one here, they'll see!"
    hide sar
    scene bg sarlot_eavesdropping
    show b neutral at center
    b "Squealer is calling for us Clover, let's go."
    scene bg barn_out 
    show sq neutral at center
    sq "Comrades, the most terrible thing has been discovered!"
    sq "Snowball has sold himself to Frederick of Pinchfield Farm, who is even now plotting to attack us and take our farm away from us!"
    sq "Snowball is to act as his guide when the attack begins."
    sq "But there is worse than that..."
    sq "We had thought that Snowball's rebellion was caused by simply his vanity and ambition but we were wrong!"
    sq "Do you know what the real reason was?"
    sq "Snowball was in league with Jones from the very start!"
    sq "He was Jone's secret agent all this time!"
    sq "It has all been proved by documents which he left behind him and which we have only just discovered."
    sq "To my mind, this explains a great deal, comrades."
    sq "Did we not see for our selves how he attempted - fortunately without success - to get us defeated and destroyed at the Battle of the Cowshed?"
    hide sq
    show b worried at center
    b "..."
    hide b 

    call boxers_choice

    scene bg some_days_later
    pause 3
    scene bg barn_out
    show n nonchalant
    n "You pigs there!"
    n "I believe you have something to confess to..."
    hide n 
    show s sad at center
    pig "We have been secretly in touch with Snowball ever since his expulsion..."
    pig "We collaborated with him in destoying the windmill, and we entered into an aggreement with him to hand over Animal Farm to a neighboring farm."
    pig "Snowball admitted to us that he's been a secret agent for years past..."
    hide pig 
    scene bg killing_pigs 
    pause 3
    scene bg barn_out 
    show n nonchalant at center
    n "Does any other animal have anything to confess?"
    hide n
    "Do the hens confess?"
    menu:
        "Yes":
            show ria neutral at center
            h "Three of us have been the ringleaders in an attempted rebellion over the eggs that were taken from us..."
            h "Snowball appeared to us in a dream and incitedus to disobey your orders Leader Napoleon."
            hide ria
            show bg hens_dead
            pause 3
            scene bg black_screen
            "Do the sheep confess?"
            menu:
                "Yes":
                    show sh neutral at center
                    sh "We have something to confess too!"
                    sh "One of us urinated in the drinking pool and the rest of us murdered and old ram, an especially devoted follower of yours..."
                    sh "We chased the ram around a bonfire when he was suffering from a cough."
                    sh "We are terribly sorry, please spare us!"
                    hide sh
                    show bg sheep_dead   
                    pause 3
                    show bg black_screen
                    "Does a goat confess?"
                    menu:
                        "Yes":
                            show mur neutral at center
                            goat "I confess."
                            hide mur
                            show n nonchalant at center
                            n "To what?"
                            n "What is your crime?"
                            hide n 
                            show mur neutral at center
                            goat "I stole milk!"
                            hide mur
                            scene goat_dead
                        "No":
                            return
                "No":
                    return
        "No":
            return
    scene bg after_slaughter
    pause 3
    sar "I can't believe what just happened..."
    sar "Until today, no animal has ever killed another animal..."
    b "I do not understand it."
    b "I would not have believed that such things could happen to our farm."
    b "It must be due to some fould in ourselves."
    b "The solution, as I see it, is to work harder."
    b "From now onwards, I shall get up a full hour earlier in the mornings."
    c "This is not what we aimed at when we set ourseles years ago to work for the overthrow of the human race."
    c "These scenes of terror and slaughter are not what we looked forward to on that night when Old Major first stirred us to rebellion."
    c "If I have any picture of the future, it is of a society of animals set free from hunger and the whip, all equal, each working according to our capacity, the strong protecting the weak."
    c "Instead - I do not know why - we have come to a time when no one dares speak their mind."
    c "When fierce, growling dogs roam everywhere..."
    c "And when you have to watch your comrades torn to pieces after confessing to shocking crimes."
    c "There is no thought of rebellion or disobedience in my mind."
    c "I know that, even as things were, we are far better off than we were in the days of Jones, and that before all else, it is needful to prevent the return of human beings."
    c "Whatever happens, I will remain faithful, work hard, carry out the orders that are given to me, and accept the leadership of Napoleon."
    c "But still, this is not what me and all you had hoped for."
    c "It is not for this that we built the windmill and faced the bullets of Jones' gun."
    show bg barn_out 
    show sq neutral at center
    sq "Comrades."
    sq "By special decree of Comrade Napoleon, Beasts of England has been abolished."
    sq "From now onwards, it is forbidden to sing it."
    hide sq 
    show mur shocked at center
    mur "Why???"
    hide mur 
    show sq neutral at center
    sq "It's no longer needed, ccomrade." 
    sq "Beasts of England was the song of the Rebellion."
    sq "But the Rebellion is now completed."
    sq "The excecution of the traitors this afternoon was the final act."
    sq "The enemy, both external and internal, has been defeated."
    sq "In Beasts of Englad, we expressed our longing for a better society in days to come."
    sq "But that society has now been established."
    sq "Clearly, this song has no longer any purpose."
    hide sq 
    show sh neutral at center
    sh "Four legs good, two legs bad!"
    hide sh 
    show sq neutral at center
    sq "Since Beasts of England is no longer needed, allow our fellow pig Minimus to introduce to you the new song that will be sung every SUnday after the hoisting of the flag."
    sq "It begins like this:"
    hide sq 
    "Animal Farm, Animal Farm"
    "Never through me shalt thou come to harm!"
    show sar resent at center
    sar "This doesn't have the same ring to it as Beasts of England..."
    jump ending2_chapter8

#boxer's choice 
label boxers_choice:
    "Does Boxer speak up against Napoleon?"
    menu:
        "Yes":
            show b neutral at center
            jump boxers_choice_yes
        "No":
            return

#boxer's choice: Yes
label boxers_choice_yes:
    show b neutral at center
    b "I do not believe that!"
    b "Snowball fought bravely at the Battle of the Cowshed."
    b "I saw him myself."
    b "Did we not give him 'Animal Hero, First Class' immediately afterwards?"
    hide b 
    show sq neutral at center
    sq "That was our mistake."
    sq "For we know now - it is all written down in the secret documents that we have found - that in reality he was trying to lure us to our doom!"
    hide sq
    show b neutral at center 
    b "But he was wounded!"
    b "We all saw him running with blood."
    hide b 
    show sq neutral at center
    sq "That was part of the arrangement!"
    sq "Jone's shot only grazed him."
    sq "I could show you this in his own writing if you were able to read it."
    sq "The plot was for Snowball, at the critical moment, to give the signal for flight and leave the field to the enemy."
    sq "And he very nearly succeeded - I will even say, comrades, he would have succeeded..."
    sq "...had it not been for our heroic Leader, Comrade Napoleon!"
    sq "Do you not remember how, just at the moment when Jones and his men had got inside the year, Snowball suddenly turned and fled, and many animals followd him?"
    sq "And do you not reemmber, too, that it was just at that moment, when panic was spreading and all seemed lost, that Comrade Napoleon sprang forward?"
    sq "H cried 'Death to Humanity!' and sank his teeth in Jone's leg?"
    sq "Surely you remember that, comrade?"
    hide sq 
    show b neutral at center
    b "I do not believe that Snowball was a traitor at the beginning."
    b "What he has done since is different."
    b "But I believe that at the Battle of the Cowshed he was a good comrade."
    hide b 
    show sq neutral at center
    sq "Our Leader, Comrade Napoleon, has stated categorically, that Snowball was Jone's agent from the very begging."
    sq "Even long before the Rebellion was ever thought of!"
    hide sq 
    show b neutral at center 
    b "Ah, that is different!"
    b "If Comrade Napoleon says it, it must be right!"
    hide b 
    show sq neutral at center
    sq "That is the true spirit, comrade!"
    sq "I warn every animal on this farm to keep their eyes very wide open."
    sq "For we have reason to hink that some of Snowball's secret agents are lurking among us at this moment!"