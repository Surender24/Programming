import random
emojies = {'r':'🥌','p':'📃','s':'✂'}
choices = ('r','p','s')
while True:
    user_choice = input("Enter your choice rock,paper or scissors?(r/p/s): ").lower()
    if user_choice not in choices:
        print("Inavlid choice")
        continue
    computer_choice = random.choice(choices)
    print("You chose ",emojies[user_choice])
    print("Computer chose ",emojies[computer_choice])

    if ((user_choice=='r'and computer_choice=='s') or 
        (user_choice=='s' and computer_choice=='p')or
        (user_choice=='p' and computer_choice=='r')):
        print("You win")
    elif (user_choice==computer_choice):
        print("Tie")
    else:
        print("You lose")

    you_continue = input("Continue? (y/n): ").lower()
    if(you_continue=='n'):
        print("Thanks for playing!")
        break
    
        


