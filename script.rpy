define Waitress = "Bartender"
define Waitress_Invert = "Bartender"
define Bar_stanger= "Sir Sloshington McBlubberpants the Third"
define Ride_offerer = "Stranger"
define Dwarf = "Shorty McShortstuff"
define Trader = "Trader"
define Goat = "Goat"
define stranger = "Stranger"
define Goat_left = "Left goat"
define Goat_right = "Right goat"

image bar1:
    "pic1.jpeg"
    zoom 1.5

image forrest:
    "Forrest.jpeg"
    zoom 2.30

image forrest2:
    "Forrest_2.jpeg"
    zoom 1.75

image scammer:
    "Dwarf_scammer.png"
    zoom 1


image desert:
    "Desert.jpeg"
    zoom 2.75

image desert_village:
    "Desert_village.png"
    zoom 2

image trader:
    "Trader.png"
    zoom 1.10

image tundra:
    "Tundra.webp"
    zoom 2

image tundra2:
    "ice_area.webp"
    zoom 2

image goat_male:
    "normal_goat_right.png"
    zoom 1.5

image goat_female:
    "normal_goat.png"
    zoom 1.5

image Angry_male:
    "Angry_goat_right.png"
    zoom 1.5

image Angry_female:
    "Angry_goat.png"
    zoom 1.5


image outdoor:
    "market.jpeg"
    zoom 1.5

image letter:
    "Love_letter_OG.png"
    zoom 2



image Waitress:
    "anna.png"
    zoom 2

image Waitress_Invert:
    "anna copy.png"
    zoom 2


    
image Bar_stanger:
    "Drunk.png"
    zoom 2.5
    
image Ride_offerer:
    "Ride_offerer2.png"
    zoom 2    




