#chapter3.rpy
#chapter 3 (main story)

label chapter3:
    scene barn_out
    show c neutral at center
    c "Another day, another hay!"
    hide c 
    show sar neutral at center
    sar "Haha, that's true!"
    sar "And the hay is for the animals and the animals only!"
    sar "We get everything that we produce."
    hide sar 
    show c neutral at center
    c "I know, but all the tools are made to be used by humans..."
    c "Work is harder than usual."
    hide c 
    show sar neutral 
    sar "True, but we are set to finish the harvest two days earlier than usual."
    hide sar 
    show c neutral at center 
    c "Yeah, that's true."
    c "On another note, have you seen Molly?"
    hide c 
    show sar sad at center
    sar "No..."
    sar "It's unusual, right?"
    sar "She always seems to join us late and leave early..."
    hide sar 
    show c sad at center 
    c "Not to mention the cat that's always absent, except when food is served!"
    hide c 
    show sar neutral at center 
    sar "Anyways..."
    sar "Sunday is coming and you know what that means..."
    hide sar 
    show c neutral at center 
    c "Yes, another meeting where Snowball and Napoleon fight the whole time."
    c "It's like they can't agree on anything!"
    hide c 
    show bet closeup at center 
    bet "Are you guys talking about Napoleon and Snowball?"
    hide bet 
    show sar neutral at center 
    sar "Yeah."
    sar "I think the only thing that they've agreed on is to make a small paddock for the retired animals."
    hide sar 
    show bet closeup at center 
    bet "They might not agree often, but they have done a great job in educating the farm."
    bet "Almost everybody has learned something!"
    bet "Even the animals who couldn't remember the commandments have learned the 'Four legs good, two legs bad' saying."
    bet "Especially the sheep!"
    bet "They love that saying!"
    hide bet
    show sar neutral at center
    sar "I guess that's true..."
    hide sar 
    show bet closeup at center 
    bet "Does anyone know what happened to Jessie and Bluebell's puppies?"
    hide bet 
    show sar neutral at center
    sar "Hm..."
    menu:
        "Sarlot explains to them.":
            sar "Yeah, Napoleon has taken them in to 'educate' them."
            sar "If you ask me, that seem's a bit weird..."
        "Keeps information to herself.":
            sar "I have no idea..."
            sar "But it's a bit weird that they just disappeared like that..."
    
    sar "What's also weird is that much of the milk and the apples seem to have disappeared..."
    hide sar
    show c neutral at center
    c "I know, but I think Squealer has something to say about that."
    c "He said earlier that we should all gather together so he can make the announcement."
    hide c
    show sq neutral at center 
    sq "Comrades!"
    sq "You do not imagine, I hope, that we pigs are taking in the milk and the apples in a spirit of selfishness and priveledge?"
    sq "Many of us actually dislike milk and apples!"
    sq "I dislike them myself!"
    sq "Our sole subject in taking these things is to preserve our health."
    sq "Milks and apples,"
    sq "and this has been proven by science comrades,"
    sq "contain substances absolutely necessary to the well-being of a pig."
    sq "We pigs are brainworkers."
    sq "The whole management and organization of this farm depends on us."
    sq "Day and night we are watching over your welfare."
    sq "It is for {i} your {/i} sake that we drink that milk and eat those apples."
    sq "Do you know what would happen if we pigs failed in our duty?"
    sq "Jones would come back!"
    sq "Yes, Jones would come back!"
    sq "Surely, comrades, there is no one among you who wants to see Jones come back?"
    hide sq 
    show sar troubled at center
    sar "{i} If there's one thing that us animals are completely certain of is that we don't want Jones back.{/i}"
    sar "{i} If that means that the pigs have to be in good health, so be it!{/i}"
    return
