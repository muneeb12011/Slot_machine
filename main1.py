import random

# Define slot symbols
symbols = ["🍒", "🍋", "🍉", "🍇", "🔔", "💎", "⭐"]

# Define the payout multipliers for 3 matching symbols
payouts = {
    "🍒": 10,
    "🍋": 5,
    "🍉": 8,
    "🍇": 4,
    "🔔": 15,
    "💎": 20,
    "⭐": 25
}

# Function to spin the slot machine
def spin():
    return [random.choice(symbols) for _ in range(3)]

# Function to check if the player wins
def check_win(spin_result):
    if spin_result[0] == spin_result[1] == spin_result[2]:
        return payouts[spin_result[0]]
    return 0

# Game loop
def play_slot_machine():
    try:
        balance = int(input("Enter your starting balance: "))  # Allow user to input starting balance
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    spin_cost = 10  # Cost per spin
    
    print(f"Your starting balance is: ${balance}")
    
    while balance >= spin_cost:
        play = input("\nPress enter to spin the reels or type 'quit' to exit: ")
        if play.lower() == 'quit':
            break
        
        balance -= spin_cost
        result = spin()
        print(f"Reels: {' | '.join(result)}")
        
        winnings = check_win(result)
        if winnings > 0:
            print(f"Congratulations! You won ${winnings * spin_cost}!")
            balance += winnings * spin_cost
        else:
            print("Better luck next time!")
        
        print(f"Current balance: ${balance}")
    
    print("Game over! Your final balance is: ${}".format(balance))

# Run the game
play_slot_machine()

