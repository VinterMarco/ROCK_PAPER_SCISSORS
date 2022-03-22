import random

rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
 
'''

scissors = '''

    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.

'''

paper = '''

          _____________
         |DAILY PROPHET|
         |&&& =========|
         |=== =========|
         |=== == %%$ ==|
         |[_] =========|
         |=== ===!##===|
         |_____________|
'''
game_images = [rock, paper, scissors]

user_input = int(input("Enter your choice:\n 0 - rock\n 1 - paper\n 2 - scissors\n Choice: "))
if user_input >= 3 or user_input < 0:
    print("You picked an invalid number.You lose!")

else:

    print('Player chose:')
    print(game_images[user_input])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_input == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_input == 2:
        print("You lose")
    elif computer_choice > user_input:
        print(" You lose!")
    elif user_input > computer_choice:
        print("You win!")

    elif computer_choice == computer_choice:
        print("It's a tie")
