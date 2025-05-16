label chapter7:
    scene bg meeting
    pause 3
    scene bg barn_in
    show sq neutral at center 
    sq "Comrades, it has been a bitter winter…"
    sq "Despite that though, you have all pulled through and managed to make significant progress on building the windmill!"
    sq "As you know, there is a significant shortage in food and the farm is struggling."
    sq "That is why the hens who are just coming in to lay must surrender their eggs."
    sq "Leader Napoleon has accepted a contract for four hundred eggs a week."
    sq "The price of these will pay for enough grain and meal to keep the farm going until summer comes and conditions are easier."
    hide sq
    "Do the hens protest against Napoleon’s decision?"
    menu:
        "Yes":
            jump yes_path
        "No":
            jump no_path

label yes_path:
    hide sq
    show n angry at center 
    n "SILENCE!"
    n "From now on, any animal that gives so much as a grain of corn to a hen is to be punished by death!"
    hide n
    show ria neutral at center
    ria "No!"
    ria "You cant take our eggs and keep our corn away too!"
    hide ria
    scene bg hens_attacking
    pause 3
    scene bg barn_in
    show n angry at center 
    n "Dogs! Take these traitors away now!!!!!!"
    scene bg killing_hens
    pause 3
    scene bg some_days_later
    pause 5
    hide n
    scene bg barn_in
    show sar sad at center 
    sar "I haven’t seen a hen since that meeting… Nine hens have died in the  meantime, supposedly from coccidiosis…"
    jump no_path


label no_path:
    scene bg some_days_later
    pause 3
    scene bg barn_in
    show sar neutral at center 
    sar "Napoleon is now on slightly better terms with the other farmers."
    sar "Even though no one had seen Snowball, Squealer informed us that he was secretly frequenting the farm by night!"
    sar "Peculiar things were happening all around the farm and the only logical explanation was that Snowball has come in the night and done them."
    sar "All this led to Napoleon becoming obsessed with going after Snowball, looking everywhere for clues."
    sar "Oh, all the animals are leaving! There must be a meeting…"
    hide sar
    show sq neutral at center 
    sq "Comrades, the most terrible thing has been discovered."
    sq "Snowball has sold himself to Frederick of Pinchfield Farm, who is even now plotting to attack us and take our farm away from us!"
    sq "Snowball is to act as his guide when the attack begins."
    sq "But there is worse than that. We had thought that Snowball's rebellion was caused simply by his vanity and ambition."
    sq "But we were wrong, comrades. Do you know what the real reason was?"
    sq "Snowball was in league with Jones from the very start! He was Jones's secret agent all the time."
    sq "It has all been proved by documents which he left behind him and which we have only just discovered."
    sq "To my mind this explains a great deal, comrades."
    sq "Did we not see for ourselves how he attempted-fortunately without success-to get us defeated and destroyed at the Battle of the Cowshed?"
    hide sq
    show b worried at center 
    b "..."
    "What will Boxer do?"
    menu:
        "Speaks up against Napoleon":
            jump yes1_path

        "Stay silent":
            jump no1_path

label yes1_path:
    scene bg barn_in
    show b angry at center 
    b "I do not believe that! Snowball fought bravely at the Battle of the Cowshed"
    b "I saw him myself. Did we not give him “Animal Hero, First Class” immediately afterwards?"
    hide b
    show sq neutral at center 
    sq "That was our mistake, comrade. For we know now – it is all written down in the secret documents that we have found – that in reality he was trying to lure us to our doom!"
    hide sq
    show b angry at center 
    b "But he was wounded! We all saw him running with blood."
    hide b
    show sq frustrated at center 
    sq "That was part of the arrangement! Jone’s shot only grazed him."
    sq "I could show you tis in his own writing if you were able to read it."
    sq "The plot was for Snowball, at the critical moment, to give the signal for flight and leave the field to the enemy."
    sq "And he very nearly succeeded – I will even say, comrades, he would have succeeded if it had not been for our heroic Leader, Comrade Napoleon"
    sq "Do you not remember how, just at the moment when Jones and his men had got inside the yard, Snowball suddenly turned and fled, and many animals followed him?"
    sq "And do you not remember, too, that it was just at that moment, when panic was spreading and all seemed lost, that Comrade Napoleon sprang forward with a cry of “Death to Humanity!” and sank his teeth in Jone’s leg?"
    sq "Surely you remember that, comrade?"
    hide sq
    show b angry at center 
    b "I do not believe that Snowball was a traitor at the beginning. What he has done since is different."
    b "But I believe that at the Battle of the Cowshed he was a good comrade"
    hide b 
    show sq neutral at center
    sq "That is the true spirit, comrade! I warn every animal on this farm to keep his eyes very wide open."
    sq "For we have reason to think that some of Snowball's secret agents are lurking among us at this moment!" 
    hide sq
    jump no1_path
    

label no1_path:
    scene bg some_days_later
    pause 3
    scene bg meeting
    pause 3
    scene bg killing_pigs
    pause 3
    scene bg barn_out
    show n nonchalant at center 
    n "You four pigs that have been protesting me all this time, CONFESS YOUR CRIMES!"
    hide n
    "What will the pigs do?"
    menu:
        "Confess their crimes":
            jump confess_path
        "Speak up against Napoleon's actions":
            jump speak_up_path