label start:
    play music "audio/BAR_SOUND .mp3" volume 0.25
    scene bar1
      
    
    "Welcome Traveler! Your adventure starts here."
    "*The bartender approach you*"
    show Waitress

    
    Waitress "Wut ye be havin today?"
    menu:
        "A: Pickled Sea Water":
            "Comin right up for YE!"
            $ drink = "Pickled Sea Water"
        "B: Elven Wine":
            "Excellent Choice!"
            $ drink = "Elven Wine"
        "C: Moon Juice":
            "that questionable ey, consider it done."
            $ drink = "Moon Juice"
        "D: nothing":
            "Ya wastin ye time aye!!"
            $ drink = ""
    show Waitress at offscreenright
    with ease
    "*The Bartender leaves*"
    pause 1.0

    show Bar_stanger 
    with moveinleft
    stranger "I haven't seen you before have I?"
    stranger "Are you a newcomer?"
    menu:
        "Yes":
            stranger "Welcome! you may call me Sir Sloshington McBlubberpants the Third"
            Bar_stanger"I'm a usual here at this fine establishment"
            Bar_stanger"What's your name?"
            jump name
        "No":
            stranger "Either im too drunk or you're just too ugly, I've never seen you before bucko"
            stranger "I am Sir Sloshington McBlubberpants the Third, and who might you be?"
            jump name

    label name: 
        while True:
            $ you = renpy.input("Enter your Name: ")
            if you == "":
                $ you = renpy.input("Please enter a name! ")
            else:
                jump title
        

    label title:
        you "I am [you], the..."
        menu:
            "Great Tax Collector!":
                Bar_stanger "I regret talking to you now.."
                Bar_stanger "Take me off your books would ya? I might pay for ya drink"
                menu:
                    "Perchance":
                        Bar_stanger "I never said that I would pay for your drink"
                        jump bar2
                    "Not a chance":
                        Bar_stanger "Well i'm broke one way or the other"
                        jump bar2
                    
            "Vermin catcher":
                Bar_stanger "I remember you!"
                Bar_stanger "You're that one guy who almost turned himself into a mice"
                Bar_stanger "MICE MANN!"
                menu:
                    "okay...":
                        Bar_stanger "HEHEHEHEHE"
                        jump bar2
                    "Excuse me...":
                        Bar_stanger "Im just poking your toes"
                        jump bar2
                    

            "Dung Catcher":
                Bar_stanger "Yikes..."
                jump bar2
    
        
       
    label bar2: 
        Bar_stanger "Newcomers like you don't stick around for too long, what's your plan [you]?"
        you "Well I was planning to head to..."
        $ Location = ["Serenity Sands", "Enchanted Grove", "Frostvale Peaks"]
        menu: 
            "Serenity Sands":
                Bar_stanger "Home of the traders and the most beautiful ladies"
                Bar_stanger "I happen uppon one myself!"
                Bar_stanger "Your MOM!"
                you "AYOOO!"
                $ Final_destination = "Serenity Sands"
                
        
            "Enchanted Grove":
                Bar_stanger "Place either gets you lost or poor"
                Bar_stanger "The place is filled with Scammers or dwarfs"
                Bar_stanger "I remember this one short GOOMBA"
                Bar_stanger "It was...."
                Bar_stanger "Your MOTHERR!!"
                you "AYOOO!"
                $ Final_destination = "Enchanted Grove"
                
            "Frostvale Peaks":
                Bar_stanger "The mysterious land that's filled with rare creatures"
                Bar_stanger "I encounter one special one myself"
                Bar_stanger "Your MOTHER!"
                you "AYOOO!"
                $ Final_destination = "Frostvale Peaks"
                

        show Bar_stanger at left
        with ease
        
        show Waitress_Invert with moveinright
        with ease
        if drink == "": 
            Waitress_Invert "Thiz fatso bothing you?"
        else:
            Waitress_Invert "Here ye [drink]"
            Waitress_Invert "Thiz fatso bothin ye?"
        show Waitress_Invert at right
        menu:
            "Yeah":
                Waitress_Invert "It's okay, he does the samething to everyone."
            "nope":
                Waitress_Invert "Just ignore the bozo"
        show Waitress_Invert at offscreenleft
        with ease
        pause 0.5
        show Bar_stanger at center
        with ease
        Bar_stanger "So back to where we were."
        Bar_stanger "Why are you heading to [Final_destination]?"
        menu: 
            "To visit your MOTHER":
                Bar_stanger "HAHAHAHAHAH, Jolly Good Show!"
                $ story_ending = 0
            "I place my phone somewhere and I couldn't find it":
                Bar_stanger "Intersting..."
                $ story_ending = 1 
        Bar_stanger "Looks like you have a long trip ahead of you"
        Bar_stanger "I'll let you be"
        Bar_stanger "Nice meeting you [you]!"
        show Bar_stanger at offscreenright
        with ease
        "*You finish your drink and leave the tavern*"
        jump outside


    


    label outside:
        scene outdoor with fade
        stop music
        play music "audio/town.mp3" volume 0.25
        "*As you ready to start your journey, someone approuches you*"
        show Ride_offerer
        with easeintop
        Ride_offerer "Ello Sir, I am in need of assistant"
        Ride_offerer "If you are to help me, I can offer you a ride on my speedy speedwagon"
        
        menu: 
        
            "Yes":
                Ride_offerer "splended Sir!"
                jump Ride_offerer_quest
            "No":
                Ride_offerer "I hope you get kicked by a dwarf wearing enchanted, jingle-toed boots!"
                show Ride_offerer at offscreenright
                with ease
                "*You leave town for [Final_destination]*"
                jump First_Destination_machine
                


    label Ride_offerer_quest:
        Ride_offerer "I am writing a love letter to thy beloved wife"
        Ride_offerer "It's been a while and I want to see if I still got the touch. *wink wink*"
        Ride_offerer "would you mind reading thy letter and say if it's good?"
        show letter
        "*read thy letter*"
        show letter at offscreenleft
        with ease
        menu:
            "Thy words are very exquisite!":
                Ride_offerer "Thank you good sirr"
            "Thy need some more feelings and less booties within thy letter":
                Ride_offerer "Hmmmm, I see."
        Ride_offerer "I shall keep thy promise and give a ride"
        Ride_offerer "Where are you heading?"

        menu: 
            "[Final_destination]":
                Ride_offerer "Thy can't go that far but thy will drop you off outside the town" 
        
        $ Location = ["Serenity Sands", "Enchanted Grove", "Frostvale Peaks"]
        $ Location.remove(Final_destination)
        $ First_Destination = renpy.random.choice(Location)
        $ Location.remove(First_Destination)
        if First_Destination == "Serenity Sands":
            "*After the ride out on the Speedy Speedwagon, you first arrive to the [First_Destination]*"
            scene desert with fade
            stop music
            jump Serenity_Sands
        elif First_Destination == "Enchanted Grove":
            "*After the ride out on the Speedy Speedwagon, you first arrive to the [First_Destination]*"
            scene forrest with fade
            stop music
            jump Enchanted_Grove
        elif First_Destination == "Frostvale Peaks":
            "*After the ride out on the Speedy Speedwagon, you first arrive to the [First_Destination]*"
            scene tundra with fade
            stop music
            jump Frostvale_Peaks
                
    label First_Destination_machine:
        $ Location = ["Serenity Sands", "Enchanted Grove", "Frostvale Peaks"]
        $ Location.remove(Final_destination)
        $ First_Destination = renpy.random.choice(Location)
        $ Location.remove(First_Destination)
        if First_Destination == "Serenity Sands":
            "*After town, you first arrive to the [First_Destination]*"
            scene desert with fade
            stop music
            jump Serenity_Sands
        elif First_Destination == "Enchanted Grove":
            "*After town, you first arrive to the [First_Destination]*"
            scene forrest with fade
            stop music
            jump Enchanted_Grove
        elif First_Destination == "Frostvale Peaks":
            "*After town, you first arrive to the [First_Destination]*"
            scene tundra with fade
            stop music
            jump Frostvale_Peaks

    label second_Destination_machine:
        $ second_Destination_machine = renpy.random.choice(Location)
        if second_Destination_machine == "Serenity Sands":
            "You would later arrive at the Serenity Sands"
            scene desert with fade
            stop music
            jump Serenity_Sands2
        elif second_Destination_machine == "Enchanted Grove":
            "You would later arrive at the Enchanted Grove"
            scene forrest with fade
            stop music
            jump Enchanted_Grove2
        elif second_Destination_machine == "Frostvale Peaks":
            "You would later arrive at the Frostvale Peaks"
            scene tundra with fade
            stop music
            jump Frostvale_Peaks2

    label last_destination: 
        if Final_destination == "Serenity Sands":
            scene desert with fade
            stop music
            jump Serenity_Sands3
        elif Final_destination == "Enchanted Grove":
            scene forrest with fade
            stop music
            jump Enchanted_Grove3
        elif Final_destination == "Frostvale Peaks":
            scene tundra with fade
            stop music
            jump Frostvale_Peaks3
        
    label ending:
        if story_ending == 0:
            jump ending0
        elif story_ending == 1:
            jump ending1


  
    label Serenity_Sands:
        play music "audio/Desert_music.mp3" volume 0.25 
        "Entering the desert is like stepping into an immense, sun-soaked tapestry of solitude and serenity."
        "You look around" 
        "The vast expanse of golden sands stretches out in every direction, seemingly endless and timeless."
        "You can't tell where you should go"
        "*Choose a direction*"
        menu:
            "North":
                "You travel North"
            "East":
                "You travel East" 
            "South":
                "You travel South"  
            "West":
                "You travel West"  
        "You see nothing"
        "You continue to wonder"
        "*Choose a direction*"
        menu:
            "North":
                "You travel North"
            "East":
                "You travel East" 
            "South":
                "You travel South"  
            "West":
                "You travel West"
        "You see nothing"
        "your body starting to feel weak"
        "*Choose a direction*"
        menu:
            "North":
                "You travel North"
            "East":
                "You travel East" 
            "South":
                "You travel South"  
            "West":
                "You travel West"
        "You passed out"
        "You feel your body being move"
        scene desert_village with fade
        "You wake up" 
        "You find yourself in a village"
        "A trader approuches you"
        show trader with moveinleft
        with ease
        Trader "You woke up!"
        Trader "I wonder into you after my fight with hot stinky beast"
        Trader "I almost died in that pooping hut!"
        Trader "How are you feeling?"
        menu:
            "I need to stop taking spontaneous naps in the desert!":
                Trader "Oh it was a nap was it! HAHAHAA"
            "Did anyone see that camel that ran me over?":
                Trader "I guess it was a hit and run then"
        Trader "Welcome to Dusty Chuckleville"
        Trader "Home of traders around the world"
        Trader "What got you here?"
        menu:
            "you did.....":
                Trader "I could've left you out there"
            "I am on a journey":
                Trader "Fascinating"
        Trader "Allow me to unveil the wonders of my wares!"
        Trader "It is most definitely top tier"
        Trader "I shall allow you to get one item for free"
        menu:
            "Pet Rock Training Manuals":
                Trader "Every pet rock deserves to learn a trick or two, right?"
                you "I will create the most talented rock in the world!"
            "Fog in a Can":
                Trader "Great for those days when you miss the mystery of not being able to see two feet in front of you"
                you "This will me my emergency food"
            "Invisible Ink Pens":
                Trader "Perfect for writing messages that even you won't be able to read"
                you "I guess this was the best option"
        Trader "before you go, remember to spread words of my wares"
        Trader "Until our path cross again stranger!"
        show trader at offscreenright
        with ease 
        "You continue with your journey"
        jump second_Destination_machine
         
        

    label Enchanted_Grove:
        play music "audio/Forrest_music.mp3" volume 0.25 
        "Entering a forest is like crossing a threshold into a living, breathing sanctuary of nature"
        "As you walk deeper into the forest, the canopy above forms a green cathedral, creating a sense of sacred space and quiet reflection."
        "You travel deeper into the woods"
        show forrest2 with fade
        "you see an extremely short man approaching you"
        show scammer with moveinright
        with ease
        Dwarf "HEY HEY HEY!"
        Dwarf "YOU JUST WON A PRIZED?!"
        menu:
            "Is it your mother?":
                Dwarf "Close but not close enough!"
            "REALLY!":
                Dwarf "Indeed good sir!"
        Dwarf "You have won a lifetime Supply of Rubber Chickens"
        Dwarf "All you have to do is pay a small fee!"
        menu:
            "*Kick Shorty McShortstuff*":
                "The dwarfs flew away"
                
            "*Continue to travel*":
                Dwarf "WHAT ABOUT YOUR LIFE SUPPLIES OF RUBBER CHICKENS?!?"
        show scammer at offscreenright
        with ease
        "You continue your journey"
        jump second_Destination_machine


    label Frostvale_Peaks:
        play music "audio/Tundra_music.mp3" volume 0.25 
        "You enter a vast and frozen dreamscape, a landscape where the world seems to hold its breath in icy stillness"
        "The ground beneath your feet is solid, frozen, and often covered in a blanket of powdery snow that crunches softly with each step"
        "You see two normal goat that coming closer to you"
        show goat_male at left
        show goat_female at right
        menu:
            "*Pet goat on the left*":
                show Angry_female at right
                Goat_right "GET YOUR BAAA-ing HANDS OFF MY HUSBAND!!!"
                show Angry_male at left
                Goat_left "YEAH DONT TOUCH ME"
                Goat_left "IM A MARRIED MAN"

            "*Pet goat on the right*":
                show Angry_male at left
                Goat_left "GET YOUR BAAA-ing HANDS OFF MY WIFE!!"
                show Angry_female at right
                Goat_right "YEAH DONT TOUCH ME"
                Goat_right "IM A MARRIED WOMAN"
        Goat_left "Dont go around touching people"
        Goat_right "You lucky I didn't press charges"
        show tundra2
        "You continue with your journey"
        jump second_Destination_machine

    
        
        
