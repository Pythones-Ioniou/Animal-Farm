label chapter8:

    scene bg some_days_later
    pause 3
    scene bg barn_in
    show sar neutral at center
    sar "Hey Clover."
    sar "I heard some animals talk about the Sixth Commandment."
    hide sar
    show c happy at center
    c "Yeah, me too. Some remember that the Sixth Commandment decreed: ‘No animal shall kill any other animal’."
    hide c
    show sar neutral at center
    sar "Let’s ask Benjamin to read it for us. I believe he’s somewhere nearby."
    hide sar
    show c happy at center
    c "Hey Benjamin!"
    c "Could you read something for us?"
    hide c
    show ben neutral at center
    ben "No. I refuse to meddle in such matters."
    hide ben
    show c neutral at center
    c "*sigh* Fine. I’ll ask Muriel."
    hide c
    show c happy at center
    c "Hey Muriel."
    c "Can you read the Sixth Commandment for us?"
    hide c
    show mur happy at center
    mur "Sure!"
    show mur skeptical at center
    mur "Eeeeeeeeeeeeeeeee..."
    mur "'No animal shall kill any other animal without cause'"
    hide mur
    show sar troubled at center
    sar "Hmmmmm. Was it always like this? Either way, since that’s the way it’s written on the wall, I guess the Sixth Commandment wasn’t violated…"
    hide sar
    show sq neutral at center
    sq "Comrades! This year, you all worked harder but it was for a good reason. The production of every class of foodstuff has increased by three hundred per cent."
    hide sq
    show sar troubled at center
    sar "Squealer always says that we produce more food now than we did with Jones but it doesn’t seem that way despite us working harder than ever, especially now that we’re rebuilding the windmill."
    hide sar
    show c neutral at center
    c "Squealer, where is Napoleon?"
    hide c
    show sq suspicious at center
    sq "Leader Napoleon is busy."
    sq "Since you mention him though, Minimus has composed another poem for you all."
    sq "Go ahead Minimus!"
    hide sq
    show sq excited at center
    mi "Friend of fatherless!"
    mi "Fountain of happiness!"
    mi "Lord of the swill-bucket!"
    mi "Oh, how my soul is on Fire"
    mi "when I gaze at thy Calm and commanding eye,"
    mi "Like the sun in the sky,"
    mi "Comrade Napoleon!"
    mi "Thou are the giver of All that thy creatures love,"
    mi "Full belly twice a day,"
    mi "clean straw to roll upon;"
    mi "Every beast great or small Sleeps at peace in his stall,"
    mi "Thou watchest over all,"
    mi "Comrade Napoleon!Had I a sucking-pig,"
    mi "Ere he had grown as big Even"
    mi "as a pint bottle or as a rolling-pin,"
    mi "He should have learned to be Faithful and true to thee,"
    mi "Yes, his first squeak should be \"Comrade Napoleon!\""
    show sq neutral at center
    sq "Now that you all heard this new poem, I think it’s time to inscribe it on the wall of the big barn!"
    hide sq
    show bg poem
    pause 3
    show bg barn_in
    show sq neutral at center 
    sq "Comrades, there’s something else I must announce to you."
    sq "Napoleon has arranged to sell the pile of timber to Mr. Pilkington."
    sq "We are also to engage in trading certain products with Foxwood."
    sq "Now, the relations between Napoleon and Pilkington are almost friendly!"
    hide sq
    show c angry at center 
    c "But he’s a Man!"
    hide c
    show sq suspicious at center 
    sq "At least he’s not Frederick!"
    show sq frustrated at center
    sq "I’m sure you’ve heard how he treats his animals."
    sq "He haa flogged an old horse to death!"
    sq "He has starved his cows!"
    sq "He has killed a dog by throwing it into the furnace!"
    sq "He amuses himself in the evenings by making cocks fight with splinters of razorblade tied to their spurs."
    sq "And since Frederick treats our kind so badly, from now on no pigeon is allowed to set foot anywhere near Foxwood."
    show sq neutral at center
    sq "Also, they are drop their former slogan ‘Death to Humanity’ in favour of ‘Death to Frederick’!"
    sq "ALSO, I was sadly informed that Snowball-"
    "What will sarlot do?"
    menu:
        "Sit and listen to Squealer":
            jump listen_path
        "Leave":
            jump leave_path

