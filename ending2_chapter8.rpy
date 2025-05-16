label ending2_chapter8:
    scene bg some_days_later
    pause 3
    scene bg barn_out
    show c neutral at center
    c "Sarlot, I need to talk to you."
    hide c 
    show sar neutral at center
    sar "Hey Clover, what's up?"
    hide sar 
    show c sad at center
    c "We're friends, right?"
    hide c 
    show sar sad at center
    sar "Of course we are, why would you even ask that?"
    hide sar 
    show c sad at center
    c "You've been acting weird lately..."
    hide c 
    show sar sad at center
    sar "What?"
    sar "How?"
    hide sar 
    show c sad at center
    c "I know you've been talking with Napoleon."
    c "I saw you."
    c "No other animal has that direct contact with him but you."
    c "If we really are friends, you'll tell me what's going on."
    hide c 
    "What will Sarlot do?"
    menu:
        "Deny everything and lie to Clover":
            show sar shocked at center
            sar "Clover!"
            sar "How dare you accuse me of such thing?"
            hide sar
            show c shocked at center
            c "I saw you Sarlot, with my own two eyes!"
            c "You even were by his ear in a meeting!"
            hide c 
            show sar shocked at center
            sar "What business would I have by Napoleon's ear?"
            hide sar 
            show c shocked at center
            c "I don't know Sarlot, that's why I'm asking you!"
            hide c
            show sar shocked at center
            sar "I'm offended that you'd even suspect me of something."
            sar "I'd never do such a thing!"
            sar "I'd never conspire with him on anything, you know that best."
            sar "I don't like the way he treats us and I want nothing to do with him."
            sar "Besides, I'm not even sure he knows I exist on the farm."
            hide sar 
            show c sad at center
            c "I guess you have a point."
            c "I'm sorry that I offended you."
            c "But please, if you're on to something, I'd like to know."
            c "Promise me that you'll tell me if something's going on."
            c "Promise me Sarlot!"
            c "You're amongst my only true friends here and I can't handle losing you!"
            hide c 
            show sar neutral at center
            sar "You have nothing to worry about, Clover."
            sar "You'll never lose me."
        "No":
            show sar sad at center
            sar "I have been talking with him, but it's not what you think."
            hide sar 
            show c shocked at center
            c "Then what is it?"
            c "And you'd better make it quick because you're on thin ice..."
            hide c 
            show sar shocked at center
            sar "All this time, we've been talking about how Napoleon has been treating us horribly and I couldn't stand here and not do anything..."
            sar "...so I told him our requests."
            sar "I told him what was troubling us."
            sar "That is the reason you've seen me by his side."
            hide sar
            show c sad at center
            c "What about you speaking to him in the meeting."
            hide c 
            show sar neutral at center
            sar "That I have no knowledge of, becase it wasn't me."
            sar "Maybe it was another spider, I don't know, but what I do know is that I never spoke in his ear during any of the meetings."
            sar "You have to believe me Clover, I'm on your side."
            hide sar 
            show c neutral at center
            c "Hm..."
            c "I believe you for now, but you'd better be careful Sarlot."
            c "If I catch you speaking to him again, I won't be this resilient."
            hide c
            show sar neutral at center
            sar "You can trust me Clover"
    show sar at center
    sar "{i}That was close..."
    sar "{i}I must be more careful when speaking with him for now on..."
    sar "{i}How did she even see him and I talk!"
    sar "{i}I'm a spider, sort of hard to spot..."
    sar "Let's move on Clover."
    sar "I heard some animals talk about the Sixth Commandment."
    hide sar 
    show c neutral at center
    c "Yeah, me too..."
    c "Some remember that the Sixth Commandment decreed:"
    c "'No animal shall kill any other animal'."
    hide c 
    show sar neutral at center
    sar "Let's ask Benjamin to read it for us."
    sar "I believe he's somewhere nearby."
    hide sar 
    show c neutral at center
    c "Hey, Benjamin!"
    c "Could you read something for us?"
    hide c 
    show ben neutral at center
    ben "No."
    ben "I refuse to meddle in such matters."
    hide ben
    show c sad at center
    c "Fine."
    c "I'll ask Muriel..."
    hide c 
    show c neutral at center
    c "Hey, Muriel!"
    c "Could you read the Sixth Commandment for us?"
    hide c 
    show mur neutral at center
    mur "Sure."
    mur "Ermmm..."
    mur "{i}'No animal shall kill any other animal without cause'"
    hide mur 
    show sar resent at center 
    sar "{i}They changed another one of the Commandments?"
    sar "{i}I must tell Napoleon and Squealer to be more discreet, otherwise the animals will figure out what's going on before I get the chance to complete my plan!"
    hide sar 
    show sq neutral at center
    sq "Comrades!"
    sq "This year, you all worked harder but it was for a good reason."
    sq "The production of every class of foodstuff has increased by three hundred per cent!"
    hide sq 
    show c neutral at center
    c "Squealer, you always say that we produce more food now than we did with Jones, but it doen't seem that way."
    c "We work harder every where but see no actual change, besides what you tell us!"
    c "Especially now that we're rebuilding the windmill!"
    c "And where is Napoleon?"
    c "We haven't seen him in forever!"
    c "Where is that leader of ours?"
    hide c
    show sq neutral at center
    sq "Leader Napoleon is busy."
    sq "Since you mention him though, Minimus has composed another poem for you all."
    sq "Here it is."
    hide sq 
    "Friend of the fatherless!"
    "Fountain of happiness!"
    "Lord of the swill-bucket!"
    "Oh, how my soul is on Fire"
    "when I gaze at thy Calm and commanding eye,"
    "Like the sun in the sky,"
    "Comrade Napoleon!"
    "Thou are the giver of All that thy creatures love,"
    "Full belly twice a day,"
    "clean straw to roll upon;"
    "Every beast great or small Sleeps at peace in his stall,"
    "Thou watchest over all,"
    "Comrade Napoleon!"
    "Had I a sucking-pig,"
    "Ere he had grown as big Even"
    "as a pint bottle or as a rolling-pin,"
    "He should have learned to be Faithful and true to thee,"
    "Yes, his first squeak should be 'Comrade Napoleon'"
    show sq neutral at center
    sq "Now that you all heard this new poem, I think it's time to inscribe it on the wall of the big barn!"
    hide sq 
    scene bg poem
    pause 3
    show sq neutral at center
    sq "Comrades, there's something else I must announce to you."
    sq "Napoleon has arranged to sell the pile of timber to Mr. Pilkington."
    sq "We are also to engage in trading certain products with Foxwood."
    sq "Now, the relations between Napoleon and Pilkington are almost friendly!"
    hide sq
    show c shocked at center
    c "But he's a Man!"
    hide c 
    show sq neutral at center
    sq "At least he's not Frederick!"
    sq "I'm sure you've heard how he treats his animals."
    sq "He has flogged an old horse to death, he has starved his cows, he has killed a dog by throwing it into the furnace, he amuses himself in the evenings by making cocks fight with splinters of razorblade tied to their spurs!"
    sq "And since Frederick treats our kind so badly, fro from now on no pigeon is allowed to set foot anywhere near Foxwood."
    sq "Also, they are to drop their former slogan 'Death to Humanity' in favour of 'Death to Frederick'!"
    sq "Now comrades, I was sadly informed that Snowball-"
    hide sq 
    "Should Sarlot sit and listen to Squealer?"
    menu:
        "Yes":
            show sq neutral at center
            sq "That Snowball has struck our farm again!"
            sq "The wheat crop was full of weeds and after some investigation, we discovered that it was a result of one of his nocturnal visits."
            sq "He came into the farm and mixed weed seeds with corn."
            sq "I should also inform you that Snowball had never - as many of you have believed - received the order of 'Animal Hero, First Class'."
            sq "This has been a mere legend, which has been spread some time after the Battle of Cowshed by Snowball himself!"
            hide sq
        "No":
            show sar resent at center
            sar "Oh god!"
            sar "Not this again!"
            sar "I can't stand listening to another moment of theories about Snowball!"
    scene bg autumn 
    pause 3 
    scene bg windmill_built
    pause 3
    scene bg windmill
    show n nonchalant
    n "Congratulations to you all."
    n "You all worked very hard for this to finally happen."
    n "I believe it's only right for the windmill to be named after me since it happened under my supervision."
    n "So, I'm happy to announce that the windmill will be named 'Napoleon's Mill'."
    hide n 
    scene bg meeting 
    pause 3 
    scene barn_in
    show n nonchalant at center
    n "I have to announce that I have sold the pile of timber to Frederick."
    hide n 
    show sar shocked at center
    sar "{i}What?"
    sar "{i}Was he in some secret agreement with Frederick this whole time?"
    sar "{i}Was his whole friendship with Pilkington just a hoax?"
    sar "{i}He didn't tell me about that!"
    hide sar 
    show n nonchalant at center
    n "All pigeons should change their slogan from 'Death to Frederick' to 'Death to Pilkington' immediately."
    n "I should also make something else clear."
    n "All the stories that have been going around about an impending attack on Animal Farm are completely untrue."
    n "All of them are rumours that originate from Snowball."
    hide n 
    show sq neutral at center
    sq "And just so you all can understand how smart our Leader Napoleon is, I'll tell you this."
    sq "By seeming to be friendly with Pilkington, he forced Frederick to raise his price by twelve pounds."
    sq "But the superior quality of Napoleon's mind, was shown in the fact that he trusted nobody, not even Frederick."
    sq "Frederick had wanted to pay for the timber with something called a cheque, which, it seemed, was a piece of paper with a promise to pay written upon it."
    sq "But Napoleon was too clever for him."
    sq "He had demanded payment in real five-pound notes, which were to be handed over before the timber was removed."
    sq "Already, Frederick had paid up; and the sum he had paid was just enough to buy the machinery for the windmill."
    hide sq 
    scene bg two_days_later
    pause 3
    scene barn_in
    show n angry at center
    n "GRAAAAAA!"
    n "The banknotes were forgeries!"
    n "Frederick got the timber for nothing!"
    n "Once we capture him, he should be boiled alive!"
    n "I must warn you that after this treacherous deed, the worst is to be expected."
    n "It is highly possible that Frederick and his men will make that long-expected attack at any moment."
    n "Squealer, sent pigeons to Foxwood immediately!"
    n "It is necessary that we reconciliate with them!"
    hide n 
    scene bg two_days_later
    pause 3 
    scene bg eating 
    pause 3
    scene barn_out 
    show sar shocked at center
    sar "Ah!"
    sar "There are fifteen men with half a dozen guns coming through the gate!"
    hide sar 
    scene bg jones_whips
    pause 3 
    scene barn_out
    b "Don't be afraid comrades!"
    hide b 
    show sar shocked at center
    sar "There's a pigeon coming with a message from Pilkington!"
    sar "{i}'Serves you right'"
    sar "What...?!"
    hide sar 
    show c shocked at center 
    c "They're trying to knock down the windmill!"
    c "They're drilling a hole at the bottom!"
    hide c 
    show n angry at center
    n "Impossible!"
    n "We have built the walls too thick for that!"
    n "They could not knock it down in a week."
    n "Courage, comrades!"
    hide n 
    show ben angry at center
    ben "Do you not see what they're doing?"
    ben "You see that hole that they're drilling?"
    ben "Any moment from now, they're going to pack blasting power into that hole."
    hide ben
    scene bg windmill_explosion
    pause 3
    scene bg windmill_destroyed
    pause 3 
    scene bg barn_in
    show b angry at center
    b "They can't keep getting away with this!"
    hide b 
    scene bg running 
    pause 3 
    scene bg black_screen 
    pause 3 
    scene bg barn_out 
    show b angry at center
    b "What is that gun firing for?"
    hide b 
    show sq excited at center 
    sq "To celebrate our victory!"
    hide sq 
    show b angry at center
    b "What victory?"
    b "My knees are bleeding, I've lost a show, split my hoof and a dozen pellets have lodged themselves in my hind legs!"
    hide b 
    show sq excited at center
    sq "What victory, comrade?"
    sq "Have we not driven the enemy off our soil - the sacred soil of Animal Farm?"
    hide sq 
    show b angry at center
    b "But they destroyed the windmill!" 
    b "And we had worked on it for two years!"
    hide b 
    show sq excited at center
    sq "What matter?"
    sq "We will build another windmill!"
    sq "We will build six windmills if we feel like it."
    sq "You do not appreciate, comrade, the mighty thing that we have done."
    sq "The enemy was in occupation of this very ground that we stand upon."
    sq "And now - thanks to the leadership of Comrade Napoleon - we have won every inch of it back again!"
    hide sq 
    show b angry at center
    b "Then we have won back what we had before!"
    hide b 
    show sq excited at center 
    sq "That's our victory!"
    hide sq 
    show b neutral at center 
    b "..."
    hide b 
    show b worried at center 
    b "Clover, I have to tell you something."
    hide b 
    show c neutral at center
    c "What's up Boxer?"
    c "Is everything okay?"
    hide c 
    "Should Boxer tell Clover what's bothering him?"
    menu: 
        "Yes":
            show b worried at center 
            b "I can already see the heavy labour of rebuilding the windmill from the foundations and I'm afraid that my muscles are not quite what they had been..."
            b "I am eleven years old after all..."
            hide b 
            show c neutral at center 
            c "Boxer, don't worry about that now."
            c "Napoleon is about to make a speech, we have to be present..."
            hide c 
        "No":
            show b worried at center 
            b "Nevermind..."
            b "Napoleon is about to make a speech."
            b "We should be present."
            hide b 
    show n nonchalant at center 
    n "Congratulations, comrades."
    n "We won a great victory today."
    n "Now we need to honour the animals who sacrificed themselves for this."
    n "Boxer and Clover, you shall pull the wagon."
    hide n 
    scene bg two_days_later
    pause 3 
    scene bg house 
    show c sad at center 
    c "I haven't seen any of the pigs in days..."
    hide c 
    show sar troubled at center 
    sar "They've been drinking all day from an old case of whisky that they found."
    sar "Yesterday, I saw Napoleon come out of the farmhouse for a while and he seemed drunk."
    sar "{i}It is true that the pigs have been drinking a lot."
    sar "{i}At first, it was a beer or two, a bit of whiskey but they've taken it too far."
    sar "{i}I can't even get a hold of Napoleon."
    sar "{i}He is too busy downing alcohol..."
    sar "{i}The last time I was able to speak to him, he was drunk out of his mind and I barely got out of the farmhouse!"
    sar "{i}He was going to smash me to death for protesting against his new drinking habit!"
    sar "Oh look, Squealer is coming over now."
    hide sar 
    show sq sad at center
    sq "Comrades!"
    sq "I have some terrible news to announce."
    sq "Comrade Napoleon is dying!"
    hide sq 
    show sar shocked at center 
    sar "{i}What?"
    sar "{i}What is Squealer saying?"
    sar "{i}This can't be true!"
    hide sar 
    show b worried at center 
    b "Oh no!"
    b "What will we do without our leader?"
    hide b 
    show ria neutral at center 
    ria "I heard that Snowball poisoned Napoleon's food!"
    hide ria 
    show sq sad at center 
    sq "As Comrade Napoleon's last act upon earth, he pronounces a solemn decree:"
    sq "the drinking of alcohol is to be punished by death!"
    hide sq 
    scene bg some_days_later
    pause 3 
    scene bg barn_in
    show sar neutral at center 
    sar "{i}Napoleon's near death experience was soon forgotten because just the next day he appeared to be better and soon came back to work."
    sar "{i}He gave orders that the small paddock beyond the orchard that was intended to be set aside as ground for the retired animals, was to be ploughed because it needed re-seeding..."
    sar "{i}Soon though, it became known that Napoleon intended to sow it with barley."
    hide sar 
    scene bg black_screen
    pause 3 
    scene bg farmhouse_night
    show mur concerned at center 
    mur "I thought the Fifth Commandment said 'No animal shall drink alcohol!'."
    mur "Oh, I guess we remembered it wrong because there on the wall it says 'No animal shall drink alcohol {i}to excess{/i}'..."
    jump ending2_chapter9
    return