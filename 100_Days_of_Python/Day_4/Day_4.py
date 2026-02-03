import  random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
rock_num = 0

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
paper_num = 1

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
scissors_num = 2

question1 = "What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"

def play_hand(num):
    if num == 0:
        print(rock)
    elif num == 1:
        print(paper)
    elif num == 2:
        print(scissors)

def decide_winner(player_num, computer_num):
    if player_num == computer_num:
        print("It's a Draw.")
    elif (player_num == rock_num and computer_num == scissors_num) or (player_num == paper_num and computer_num == rock_num) or (player_num == scissors_num and computer_num == paper_num):
        print("You Win!")
    else:
        print("You Lose!")

decision = int(input(question1))
if decision == 0 or decision == 1 or decision == 2:
    play_hand(decision)
    cpu_decision = random.randint(0, 2)
    print("Computer chose:")
    play_hand(cpu_decision)
    decide_winner(decision, cpu_decision)
else:
    print("Invalid Input")

