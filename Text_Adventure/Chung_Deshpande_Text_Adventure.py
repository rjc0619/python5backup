import time
'''Introduction to Game'''

print 'Welcome to the Jungle!'
time.sleep(2)
print'Oh no! The emerald stone has been taken by the Jaguars, an evil group of'
time.sleep(2)
print'thieves. The stone holds the power of the almighty jungle and if you have'
time.sleep(2)
print'possession of the emerald, then you will hold the power of the jungle. You'
time.sleep(2)
print'are able to control the animals in the jungle as well as the plants. While'
time.sleep(2)
print'you are on your journey through the jungle, make sure to be aware of normal'
time.sleep(2)
print'objects that can be in disguise and then pop out of nowhere. So make sure'
time.sleep(2)
print'to be aware of what the almighty jungle has to bring to you. Get ready for'
time.sleep(2)
print'the challenge!'
time.sleep(2)
'''Characters'''

# CHARACTER CHOOSING
print 'Which character would you like to choose?'
time.sleep(2)
print '~ 1. Ruby Roundhouse ~'
print '~ 2. Dr. Smolder Bravestone ~'
print '~ 3. Franklin Finbar ~'
print '~ 4. Professor Shelly Oberon ~'
time.sleep(2)
print 'PICK A CHARACTER USING THE NUMBER'

'''NO PARAMETERS. THIS FUNCTION IS FOR DISPLAYING THE STRENGTHS AND WEAKNESSES
OF WHICHEVER CHARACTER THE PLAYER HAS CHOOSEN.'''
def character():
    a = raw_input('Do you choose character 1, 2, 3, or 4? ')
    if a == '1':
        print 'Ruby Roundhouse'
        time.sleep(2)
        print ' Strengths:'
        print '  -Karate'
        print "  -T'ai Chi"
        print '  -Aikido'
        print '  -Dance Fighting'
        time.sleep(2)
        print ' Weaknesses:'
        print '  -Venom'
        time.sleep(2)
    elif a == '2':
        print 'Dr. Smolder Bravestone'
        time.sleep(2)
        print ' Strengths:'
        print ' -Fearless'
        print ' -Climbing'
        print ' -Speed'
        print ' -Boomerang'
        print ' -Smoldering Intensity'
        time.sleep(2)
        print ' Weaknesses:'
        print '  NONE'
        time.sleep(2)
    elif a == '3':
        print 'Franklin Finbar' 
        time.sleep(2)
        print ' Strengths:'
        print ' -Zoology'
        print ' -Weapons Valet'
        time.sleep(2)
        print ' Weaknesses'
        print ' -Cake'
        print ' -Speed'
        print ' -Strength'
        time.sleep(2)
    elif a == '4':
        print 'Professor Shelly Oberon'
        time.sleep(2)
        print ' Strengths:'
        print ' -Cartography'
        print ' -Archaeology'
        print ' -Paleontology'
        time.sleep(1.5)
        print ' Weaknesses:'
        print ' -Endurance'
        time.sleep(2)
    else:
        print 'NOT A VALID ANSWER'
    print 'You are now ready to start your JOURNEY THROUGH THE JUNGLE!'
character()

'''NO PARAMETERS. THIS FUNCTION IS PRIMARILY FOR THE METHOD OF TRANSPORTATION.
IT CONTINUES TO SERVE THE PURPOSE OF WEAPONS, HUNTING, AND OTHER FACTOR(S)
NEEDED TO WIN THE GAME.'''
def transportation():
    time.sleep(2)
    print'The almighty jungle is only for the brave. So make sure you can find the'
    time.sleep(2)
    print'emerald stone. Please make sure to choose wisely!'
    time.sleep(2)
    b = raw_input('Which method of transportation would you like? Car or Boat? ')
    
# CAR CODE:    
    if b == 'Car' or b =='car':

