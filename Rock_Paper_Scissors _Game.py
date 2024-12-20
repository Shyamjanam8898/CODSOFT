import random

def get_user_choice():    # Get the user's choice
    print("Choose one: Rock, Paper, or Scissors")
    user_choice=input().lower()
    while user_choice not in ["rock","paper","scissors"]:
        print("Invalid choice. Please choose  any one of Rock, Paper, or Scissors.")
        user_choice=input().lower()
    return user_choice

def get_computer_choice():    # Get a random choice form the computer
    return random.choice(["rock","paper","scissors"])

def winner(user_choice,computer_choice):    # Determine the winner based on the choices
    if user_choice==computer_choice:
        return ("It is a tie!")
    elif (user_choice=="rock" and computer_choice=="scissors"):
        return ("You win!")
    elif (user_choice=="paper" and computer_choice=="rock"):
        return ("You win!")
    elif(user_choice=="scissors" and computer_choice=="paper"):
        return ("You win!")
    else:
        return ("Computer wins!")
def main():
    won=0
    tie=0
    lose=0
    print("Welcome to Rock, Paper, Scissors Game!")
    
    while True:
        user_choice=get_user_choice()
        computer_choice=get_computer_choice()
        
        print(f"\nYour choice:{user_choice}")
        print(f"Computer choice:{computer_choice}\n")
        
        result=winner(user_choice,computer_choice)
        print(result)
        if result=="You win!":
            won+=1
        elif result=="Computer wins!":
            lose+=1
        else:
            tie+=1
        play_again = input("\nDo you want to play again? (y/n): ").lower()        # Asking to the user if they want to play again
        if play_again=="y":
            pass
        elif play_again=="n":
            print("Thanks for playing!")
            print(f"Your Score: \n Won: {won} \t lose: {lose} \t tie: {tie}")
            break
        else:
            print("Invalid Input")
            print(f"Your Score: \n Won: {won} \t lose: {lose} \t tie: {tie}")
            break

if __name__ == "__main__":
    main()

