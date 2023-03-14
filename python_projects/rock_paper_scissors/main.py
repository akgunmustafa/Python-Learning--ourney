import random

player1 = input("Select Rock, Paper or Scissor : ").lower()
player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("Cumputer : "+player2)

if player1 == "rock" and player2 == "paper":
    print("Computer Won")
elif player1 == "paper" and player2 == "scissor":
    print("Computer Won")
elif player1 == "scissor" and player2 == "rock":
    print("Computer Won")
elif player1 == player2:
    print("Tie")
else:
    print("Human Won")

print("\n The computer's selects are random.")