label listen_path:
    scene bg barn_in
    show sq neutral at center 
    sq "...That Snowball has struck our farm again"
    sq "The wheat crop was full of weeds and after some investigation, we discovered that it was a result of one of his nocturnal visits"
    sq "He came into the farm and mixed weed seeds with the seed corn."
    sq "I should also inform you that Snowball had never – as many of you have believed – received the order of ‘Animal Hero, First Class’."
    sq "This has been a mere legend, which has been spread some time after the Battle of the Cowshed by Snowball himself!"
    hide sq
    jump leave_path

label leave_path:
    scene bg barn_in
    show sar troubled at center 
    sar "Not again with the theories about Snowball…"
    hide sar
    scene bg august
    pause 3
    scene bg windmill_built
    pause 3
    scene bg windmill_whole
    show n nonchalant at center 
    n "Congratulations to you all."
    n "You all worked very hard for this to finally happen."
    n "I believe it’s only right for the windmill to be named after me since it happened under my supervision."
    n "So, I’m happy to announce that the windmill will be named ‘Napoleon’s Mill’."
    hide n
    all "WOOHOOO"
    scene bg meeting
    pause 3
    scene bg barn_in
    show n nonchalant at center 
    n "I have come to announce that I have sold the pile of timber to Frederick."
    hide n
    show sar troubled at center 
    s "Was he in some secret agreement with Frederick this whole time? Was his whole friendship with Pilkington just a hoax?"
    hide sar
    show n irritated at center 
    n "All pigeons should change their slogan from ‘Death to Frederick’ to ‘Death to Pilkington’ immediately."
    n "I should also make something else clear."
    n "All the stories that have been going around about an impending attack on Animal Farm are completely untrue."
    n "All of them are rumours that originate from Snowball!"
    hide n
    show sq neutral at center 
    sq "To show you just how smart our leader Napoleon is.."
    sq "By seeming to be friendly with Pilkington he had forced Frederick to raise his price by twelve pounds."
    sq "But the superior quality of Napoleon's mind, said Squealer, was shown in the fact that he trusted nobody, not even Frederick."
    sq "Frederick had wanted to pay for the timber with something called a cheque, which, it seemed, was a piece of paper with a promise to pay written upon it."
    sq "But Napoleon was too clever for him. He had demanded payment in real five-pound notes, which were to be handed over before the timber was removed."
    sq "Already Frederick had paid up;and the sum he had paid was just enough to buy the machinery for the windmill."
    hide sq
    scene bg some_days_later
    pause 3
    scene bg barn_out
    show n angry at center 
    n "GRAAAAAAAAAAAAAA!"
    n "The banknotes were forgeries!"
    n "Frederick   got the timber for nothing!"
    n "Once we capture him, he should be boiled alive!"
    n "I must warn you that after this treacherous deed, the worst is to be expected."
    n "It is highly possible that Frederick and his men will make that long-expected attack at any moment."
    n "Squealer, sent pigeons to Foxwood immediately!"
    n "It is necessary that we reconciliate with them!"
    hide n
    scene bg some_days_later
    pause 3
    scene bg eating
    pause 3
    scene bg barn_out
    show sar shocked at center 
    sar "Ah! There are fifteen men with half a dozen guns coming through the gate."
    hide sar
    scene bg first_attack
    pause 3
    scene bg retreat
    pause 3
    scene bg black_screen
    "bam"
    pause 3 
    scene bg barn_in
    show b angry at center 
    b "Do not be afraid comrades!"
    hide b
    scene bg after_first_battle
    pause 3
    scene bg barn_in
    show sar neutral at center 
    sar "There is a pigeon coming with a message from Pilkington!"
    sar "‘Serves you right.’"
    hide sar
    show sar shocked at center 
    sar "???"
    hide sar
    show bet sad at center 
    bet "They’re trying to knock down the windmill!! They’re drilling a hole at the bottom!"
    hide bet
    show n angry at center 
    n "Impossible! We have built the walls too thick for that!"
    n "They could not knock it down in a week."
    n "Courage, comrades!"
    hide n
    show ben angry at center 
    ben "Do you not see what they are doing?"
    ben "In another moment they are going to pack blasting power into that hole."
    scene bg windmill_explosion
    pause 3
    scene bg barn_in
    show b angry at center 
    b "They can't keep getting away with it!"
    hide b
    show sar neutral at center 
    sar "Oh my, they are really going to attack the farmers! Agh, i cannot keep looking."
    sar "Wait a minute...They really did made the men go away!"
    sar "But... at what cost. So many animals died..."
    hide sar
    scene bg black_screen
    "bam"
    pause 3
    scene bg windmill_almostdestroyed
    show b worried at center 
    b "What is the gun firing for?"
    hide b
    show sq excited at center 
    sq "To celebrate out victory"
    hide sq
    show b neutral at center 
    b "What victory?"
    b "My knees are bleeding, I’ve lost a show, split my hoof and a dozen pellets have lodged themselves in my hind leg!"
    hide b
    show sq excited at center 
    sq "What victory, comrade? Have we not driven the enemy off our soil – the sacred soil of Animal Farm?"
    hide sq
    show b angry at center 
    b "But they destroyed the windmill!"
    b "And we had worked on it for two years!"
    hide b
    show sq suspicious at center 
    sq "What matter?"
    show sq neutral at center
    sq "We will build another windmill!"
    show sq excited at center
    sq "We will build six windmills if we feel like it."
    sq "You do not appreciate, comrade, the mighty thing that we have done."
    sq "The enemy was in occupation of this very ground that we stand upon."
    sq "And now – thanks to the leadership of Comrade Napoleon – we have won every inch of it back again!"
    hide sq
    show b neutral at center 
    b "Then we have won back what we had before."
    hide b
    show sq suspicious at center 
    sq "That is our victory"
    hide sq
    show bg barn_in
    show b worried at center 
    b "Clover, I have to tell you something."
    hide b
    show c sad at center 
    c "What’s up Boxer? Is everything okay?"
    "What will Boxer do?"
    menu:
        "Tell Clover what is bothering him":
            jump bothering_path
        "Keep it for himself":
            jump keep_path