#"-------------------------------------------"

    label Serenity_Sands2:
        play music "audio/Desert_music.mp3" volume 0.25 
        "Entering the desert is like stepping into an immense, sun-soaked tapestry of solitude and serenity."
        "You look around" 
        "The vast expanse of golden sands stretches out in every direction, seemingly endless and timeless."
        "You can't tell where you should go"
        "*Choose a direction*"
        menu:
            "North":
                "You travel North"
            "East":
                "You travel East" 
            "South":
                "You travel South"  
            "West":
                "You travel West"  
        "You see nothing"
        "You continue to wonder"
        "*Choose a direction*"
        menu:
            "North":
                "You travel North"
            "East":
                "You travel East" 
            "South":
                "You travel South"  
            "West":
                "You travel West"
        "You see nothing"
        "your body starting to feel weak"
        "*Choose a direction*"
        menu:
            "North":
                "You travel North"
            "East":
                "You travel East" 
            "South":
                "You travel South"  
            "West":
                "You travel West"
        "You passed out"
        "You feel your body being move"
        scene desert_village with fade
        "You wake up" 
        "You find yourself in a village"
        "A trader approuches you"
        show trader with moveinleft
        with ease
        Trader "You woke up!"
        Trader "I wonder into you after my fight with hot stinky beast"
        Trader "I almost died in that pooping hut!"
        Trader "How are you feeling?"
        menu:
            "I need to stop taking spontaneous naps in the desert!":
                Trader "Oh it was a nap was it! HAHAHAA"
            "Did anyone see that camel that ran me over?":
                Trader "I guess it was a hit and run then"
        Trader "Welcome to Dusty Chuckleville"
        Trader "Home of traders around the world"
        Trader "What got you here?"
        menu:
            "you did.....":
                Trader "I could've left you out there"
            "I am on a journey":
                Trader "Fascinating"
        Trader "Allow me to unveil the wonders of my wares!"
        Trader "It is most definitely top tier"
        Trader "I shall allow you to get one item for free"
        menu:
            "Pet Rock Training Manuals":
                Trader "Every pet rock deserves to learn a trick or two, right?"
                you "I will create the most talented rock in the world!"
            "Fog in a Can":
                Trader "Great for those days when you miss the mystery of not being able to see two feet in front of you"
                you "This will me my emergency food"
            "Invisible Ink Pens":
                Trader "Perfect for writing messages that even you won't be able to read"
                you "I guess this was the best option"
        Trader "before you go, remember to spread words of my wares"
        Trader "Until our path cross again stranger!"
        show trader at offscreenright
        with ease 
        "You continue with your journey"
        jump last_destination
         
        

    label Enchanted_Grove2:
        play music "audio/Forrest_music.mp3" volume 0.25 
        "Entering a forest is like crossing a threshold into a living, breathing sanctuary of nature"
        "As you walk deeper into the forest, the canopy above forms a green cathedral, creating a sense of sacred space and quiet reflection."
        "You travel deeper into the woods"
        show forrest2 with fade
        "you see an extremely short man approaching you"
        show scammer with moveinright
        with ease
        Dwarf "HEY HEY HEY!"
        Dwarf "YOU JUST WON A PRIZED?!"
        menu:
            "Is it your mother?":
                Dwarf "Close but not close enough!"
            "REALLY!":
                Dwarf "Indeed good sir!"
        Dwarf "You have won a lifetime Supply of Rubber Chickens"
        Dwarf "All you have to do is pay a small fee!"
        menu:
            "*Kick Shorty McShortstuff*":
                "The dwarfs flew away"
                
            "*Continue to travel*":
                Dwarf "WHAT ABOUT YOUR LIFE SUPPLIES OF RUBBER CHICKENS?!?"
        show scammer at offscreenright
        with ease
        "You continue your journey"
        jump last_destination

    label Frostvale_Peaks2:
        play music "audio/Tundra_music.mp3" volume 0.25 
        "You enter a vast and frozen dreamscape, a landscape where the world seems to hold its breath in icy stillness"
        "The ground beneath your feet is solid, frozen, and often covered in a blanket of powdery snow that crunches softly with each step"
        "You see two normal goat that coming closer to you"
        show goat_male at left
        show goat_female at right
        menu:
            "*Pet goat on the left*":
                show Angry_female at right
                Goat_right "GET YOUR BAAA-ing HANDS OFF MY HUSBAND!!!"
                show Angry_male at left
                Goat_left "YEAH DONT TOUCH ME"
                Goat_left "IM A MARRIED MAN"

            "*Pet goat on the right*":
                show Angry_male at left
                Goat_left "GET YOUR BAAA-ing HANDS OFF MY WIFE!!"
                show Angry_female at right
                Goat_right "YEAH DONT TOUCH ME"
                Goat_right "IM A MARRIED WOMAN"
        Goat_left "Dont go around touching people"
        Goat_right "You lucky I didn't press charges"
        show tundra2
        "You continue with your journey"
        jump last_destination
        