label speak_up_path:
    call ending4 from _call_ending4

label confess_path:
    scene bg barn_out
    show sq sad at center
    show sq sad at center
    mar "We have been secretly in touch with Snowball ever since his expulsion."
    mar "We collaborated with him in destroying the windmill, and we entered into an agreement with him to hand over Animal Farm to a neighboring farm."
    hide sq
    jump pathing

label pathing:
    show n irritated at center 
    n "Dogs! Take care of these traitors..."
    hide n
    scene bg black_screen
    pause 3
    scene bg barn_out
    show n nonchalant at center 
    n "Does any other animal have anything to confess?"
    hide n
    "Will the hens confess?"
    menu:
        "Yes":
            jump yes2_path
        "No":
            jump no2_path

label yes2_path:
    scene bg barn_out
    show ria neutral at center 
    ria "Three of us have been the ringleaders in an attempted rebellion over the eggs that were taken from us!" 
    ria "Snowball appeared to us in a dream and incited us to disobey your orders Leader Napoleon."
    hide ria
    scene bg hens_dead
    pause 3
    jump no2_path

label no2_path:
    scene bg barn_out
    "Does the chicken confess"
    menu:
        "Yes":
            jump yes3_path

        "No":
            jump no3_path

label yes3_path:
    scene bg barn_out
    show ria neutral at center 
    h "I have something to confess as well! I secreted six ears of corn during the last year’s harvest and eaten them in the night!"
    hide ria
    scene bg hen_dead
    pause 3
    jump no3_path

label no3_path:
    scene bg barn_out
    "Will the sheep confess?"
    menu:
        "Yes":
            jump yes4_path

        "No":
            jump no4_path

label yes4_path:
    scene bg barn_out
    show sh neutral at center 
    sh "We have something to confess too!"
    sh "One of us urinated in the drinking pool and the rest of us murdered an old ram, an especially devoted follower of yours Comrade Napoleon!"
    sh "We chased the ram around a bonfire when he was suffering from a cough. We are terribly sorry, please spare us!"
    hide sh
    scene bg sheep_dead
    pause 3
    jump no4_path

label no4_path:
    scene bg barn_out
    "Will the goat confess?"
    menu:
        "Yes" :
            jump yes5_path
        "No" :
            jump no5_path

label yes5_path:
    scene bg barn_out
    show mur sad at center
    goat "I confess."
    hide mur
    show n irritated at center 
    n "To what? What is your crime"
    hide n
    show mur sad at center 
    goat "I stole milk!"
    hide mur
    scene goat_dead
    pause 3
    jump no5_path

label no5_path:
    scene after_slaughter
    pause 3
    scene bg house
    show sar troubled at center
    s "I can’t believe what just happened… Until today, no animal has ever killed another animal…!"
    hide sar
    show b worried at center 
    b "I do not understand it. I would not have believed that such things could happen on our farm."
    b "It must be due to some fault in ourselves."
    b "The solution, as I see it, is to work harder. From now onwards I shall get up a full hour earlier in the mornings."
    hide b
    show c sad at center
    c "This is not what we aimed at when we set ourselves years ago to work for the overthrow of the human race"
    c "These scenes of terror and slaughter are not what we looked forward to on that night when old Major first stirred us to rebellion."
    c "If I have any picture of the future..."
    c "It is of a society of animals set free from hunger and the whip, all equal, each working according to our capacity, the strong protecting the weak, as I protected the lost brood of ducklings with my foreleg on the night of Major's speech."
    c "Instead - I do not know why - we have come to a time when no one dares speak their mind, when fierce, growling dogs roam everywhere, and when you have to watch your comrades torn to pieces after confessing to shocking crimes."
    c "There is no thought of rebellion or disobedience in my mind. I know that, even as things were, we are far better off than we were in the days of Jones, and that before all else it is needful to prevent the return of the human beings."
    c "Whatever happenes I will remain faithful, work hard, carry out the orders that are given to me, and accept the leadership of Napoleon."
    c "But still, this is not what me and all you had hoped for. It is not for this that we built the windmill and faced the bullets of Jones's gun."
    c "*singing beasts of England*"
    hide c
    show sq neutral at center 
    sq "By a special decree of Comrade Napoleon, Beasts of England had been abolished. From now onwards it is forbidden to sing it"
    hide sq
    show mur shocked at center 
    mur "WHY????"
    hide mur
    show sq neutral at center 
    sq "It's no longer needed, comrade. Beasts of England was the song of the Rebellion. But the Rebellion is now completed"
    sq "The execution of the traitors this afternoon was the final act. The enemy both external and internal has been defeated."
    sq "In Beasts of England we expressed our longing for a better society in days to come. But that society has now been established"
    sq "Clearly this song has no longer any purpose."
    hide sq
    show sh neutral at center 
    sh "Four legs good, two legs bad."
    hide sh
    show sq neutral at center 
    mi "Since Beasts of England is no longer needed, allow me to introduce to you the new song that will be sung every Sunday after the hoisting of the flag. It begins like this:"
    mi "Animal Farm, Animal Farm"
    mi "Never through me shalt thou come to harm!"
    hide sq
    show sar troubled at center 
    sar "Neither the words nor the tune of this song has the same worth as Beasts of England…"
    hide sar
    return