label bothering_path:
    scene bg barn_in
    show b worried at center 
    b "I can already see the heavy labour of rebuilding the windmill from the foundations and I’m afraid that my muscles are not quite what they had been."
    b "I am eleven years old after all…"
    hide b
    show c sad at center 
    c "Boxer, don’t worry about that now."
    c "Napoleon is about to make a speech, we have to be present…"
    hide c
    jump continue_path

label keep_path:
    scene bg barn_in
    show b worried at center 
    b "Nevermind… Napoleon is about to make a speech. We should be present"
    hide b
    jump continue_path

label continue_path:
    scene bg barn_in
    show n nonchalant at center 
    n "Congratulations, comrades."
    n "We won a great victory today."
    n "Now we need to honour the animals who sacrificed themselves for this."
    n "Boxer and Clover, you shall pull the wagon."
    hide n
    scene bg black_screen
    pause 3
    scene bg two_days_later
    pause 3
    scene bg barn_in
    show c sad at center 
    c "I haven't seen any of the pigs in days…"
    hide c
    show sar shocked at center 
    sar "They’ve been drinking all day from an old case of whisky that they found. Yesterday, I saw Napoleon come out of the farmhouse for a while and he seemed drunk..."
    sar "Oh look, Squealer is coming over now."
    hide sar
    show sq sad at center 
    sq "Comrades! I have some terrible news to announce."
    sq "Comrade Napoleon is dying!"
    hide sq
    show b worried at center 
    b "Oh no! What will we do without our leader?!"
    hide b
    show ria neutral at center 
    h "I heard that Snowball poisoned Napoleon’s food!"
    hide h
    show sq sad at center 
    sq "As Comrade Napoleon’s last act upon earth, he pronounces a solemn decree: the drinking of alcohol is to be punished by death!"
    hide sq
    scene bg some_days_later
    pause 3
    scene bg barn_in
    show sar troubled at center 
    sar "Napoleon’s near death experience was soon forgotten because just the next day he appeared to be better and soon came back to work."
    sar "He gave orders that the small paddock beyond the orchard that was intended to be set aside as ground for the retired animals, was to be ploughed because it need re-seeding but it soon became known that Napoleon intended to sow it with barley."
    hide s
    scene bg black_screen
    pause 3
    scene bg barn_in
    show sar troubled at center 
    sar "What was that??"
    hide s
    show sar troubled at center 
    sar "Why is...Squealer on the floor. I'm sure he did something at the commandments again.."
    sar "Why else would he hold the paintbrush and have the dogs protecting him?"
    hide sar
    show mur concerned at center 
    mur "I thought the Fifth Commandment said ‘No animal shall drink alcohol’! Oh, I guess we remembered it wrong because there on the wall it says ‘No animal shall drink alcohol to excess’.."
    return 