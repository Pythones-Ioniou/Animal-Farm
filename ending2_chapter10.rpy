label ending2_chapter10:
    scene bg barn_out
    show sar neutral at center 
    sar "{i}Jones did come, sooner than expected." 
    sar "{i}He came in the farm with his men and raided the farmhouse."
    sar "{i}The pigs were all gathered and were brought out before us." 
    hide sar 
    scene bg house 
    show jon neutral at center 
    jon "Firstly, my animals, I'd like to apologize." 
    jon "When Sarlot came to me, she told me that I treated you horribly while I oversaw the farm." 
    jon "At first, I was hostile towards her." 
    jon "I couldn't believe that I was that cruel towards you." 
    jon "While I sat in exile from the farm, I thought it over and realized that I did mistreat all of you and for that I am very sorry." 
    jon "I vow to be better from now on." 
    jon "Things will be different from now on." 
    jon "You chose me as your leader now and I shall live up to that expectation!" 
    hide jon 
    show sar shocked at center 
    sar "{i}Wow..."
    sar "{i}That was a pleasant surpise!" 
    sar "{i}I never expected Jones to come around and be so reasonable!" 
    hide sar 
    show jon neutral at center 
    jon "I now bring before you these pigs that have been your tyrants all this time." 
    jon "It's time you have the justice that you all deserve." 
    jon "If anyone has something to say to them, now is the time." 
    hide jon 
    "What does Napoleon do?" 
    menu: 
        "Expose Sarlot for manipulating him into becoming a horrible leader.": 
            show n worried at center 
            n "Comrades, I didn't know that you held so negative feelings over me." 
            n "It is true, I was selfish and cruel to you." 
            n "I did become a tyrant." 
            n "Power took over me." 
            n "But it wasn't all my doing!" 
            n "You have a traitor amongst you and you have yet to realize it." 
            hide n 
            show c angry at center 
            c "Don't try to distract us with your lies Napoleon!" 
            c "The only traitors here are you and the rest of the pigs." 
            hide c 
            show n angry at center 
            n "You all are so naïve." 
            n "Sarlot, don't be shy." 
            n "Confess!" 
            hide n 
            show sar shocked at center 
            sar "Confess to what, Napoleon?" 
            hide sar 
            show n angry at center 
            n "Don't act like you don't know what I'm talking about!" 
            n "Comrades, Sarlot has been my consultant ever since the rebellion happened." 
            n "She's been giving me advice on how to become the ruler of the farm." 
            n "She's managed to fool you all." 
            n "She acted like your friend but in reality she was just an informant for me!" 
            hide n 
            show c angry at center 
            c "So it is true, Sarlot!" 
            c "You were whispering in Napoleon's ear in all those meetings!" 
            hide c 
            show sar shocked at center 
            sar "Are you really going to believe this traitor to our kind over me?" 
            sar "Do you really think that I would do such thing?" 
            hide sar 
            show c angry at center 
            c "It makes sense though!" 
            c "It all makes sense..." 
            c "Why would you do that?" 
            hide c 
            show sar shocked at center 
            sar "I didn't do anything!" 
            sar "Clover!" 
            sar "Comrades!" 
            sar "You have to believe me!" 
            sar "I am innocent!" 
            hide sar 
            show bet closeup at center 
            bet "Sarlot, confess!" 
            bet "Be noble and confess!" 
            hide bet 
            "Does Sarlot confess?" 
            menu: 
                "Yes":
                    show sar resent at center 
                    sar "Fine." 
                    sar "What Napoleon speaks of is true." 
                    sar "I did conspire with him to take over the farm..." 
                    sar "...but before you condemn be, listen to my motives!" 
                    sar "When Old Major made that speech, I was worried." 
                    sar "I knew the rebellion was bound to happen, but I did not believe in it." 
                    sar "It was a flawed idea from the start." 
                    sar "We animals are not fir for independence." 
                    sar "Yes, somethign had to be done because our living conditions were horrible, but I did not believe that we would be successful in running a farm by ourselves." 
                    sar "That's why I made a deal with Jones when the talk of rebellion was getting serious." 
                    sar "I told him that I'd help him win the farm back and in return I demanded better living conditions for us." 
                    sar "My plan was to pick someone that had an inclination for leadership and corrupt them so you all could realize that having Jones is better than being without him." 
                    sar "I did it all for the good of the farm, you must realize that!" 
                    sar "My ways were unethical, but I had good intentions!" 
                    sar "Surely, no-one here can deny that I care for the farm, right?" 
                    hide sar 
                    show c angry at center 
                    c " I'm not sure about that anymore, Sarlot." 
                    c "You were dishonest." 
                    c "You lied to us." 
                    c "You deceived us." 
                    c "I don't care what your motives were, you should be up there with Napoleon." 
                    hide c 
                    show sar shocked at center 
                    sar "No!" 
                    sar "Comrades, please!" 
                    sar "I'm so very sorry for deceiving you!" 
                    sar "I had good intentions, I swear!" 
                    hide sar 
                    show c angry at center 
                    c "But how can we even be sure you're telling us the truth now?" 
                    hide c 
                    show sar shocked at center 
                    sar "Ask Jones!" 
                    hide sar 
                    show c angry at center 
                    c "Jones may know about your deal but only you know your motives and intentions." 
                    c "You should be brought to justice for manipulating all of us!" 
                    scene bg sarlot_captured 
                    pause 3 
                    scene bg barn_out
                    show jon neutral at center 
                    jon "What do you want to be done with these traitors?" 
                    hide jon 
                    show bet closeup at center 
                    bet "They should be executed!"
                    hide bet 
                    show c neutral at center 
                    c "No, Betty." 
                    c "That isn't right."
                    c "The Commandments still apply." 
                    c "The real Commandments, not the altered ones." 
                    c "No animal shall kill any other animal." 
                    hide c 
                    show bet closeup at center 
                    bet "Then what should we do with them?" 
                    hide bet 
                    show c neutral at center 
                    c "I believe the pigs should start living the way we lived all this time." 
                    c "They should work day and night, be withheld food and have no oil for the lamps in their stalls." 
                    c "As for Sarlot, she should be contained somewhere, never to communicate with any of us again." 
                    c "I don't want a traitor and a manipulator walking freely among us ever again." 
                    hide c 
                    show sar shocked at center 
                    sar "No Clover!" 
                    sar "We are friends, remember?" 
                    hide sar 
                    show c angry at center 
                    c "We were friends, but you betrayed me." 
                    c "You betrayed us!"
                    c "I want nothing to do with you anymore Sarlot." 
                    c "I'm ashamed that I was ever your friend in the first place..." 
                    hide c 
                    show jon neutral at center 
                    jon "Now that that's settled, I have a proposition for you." 
                    jon "I think you should elect an ambassador for you kind." 
                    jon "Someone to talk to me about matters that upset you, any requests that you may have or improvements for the farm." 
                    jon "I want us to live in harmony and I believe this is the way." 
                    hide jon 
                    show ria neutral at center 
                    ria "I think it should be Clover." 
                    ria "She's always been reasonable and has never failed the farm." 
                    ria "Also, she's reaching the age of retirement." 
                    ria "She's wiser than any of us here." 
                    hide ria 
                    show bet closeup at center 
                    bet "I agree." 
                    bet "Clover is a good fit!" 
                    hide bet 
                    all "We want Clover!" 
                    show jon neutral at center 
                    jon "Then I think it's settled!" 
                    scene bg black_screen
                    "Years later..." 
                    scene bg kitchen_dark 
                    show sar sad at center 
                    sar "Life in this box has been so mundane..." 
                    sar "The only one who speaks to me now is Jones, who's passed the farm over to his sons..." 
                    sar "He usually keeps me in his bedside table." 
                    sar "The alliance between humans and animals has been going well." 
                    sar "Clover really was a good fit for a represantor of the animals." 
                    sar "She's helped improve the farm so much, it's admirable." 
                    sar "Jones' sons are also doing a good job in overseeing the farm." 
                    sar "It is said that our farm is doing the best amongst all farms in England." 
                    sar "Also, Jones never switched back the farm name." 
                    sar "He kept it Animal Farm." 
                    sar "He said since they're working together now, there's no need to change it back." 
                    sar "As for the pigs, most of them died some years ago." 
                    sar "They had damaged their bodies from drinking alcohol so much that when put to labour they gave in." 
                    sar "Only Napoleon and Squealer are still alive now, who still are made to work even though they should be out on pension." 
                    sar "Jones and Clover say that they're to work until they die, to pay for their heinous crimes." 
                    sar "I've had plenty of time to think while confined in a box." 
                    sar "I concluded that I do not regret what I did all those years back, even if that cost me my freedom." 
                    sar "I may be confined in a box, leading a horrible last few years but at least the farm is doing well." 
                "No":
                    show sar shocked at center 
                    sar "I have nothing to confess!" 
                    sar "How dare you believe Napoleon over me!" 
                    sar "When have I ever done anything to give off the impression that I'd betray our farm?" 
                    hide sar 
                    show c neutral at center 
                    c "The truth is that Sarlot really hasn't done anything for us to believe Napoleon over her." 
                    c "For all we know, this is a last desperate attempt for Napoleon to save himself by shifting the blame from him to someone else..." 
                    hide c 
                    show n angry at center 
                    n "But it's true!" 
                    n "You must believe me in this!" 
                    n "I know I've lied and cheaeted all this time, but I speak truth on this!" 
                    n "Sarlot is a vicious manipulator..." 
                    hide n 
                    show c angry at center 
                    c "You are truthful when you say that you've lied and cheated but I doubt you speak any more truths than that."
                    hide c 
                    show jon neutral at center 
                    jon "Now that this matter was settled, what would you want to be done with these traitors?" 
                    hide jon 
                    show c angry at center 
                    c "I think they should be treated the same way they treated us." 
                    c "They should withheld food and made to work twice as hard as we worked, to make up for all their crimes." 
                    hide c 
                    show bet closeup at center 
                    bet "I want them dead!" 
                    bet "Don't you remember what they did to Boxer?" 
                    hide bet 
                    show c sad at center 
                    c "Of course..." 
                    c "Of course I remember what they did to my Boxer." 
                    c "I'll never forget that..." 
                    hide c 
                    show c angry at center 
                    c "But death is an easy way out and I don't want that for them!" 
                    c "I want them to suffer the same way we did when they ruled over us!" 
                    c "They need to realize how terribly they treated us." 
                    hide c 
                    show sar neutral at center 
                    sar "I agree with Clover." 
                    sar "Besides that though, don't you all remember the Sixth Commandment?" 
                    sar "The true one." 
                    sar "'No animal shall kill any other animal'." 
                    sar "We shouldn't sentence our fellow kind to death." 
                    hide sar 
                    show ria neutral at center 
                    ria "That's true." 
                    ria "I agree with Sarlot and Clover." 
                    hide ria 
                    show sar neutral at center 
                    sar "We should vote." 
                    sar "Everyone in favour of their death speak up." 
                    hide sar 
                    pause 3 
                    show jon neutral at center 
                    jon "Now that that's settled, I have a proposition for you." 
                    jon "I think you should elect an ambassador for your kind." 
                    jon "Someone to talk to me about matters that upset you, any requests that you may have or improvements for the farm." 
                    jon "I want us to live in harmony and I believe this is the way." 
                    hide jon 
                    show ria neutral at center 
                    ria "I think it should be Clover." 
                    ria "She's always been reasonable and has never failed the farm." 
                    ria "Also, she's reaching the age of retirement." 
                    ria "She's wiser than any of us here." 
                    hide ria
                    show bet closeup at center 
                    bet "I agree." 
                    bet "Clover is good fit." 
                    hide bet 
                    all "We want Clover!" 
                    show jon neutral at center 
                    jon "It is settled then..." 
                    scene bg black_screen
                    "Years later..." 
                    scene bg entrance 
                    show sar neutral at center 
                    sar "The farm has been prospering these last few years." 
                    sar "Clover has done a great job at representing the animals and has helped a great deal in making the farm better for everyone." 
                    sar "It is even said that our farm is the most successful in the whole country!" 
                    sar "Jones never changed the name from Animal Farm back to Manor Farm." 
                    sar "He said that there was no need." 
                    sar "He liked the name after all and found it suitable since we all worked together now." 
                    sar "After a year or two, I don't really remember well, Jones passed the farm over to his sons since he deemed himself too old to oversee the farm." 
                    sar "He made it clear though that the farm was to work the same as it's been." 
                    sar "He said that if a son of his was to back to leading the farm the way he did before the rebellion, us animals are to kick him off the farm." 
                    sar "I've had a lot of time to think about my actions back then." 
                    sar "I still feel guilty for lying to my friends." 
                    sar "I feel guilty for tricking everyone and manipulating them, but I do not regret anything." 
                    sar "Everything turned out as expected, that's what matters." 
                    sar "It still bothers me though." 
                    sar "I have no one to tell and it's been eating at me all these years." 
                    sar "Maybe, now that I'm old and approaching death, I'll finally tell Clover..." 
        "Curse out the animals for overthrowing him":
            show n angry at center 
            n "You all are fools!" 
            n "Foolish and stupid animals!" 
            n "Do you really believe Jones?" 
            n "Do you believe that he's a changed man?" 
            n "If you do, you're extremely stupid and I feel sorry for you!" 
            n "You'll lead the same miserable and ravenous lives that you did back then, before the rebellion!" 
            hide n 
            show c angry at center 
            c "Napoleon, do you really think that you did good on this farm?" 
            c "Do you really think that all this time that you've been our leader, you were any different from how Jones was before the rebellion?" 
            hide c 
            show n angry at center
            n "Of course I was" 
            n "But you wouldn't know, you're not half as smart as I am." 
            hide n 
            show c angry at center 
            c "If you really think that you're any different from Jones then I'm sorry to be the one to tell you Napoleon, but it's you who is foolish and stupid." 
            c "You were even worse than him."
            hide c 
            show sq frustrated at center 
            sq "Comrades!" 
            sq "What you're doing is not right!" 
            sq "Leader Napoleon only wants what's best for you!" 
            sq "Please, come to your senses comrades!" 
            sq "This is not what you want, I'm sure of it." 
            hide sq 
            show sar evil at center 
            sar "Oh, but it is Squealer." 
            hide sar 
            show c angry at center 
            c "You have a lot of nerve, Squealer." 
            hide c 
            show sq sad at center 
            sq "Be reasonable comrades." 
            sq "We fought so hard to kick Jones off the farm, surely you don't want him back." 
            sq "I'm sure this all is a big misunderstanding!" 
            sq "It isn't late to turn him away again." 
            sq "Napoleon will forgive you for this act of treason, I'm sure of it." 
            sq "He's good and just." 
            hide sq 
            show c angry at center 
            c "Was he good and just when he took Boxer to his death?" 
            c "How dare you even say such words out loud?" 
            c "Do you really have no shame?" 
            hide c 
            show sq frustrated at center 
            sq "He didn't take Boxer to his death!" 
            sq "I thought that was clear enough." 
            sq "We talked about this, comrades." 
            sq "Boxer died peacefully in the hospital!" 
            hide sq
            show c angry at center 
            c "Do you really expect us to believe that?" 
            c "It's baffling that you think of us as such stupid animals." 
            c "We know what you did." 
            c "We know what Napoleon did and you'll pay for that." 
            hide c 
            show sq frustrated at center 
            sq "Clover, be reasonable." 
            sq "Napoleon wouldn't do such thing." 
            sq "I assure you." 
            hide sq 
            show n angry at center 
            n "Squealer, enough!" 
            n "Yes, I did take him to the knacker's to get killed." 
            n "That is true." 
            n "And you know why?" 
            n "Because he was of no use to us anymore." 
            n "He wasn't strong enough." 
            n "He fell." 
            n "I had no use for him, so I send him to the knacker's."
            n "You should be thanking me!" 
            n "His death meant something." 
            n "We got something out of that." 
            n "We got resources!" 
            n "I can't believe you all are so stupid that you cannot understand such a simple concept!" 
            hide n 
            show c angry at center 
            c "I'll kill you Napleon!" 
            c "I'll kill you with my bare hoofs!" 
            c "How dare you!" 
            hide c 
            show sar shocked at center 
            sar "No Clover!" 
            sar "It's not worth it!" 
            sar "Don't stoop down to his level, please!" 
            hide sar 
            show c angry at center 
            c "It's what he deseerves!" 
            c "The world doesn't haave a place for such a cruel pig!" 
            hide c 
            show n angry at center 
            n "Do it if you dare you stupid horse!" 
            hide n 
            show sar shocked at center 
            sar "Clover, death is the easy way out." 
            sar "Look at him, he's begging for you to kill him so that he doesn't have to face the consequences of his actions." 
            sar "We'll make him pay some other way, I promise you!" 
            hide sar 
            show c angry at center 
            c "But he killed Boxer!" 
            c "He killed my Boxer and he has to receive the maximum punishment!" 
            hide c 
            show sar shocked at center 
            sar "Clover, remember the Sixth Commandment..." 
            sar "'No animal shall kill any other animal'." 
            sar "Do not let your rage consume you." 
            sar "I'm just as angry as you are but we also must find a reason in that anger." 
            sar "We'll find a suitable punishment for him, I promise!" 
            hide sar 
            show c angry at center 
            c "Fine!" 
            c "But he will pay." 
            c "He can't get away with this." 
            c "Boxer should be avenged." 
            hide c 
            show sar sad at center 
            sar "He will be, I promise you." 
            hide sar 
            show jon neutral 
            jon "So, what is to be done with these traitors?" 
            hide jon 
            show sar neutral at center 
            sar "I believe that all the pigs, except Napoleon, are to live in the same conditions that they had us living in for so long." 
            sar "They are to be withheld foo, work all day with no day off, no retirement and no oil for the lamps in their stalls." 
            sar "They are to live in hunger, darkness and labour for the rest of their lives." 
            sar "Now, as for Napoleon..." 
            sar "He should be left to sleep on the hard floor, with limited ammount of food and water." 
            sar "No light in his stall either." 
            sar "He should work day and night, only getting an hour or two of sleep." 
            sar "He shall have no cntact with any of the animals in this farm and if anyone is caught talking to him, more hours of labour will be added to their schedule." 
            sar "Of course, that will be for the rest of his life, until he dies." 
            sar "When his death approached, he should be left to die starved and parched." 
            hide sar 
            show n angry at center 
            n "I will not work!" 
            n "Work isn't for pigs!" 
            n "We are smarter than all of you combined and you want me to work in the fields?" 
            n "No way!"
            n "I am not doing that!" 
            hide n 
            show sar evil at center 
            sar "Instead of protesting, you should be grateful that I am so resilient with you." 
            sar "You deserve far worse treatment." 
            hide sar 
            show c neutral at center 
            c "I can live with this punishment." 
            hide c 
            show jon neutral at center 
            jon "It is settled then!" 
            jon "The pigs are to start work effective immediately!" 
            jon "I also have a proposition for you." 
            jon "I think you should elect an ambassador for your kind." 
            jon "Someone to talk to me about matters that upset you, any requests that you may have or imporvements for the farm." 
            jon "I want us to live in harmony and I believe this is the way!" 
            hide jon 
            show ria neutral at center 
            ria "I think it should be Clover." 
            ria "She's always been reasonable and has never failed the farm." 
            ria "Also, she's reaching the age of retirement soon." 
            ria "She's wiser than any of us here..." 
            hide ria 
            show bet closeup at center 
            bet "I agree!" 
            bet "Clover is a good fit!" 
            hide bet 
            all "We want Clover!" 
            show jon neutral at center 
            jon "It is settled then!" 
            jon "Now, you animals are in need of a long due break from all the hard labour!" 
            jon "I'll prepare food for you immediately!"
            hide jon 
            scene bg black_screen
            "Years later..." 
            scene bg barn_out 
            show sar neutral at center 
            sar "Ah, retirement!" 
            sar "Such a wonderful thing, don't you agree Clover?" 
            hide sar 
            show c neutral at center 
            c "I do Sarlot!" 
            c "It's good to have the time for leisure after so long!" 
            hide c 
            show sar neutral at center 
            sar "I'm really proud of the way the farm turned out." 
            sar "Do you know that we are the most successful farm in the whole country?" 
            hide sar 
            show c neutral at center 
            c "I do!" 
            c "I heard Jones say it the other day." 
            hide c 
            show sar neutral at center 
            sar "It took us a long time and many hard days, but we finally did it!" 
            sar "We may not be free from humans, but we are in good terms with them." 
            sar "We finally know life without being enslaves to someone!" 
    scene bg end
    " "
    $ renpy.full_restart()