label chapter4:
    scene bg barn_in 
    show sar neutral at center 
    sar "{i}By the late summer, the events that happened on the farm had crossed half the country and the pigs would send carrried pigeons to neighboring farms with information about the rebellion." 
    sar "{i}Pigeons say that the neighboring farmers are terrified of a revolution and try to abstract any information from getting in their farms." 
    sar "{i}The only thing that's for certain is that the animal farm's success has circulated in the entire countryside." 
    hide sar
    show pigeon neutral at center 
    pigeon "THEY ARE COMING!"
    hide pigeon
    show s neutral at center
    s "Clam down!"
    s "Who's coming?"
    hide s
    show pigeon neutral at center
    pigeon "JONES AND ABOUT HALF DOZEN MEN!"
    hide pigeon
    show s focused at center
    s "I'll go get the others!"
    hide s 
    scene bg first_attack
    pause 3
    scene bg barn_in
    show s confident at center
    s "Egg legion, CHARGE!"
    hide s 
    show mixed snowball_attack at center
    pause 3
    hide mixed
    show mixed egg_legion at center
    pause 3
    hide mixed
    show s confident at center
    s "Hoof Command, ATTACK!"
    hide s
    show mixed hoof_attack at center
    hide mixed 
    scene bg retreat
    pause 3
    scene bg barn_in
    show s confident
    s "Don't worry comrades, the battle isn't over yet!"
    s "This is all part of my plan!"
    hide s 
    scene all_according_to_plan
    pause 3
    show mixed boxer_ready_attack
    call choice_boxerr
    scene bg barn_in
    show c shocked at center
    c "Where is Mollie?"
    hide c
    show sar neutral
    sar "That's her over there!"
    hide sar
    scene bg head_in_hay_mollie 
    pause 3
    scene bg barn_in
    show s confident
    s "Comrades!"
    s "Today's battle will mark the history books of our farm."
    s "This win hasn't come without its costs and the lost aninmals will be honored."
    s "Despite the casualties, we must look forward because this was just the first big obstacle on our way."
    s "Every animal must be prepared to give its life to protect the farm."
    s "Because this is our principle, we must protect each other with all of our being."
    s "All animals are equal!"
    hide s 
    show sar neutral at center
    sar "The animals decided to create a military decoration, 'Animal Hero, First Class'."
    sar "That title was given to Snowball and Boxer."
    sar "Also, they created 'Animal Hero, Second Class', which was given to the dead sheep."
    sar "The battle was named Battle of the Cowshed, since that was where the ambush had been sprung."
    sar "Jones' gun was found laying in the mud and it was decided to set it up at the foot of the flagstaff and fire it once in the anniversary of the battle and once at the anniversary of the rebellion."
    return
    
    #menu for boxer's choice
    label choice_boxerr:
        hide mixed
        "Does Boxer kill the man?"
        menu: 
            "Yes":
                hide mixed
                call choice_boxer_yess
            "No":
                call choice_boxer_noo
        return

    #boxer's choice if "Yes"
    label choice_boxer_yess:
        scene barn_out
        show b worried at center
        b "He's dead!"
        b "I had no intention of doing that!"
        b "I forgot that I was wearing iron shoes."
        b "Who will believe that I did not do this on purpose?"
        hide b
        show s determined at center
        s "No sentimentality comrade!"
        s "War is war."
        s "The only good human being is a dead one."
        hide s 
        show b worried at center
        b "I have no wish to take life."
        b "Not even human life..."
        hide b 
        return
    
    #boxer's choice if "No"
    label choice_boxer_noo:
        scene bg running
        pause 3
        return 