# WEAPONS CHOOSING(CAR)
        print'It is now time for you to choose a weapon. If you'
        time.sleep(2)
        print'choose the gun then you will be able to easily kill off the enemies'
        time.sleep(2)
        print'at close range but if you choose the bow and arrow it will be easier'
        time.sleep(2)
        print'to kill enemies from a farther range. Be sure to choose wisely!'
        time.sleep(2)
        e = raw_input('Which weapon would you like? Gun or bow and arrow? ')
        if e == 'Gun' or e =='gun':
            print 'Nice choice with the gun!'
            time.sleep(2)
            print 'Enjoy the jungle in your car. You are now on the road. '
            time.sleep(2)
        elif e == 'bow and arrow' or e == 'bow' or e == 'Bow and Arrow':
            print 'Good going with the bow and arrow!'
            time.sleep(2)
            print 'Enjoy the jungle in your car! You are now on the road. '
            time.sleep(2)
        else:
            print 'NOT A VALID ANSWER'
            
    # EAT OR STAY IN CAR?        
        print'Looks like you are feeling hungry, you are surounded by plenty of food'
        time.sleep(2)
        print'but you don\'t know if it is safe to get off your vehicle and hunt.'
        time.sleep(2)
        print'Choose wisely!'
        time.sleep(2)
        c =  raw_input('Do you want to continue in your car or would you like \
to hunt for some food? ')
        if c == 'hunt':
           print 'Oh look! There\'s a deer '
           time.sleep(2)
        elif c == 'continue' or c == 'continue in your car':
            print 'Seems like you are in love with this jungle!'
            time.sleep(2)
        else:
            print 'NOT A VALID ANSWER'
        print'You have been on your journey for a while now, but looks like'
        time.sleep(2)
        print'we\'ve hit a crossroad! What direction are you planing on going now!'   
        time.sleep(2)
        g = raw_input('Would you like to make a Left or Right?' )
        
    # LEFT OR RIGHT? DIE AT LEFT, SURVIVE AT RIGHT(CAR)        
        if g == 'Left' or g == 'left':
            print 'GAME OVER, POISONOUS BATS SEEMED TO HAVE KILLED YOU!'
            time.sleep(2)
        elif  g == 'Right' or g == 'right':
            print 'Good Going! Looks like it is time to take a break!'
            time.sleep(2)
            print 'The JAGUARS. Ahhhhh! The leader of the jaguars has been tracing'
            time.sleep(2)
            print 'your steps! Although the glow of the stone is revealing its location,'
            time.sleep(2)
            print 'it is near impossible to retrieve it. It is in the leader\'s fanny'
            time.sleep(2)
            print 'pack!'
            time.sleep(2)
            
        # EMERALD VS. JAGUAR 'SCENE' 
            time.sleep(4)
            print'Oh no! Looks like your weapon has broken but your'
            time.sleep(2)
            print 'last shot seem to have distracted the leader.'
            j = raw_input('Would you like to fight anyways or grab at the fanny pack?')
            if j == 'grab at the fanny pack' or j == 'grab':
                print 'You run in to grab the emerald but right as to are in reach'
                time.sleep(2)
                print 'the leader turns around an punches you backwards. You won\'t'
                time.sleep(2)
                print 'give up so you get right back up and then you charge for '
                time.sleep(2)
                print 'the fanny pack. This time you are able to grip onto the fanny'
                time.sleep(2)
                print 'pack and push the leader down. You have the emerald and now'
                time.sleep(2)
                print 'the power of the jungle is in good hands. Make sure to keep'
                time.sleep(2)
                print 'this stone safe!'
                time.sleep(3.5) 
                print 'YOU HAVE WON!:)'
            elif j == 'fight':
                print 'You run up to the Leader and decide to give him a punch but'
                time.sleep(2)
                print 'the leader cathcs you hand and breaks it. And just as he is'
                time.sleep(2)
                print 'about to crush your face with his foot you roll over and'
                time.sleep(2)
                print 'avoid the leader crushing your face. You get back up and'
                time.sleep(2)
                print 'then go for another swing to his face. Once again the leader'
                time.sleep(2)
                print 'catches your hand but this time he throws you into the air.'
                time.sleep(2)
                print 'The jaguar leader seems to have been to strong for you.'
                time.sleep(2)
                print 'Causing your unfortunate death. GAME OVER!'
        else:
            print 'NOT A VALID ANSWER'

