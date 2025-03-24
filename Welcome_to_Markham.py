# Welcome to Markham
# Author: Kishan Patel
# Date: Thursday, October 10th, 2024


def adventure():
   print("WELCOME TO THE MARKHAM.")
   print("You find yourself in a Cornell Rouge Woods Park in Markham. You have two choices.")
   choice1 = input("Would you like to go 'left' towards the dark cave or 'right' towards the river? ").lower()


   if choice1 == 'left':
       # Room 2
       print("\nYou approach the dark cave and hear strange noises coming from inside.")
       choice2 = input("Would you like to 'enter' the cave or 'walk away'? ").lower()


       if choice2 == 'enter':
           # Room 3
           print("\nYou enter the cave and see two paths.")
           choice3 = input("Do you take the 'narrow path' or the 'wide path'? ").lower()


           if choice3 == 'narrow path':
               # Room 4
               print("\nThe narrow path has a wet floor and leads to a dead end.")
               choice4 = input("Do you 'turn back' or 'climb the wall'? ").lower()


               if choice4 == 'turn back':
                   # Ending 1
                   print("\nYou safely return to the entrance. You win!")
               elif choice4 == 'climb the wall':
                   # Ending 2
                   print("\nYou slip on baby oil and P. Diddy found you. Game over!")
               else:
                   print("\nInvalid choice. Game over.")


           elif choice3 == 'wide path':
               # Room 5
               print("\nThe wide path leads to a dark room with a note.")
               choice4 = input("Do you 'check the note' or 'leave it alone'? ").lower()


               if choice4 == 'check the note':
                   # Ending 3
                   print("\nThe note gives you a way to avoid taxes LEGALY. No more taxes!")
               elif choice4 == 'leave it alone':
                   # Ending 4
                   print("\nYou walk away safely but empty-handed. You win!")
               else:
                   print("\nInvalid choice. Game over.")


           else:
               print("\nInvalid choice. Game over.")


       elif choice2 == 'walk away':
           # Room 6
           print("\nYou decide it's best not to risk it and walk away.")
           choice3 = input("Do you 'climb a tree' to get a better view or 'follow a path'? ").lower()


           if choice3 == 'climb a tree':
               # Room 7
               print("\nYou climb a tree and spot a house in the distance.")
               choice4 = input("Do you 'head to the house' or 'stay in the forest'? ").lower()


               if choice4 == 'head to the house':
                   # Ending 5
                   print("\nYou reach the house safely. You win!")
               elif choice4 == 'stay in the forest':
                   # Ending 6
                   print("\nDiddy found you. Game over!")
               else:
                   print("\nInvalid choice. Game over.")


           elif choice3 == 'follow a path':
               # Room 8
               print("\nYou follow a path and find the rapper Lucki.")
               choice4 = input("Do you 'hug Lucki' or 'ignore him'? ").lower()


               if choice4 == 'hug Lucki':
                   # Ending 7
                   print("\nYou hug Lucki and he leads you to a secret cave. You win!")
               elif choice4 == 'ignore him':
                   # Ending 8
                   print("\nLucki is sad you ignored him and eats you. You loose!")
               else:
                   print("\nInvalid choice. Game over.")


           else:
               print("\nInvalid choice. Game over.")


   elif choice1 == 'right':
       # Room 9
       print("\nYou walk towards the river and see a boat and a bridge.")
       choice2 = input("Would you like to 'take the boat' or 'cross the bridge'? ").lower()


       if choice2 == 'take the boat':
           # Room 10
           print("\nYou start rowing the boat, but a storm approaches.")
           choice3 = input("Do you 'keep rowing' or 'return to shore'? ").lower()


           if choice3 == 'keep rowing':
               # Room 11
               print("\nYou brave the storm and make it to the other side safely.")
               choice4 = input("Do you 'explore the island' or 'set up camp'? ").lower()


               if choice4 == 'explore the island':
                   # Ending 9
                   print("\nYou discover ancient ruins. You win!")
               elif choice4 == 'set up camp':
                   # Ending 10
                   print("\nYou set up camp and survive the night. You win!")
               else:
                   print("\nInvalid choice. Game over.")


           elif choice3 == 'return to shore':
               # Room 12
               print("\nYou return to shore, but a goose chases you.")
               choice4 = input("Do you 'climb a tree' or 'run'? ").lower()


               if choice4 == 'climb a tree':
                   # Ending 11
                   print("\nYou manage to escape the goose. You win!")
               elif choice4 == 'run':
                   # Ending 12
                   print("\nThe goose catches you. Game over!")
               else:
                   print("\nInvalid choice. Game over.")


           else:
               print("\nInvalid choice. Game over.")


       elif choice2 == 'cross the bridge':
           # Room 13
           print("\nYou cross the bridge and find Babytron also known as James Johnson IV.")
           choice3 = input("Do you 'talk' to Babyron or 'ignore' him? ").lower()


           if choice3 == 'talk':
               # Room 14
               print("\nBabytron offers you a choice of two drinks.")
               choice4 = input("Do you take the 'coca cola' or the 'sprite'? ").lower()


               if choice4 == 'coca cola':
                   # Ending 13
                   print("\nThe coca cola gives you super strength. You win!")
               elif choice4 == 'sprite':
                   # Ending 14
                   print("\nThe sprite turns you invisible. You win!")
               else:
                   print("\nInvalid choice. Game over.")


           elif choice3 == 'ignore':
               # Room 15
               print("\nBabytron gets offended and gets your credit card information.")
               choice4 = input("Do you 'apologize' or 'fight him'? ").lower()


               if choice4 == 'apologize':
                   # Ending 15
                   print("\nBabytron decides not to scam you. You win!")
               elif choice4 == 'fight him':
                   # Ending 16
                   print("\nYou try to fight him but his cartier glasses have lasers and burn you. Game over!")
               else:
                   print("\nInvalid choice. Game over.")


           else:
               print("\nInvalid choice. Game over.")


   else:
       print("\nInvalid choice. Game over.")


# Start the game
adventure()



