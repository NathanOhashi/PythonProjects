# From project: https://www.youtube.com/watch?v=th4OBktqK1I
# User will input() money that will go into a balance[]
# User will bet on lines and will be determined if they won
# If they win: bet * value of line and add to balance
# User can cash out or run out of money

# Import modules
import random

# Global constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# How many symbols are there? How many in each column?
# Dictionary of symbols
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = { # multiplier value
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# Randomly pick number of rows inside of each column
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # .items gives you key and value from dict
        for i in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:] # using slice makes a copy of list instead of using all_symbols[], or all_symbols.copy()
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

# Deposits an amount of money into your balance
# While loop checks if input() is a number and greater than 0
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

# Transpose rows into columns
# Number of rows = number of elements in each column
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1: 
                # len(columns) - 1 is the maximum index to access in the columns list
                print(column[row],end=" | ")
            else:
                print(column[row], end="")
        print()

# Gets number of lines to bet on from the user
# While loop checks if input is a number and makes sure it is between 1 and MAX_LINES
def get_number_of_lines():
    while True:
        lines = input("Enter the amount of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

# Gets the bet amount from the user between MIN_BET and MAX_BET
# print(f"str") lets you put any variable in {} to auto convert into str() if possible
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough funds. Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines) # splat/unpack operator passes every line from winning_lines

    return winnings - total_bet # tells you how much you won or lost form this spin

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == 'q':
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()