# BOAT CODE:   
    elif b == 'Boat' or b == 'boat':

    # WEAPONS CHOOSING(BOAT)  
        print'It is now time for you to choose a weapon if your choice. If you'
        time.sleep(2)
        print'choose the spear then you will be able to easily kill off the enemies'
        time.sleep(2)
        print'by throwing. But if you choose the bow and arrow it will be easier'
        time.sleep(2)
        print'to kill enemies from a farther range. Make sure to choose wisely!'
        time.sleep(2)
        f = raw_input('Which weapon would you like? Spear or bow and arrow? ')
        if f == 'Spear' or f == 'spear':
            print 'Nice choice with the spear!'
            time.sleep(2)
            print 'Enjoy the jungle in your boat. You are now in the river.'
            time.sleep(2)
        elif f == 'bow and arrow' or f == 'bow' or f == 'Bow and Arrow':
            print 'Good going with the bow and arrow!'
            time.sleep(2)
            print 'Enjoy the jungle in your boat. You are now in the river. '
            time.sleep(2)
        else:
                print 'NOT A VALID ANSWER'

    # EAT OR STAY IN BOAT?
        print'Looks like you are feeling hungry, you\'re surounded by plenty of food'
        time.sleep(2)
        print'but you don\'t know if it is safe to stop your boat and start fishing.'
        time.sleep(2)
        print'Choose wisely!'
        time.sleep(2)
        d = raw_input('Do you want to continue in your boat or would you like some fish? ')
        if d == 'fish' or d == 'Fish':
            print "Nice choice! I see a fish there, let's catch it! "
            time.sleep(2)
        elif d == 'continue' or d == 'continue in boat':
            print 'Seems like you are in love with this jungle!'
            time.sleep(2)
        else:
                print 'NOT A VALID ANSWER'
        print'You have been on your journey for a while now. Oh no! Looks like'
        time.sleep(2)
        print'the river is splitting! What direction are you planing on going now!'   
        time.sleep(2)        
        h = raw_input(' Would you like to row Left or Right?')
        
    # LEFT OR RIGHT? SURVIVE AT LEFT, DIE AT RIGHT(BOAT)          
        if h == 'left' or h == 'Left':
            print 'You take the left in the river and you noticed that you missed'
            time.sleep(2)
            print 'the waterfall! Good choice! Now you may continue on your'
            time.sleep(2)
            print 'journey to the emerald stone.'
            time.sleep(2)
            
        # EMERALD VS. JAGUAR 'SCENE'                  
            print 'It is now that time, to win the stone, you must fight its keepers.'
            time.sleep(2)
            print 'The JAGUARS. Ahhhhh! The leader of the jaguars has been tracing'
            time.sleep(2)
            print 'your steps! Although the glow of the stone is revealing its location,'
            time.sleep(2)
            print 'it is near impossible to retrieve it. It is in the leader\'s fanny'
            time.sleep(2)
            print 'pack!'
            time.sleep(4)
            print'Oh no! Looks like your weapon has broken, but your'
            time.sleep(2)
            print 'last shot seem to have distracted the leader.'
            j = raw_input('Would you like to fight anyways or grab at the fanny pack?')
            if j == 'grab at the fanny pack' or j == 'grab':
                print 'You run in to grab the emerald but right as to are in reach'
                time.sleep(2)
                print 'the leader turns around an punches you backwards. You won\'t'
                time.sleep(2)
                print 'give up so you get right back up and then you charge for '
                time.sleep(2)
                print 'the fanny pack. This time you are able to grip onto the fanny'
                time.sleep(2)
                print 'pack and push the leader down. You have the emerald and now'
                time.sleep(2)
                print 'the power of the jungle is in good hands. Make sure to keep'
                time.sleep(2)
                print 'this stone safe!'
                time.sleep(3.5) 
                print 'YOU HAVE WON!:)'
            elif j == 'fight':
                print 'You run up to the Leader and decide to give him a punch but'
                time.sleep(2)
                print 'the leader cathcs you hand and breaks it. And just as he is'
                time.sleep(2)
                print 'about to crush your face with his foot you roll over and'
                time.sleep(2)
                print 'avoid the leader crushing your face. You get back up and'
                time.sleep(2)
                print 'then go for another swing to his face. Once again the leader'
                time.sleep(2)
                print 'catches your hand but this time he throws you into the air.'
                time.sleep(2)
                print 'The jaguar leader seems to have been to strong for you.'
                time.sleep(2)
                print 'Causing your unfortunate death. GAME OVER!'
        elif h == 'Right' or h == 'right':
            print 'You take the right in the river and you seem to be reaching'
            time.sleep(2)
            print 'the end of the river but at the end of the river is a waterfall!'
            time.sleep(2)
            print 'The current is too stong and you can\'t make it to shore safely!'
            time.sleep(2)
            print 'Nor can you change the direction of the boat. You reach the edge'
            time.sleep(2)
            print 'of the river and fall to your death. GAME OVER!'
            time.sleep(2)
    else:
        print 'NOT A VALID ANSWER'

transportation()