#----------------------------------------------------

    label Serenity_Sands3:
        play music "audio/Desert_music.mp3" volume 0.25 
        "Entering the desert is like stepping into an immense, sun-soaked tapestry of solitude and serenity."
        "You look around" 
        "The vast expanse of golden sands stretches out in every direction, seemingly endless and timeless."
        "You can't tell where you should go"
        "*Choose a direction*"
        menu:
            "North":
                "You travel North"
            "East":
                "You travel East" 
            "South":
                "You travel South"  
            "West":
                "You travel West"  
        "You see nothing"
        "You continue to wonder"
        "*Choose a direction*"
        menu:
            "North":
                "You travel North"
            "East":
                "You travel East" 
            "South":
                "You travel South"  
            "West":
                "You travel West"
        "You see nothing"
        "your body starting to feel weak"
        "*Choose a direction*"
        menu:
            "North":
                "You travel North"
            "East":
                "You travel East" 
            "South":
                "You travel South"  
            "West":
                "You travel West"
        "You passed out"
        "You feel your body being move"
        scene desert_village with fade
        "You wake up" 
        "You find yourself in a village"
        "A trader approuches you"
        show trader with moveinleft
        with ease
        Trader "You woke up!"
        Trader "I wonder into you after my fight with hot stinky beast"
        Trader "I almost died in that pooping hut!"
        Trader "How are you feeling?"
        menu:
            "I need to stop taking spontaneous naps in the desert!":
                Trader "Oh it was a nap was it! HAHAHAA"
            "Did anyone see that camel that ran me over?":
                Trader "I guess it was a hit and run then"
        Trader "Welcome to Dusty Chuckleville"
        Trader "Home of traders around the world"
        Trader "What got you here?"
        menu:
            "you did.....":
                Trader "I could've left you out there"
            "I am on a journey":
                Trader "Fascinating"
        Trader "Allow me to unveil the wonders of my wares!"
        Trader "It is most definitely top tier"
        Trader "I shall allow you to get one item for free"
        menu:
            "Pet Rock Training Manuals":
                Trader "Every pet rock deserves to learn a trick or two, right?"
                you "I will create the most talented rock in the world!"
            "Fog in a Can":
                Trader "Great for those days when you miss the mystery of not being able to see two feet in front of you"
                you "This will me my emergency food"
            "Invisible Ink Pens":
                Trader "Perfect for writing messages that even you won't be able to read"
                you "I guess this was the best option"
        Trader "before you go, remember to spread words of my wares"
        Trader "Until our path cross again stranger!"
        show trader at offscreenright
        with ease 
        "You continue with your journey"
        jump ending
         
        

    label Enchanted_Grove3:
        play music "audio/Forrest_music.mp3" volume 0.25 
        "Entering a forest is like crossing a threshold into a living, breathing sanctuary of nature"
        "As you walk deeper into the forest, the canopy above forms a green cathedral, creating a sense of sacred space and quiet reflection."
        "You travel deeper into the woods"
        show forrest2 with fade
        "you see an extremely short man approaching you"
        show scammer with moveinright
        with ease
        Dwarf "HEY HEY HEY!"
        Dwarf "YOU JUST WON A PRIZED?!"
        menu:
            "Is it your mother?":
                Dwarf "Close but not close enough!"
            "REALLY!":
                Dwarf "Indeed good sir!"
        Dwarf "You have won a lifetime Supply of Rubber Chickens"
        Dwarf "All you have to do is pay a small fee!"
        menu:
            "*Kick Shorty McShortstuff*":
                "The dwarfs flew away"
    
            "*Continue to travel*":
                Dwarf "WHAT ABOUT YOUR LIFE SUPPLIES OF RUBBER CHICKENS?!?"
        show scammer at offscreenright
        with ease
        "You continue your journey"
        jump ending

    label Frostvale_Peaks3:
        play music "audio/Tundra_music.mp3" volume 0.25 
        "You enter a vast and frozen dreamscape, a landscape where the world seems to hold its breath in icy stillness"
        "The ground beneath your feet is solid, frozen, and often covered in a blanket of powdery snow that crunches softly with each step"
        "You see two normal goat that coming closer to you"
        show goat_male at left
        show goat_female at right
        menu:
            "*Pet goat on the left*":
                show Angry_female at right
                Goat_right "GET YOUR BAAA-ing HANDS OFF MY HUSBAND!!!"
                show Angry_male at left
                Goat_left "YEAH DONT TOUCH ME"
                Goat_left "IM A MARRIED MAN"

            "*Pet goat on the right*":
                show Angry_male at left
                Goat_left "GET YOUR BAAA-ing HANDS OFF MY WIFE!!"
                show Angry_female at right
                Goat_right "YEAH DONT TOUCH ME"
                Goat_right "IM A MARRIED WOMAN"
        Goat_left "Dont go around touching people"
        Goat_right "You lucky I didn't press charges"
        show tundra2
        "You continue with your journey"
        jump ending
#-------------------------------------------------

    label ending0:
        "You have reach the end of your journey"
        "you become dispointed"
        "You never found Sir Sloshington McBlubberpants the Third's mother"
        "FIN"
        return
    label ending1:
        "After all of that traveling"
        "you still couldn't find your phone..."
        "you reach in your pockets and felt something"
        "It was your phone"
        "THE END"
        return

return 


        



#[desert/Serenity Sands- kingdom/trader, forrest/Enchanted Grove- thief/scammer, swamp/moss wood- , tundra]
    
    
   


    


