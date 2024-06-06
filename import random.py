import random

#defining the maximum number of lines and the maximum and minimum bet
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#defining the number of rows and columns
ROWS = 3
COLS = 3

#defining the symbols and their counts
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

#defining the values of the symbols
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#function to check the winnings
def check_winnings(columns, lines,bet,values):
    # initializing winnings to 0
    winnings = 0
    winning_lines = []
    # looping through the number of lines we have
    for line in range(lines):
        # getting the symbol of the first column at the current line
        symbol = columns[0][line]
        # looping through the number of columns we have
        for column in columns:
            # getting the symbol of the current column at the current line
            symbol_to_check = column[line]
            # checking if the symbol is not equal to the symbol to check
            if symbol != symbol_to_check:
                # if the symbols are not equal, break the loop
                break
                # if the symbols are equal, calculate the winnings
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        # _ universal python variable name for unused variables
        for _ in range(symbol_count):
            all_symbols.append(symbol)
      #defining column list
    columns = []
    #generate column for every single column we have
    for _ in range(cols):
        #picking random values for each row in our column
        column = []
        current_symbols = all_symbols[:]
        #looping through the number of values we need to generate, which is the number of rows
        for _ in range(rows):
            #picking a random value from the current symbols list
            value = random.choice(current_symbols)
            #removing the value from the current symbols list, so we cant pick it again
            current_symbols.remove(value)
            #adding the value to the column
            column.append(value)

        #adding the column to the columns list
        columns.append(column)
    return columns

#function to print the slot machine
def print_slot_machine(columns):
    #looping through the number of rows we have
    for row in range(len(columns[0])):
        #looping through the number of columns we have
        for i, column in enumerate(columns):
            #printing the value of the column at the current row
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()




#function for user to deposit money into virtual slot machine
def deposit():
    #infinite loop that breaks until the user enters a valid amount
    while True:
        amount = input("What would you like to deposit? $")
        #checking if the amount entered is a digit
        if amount.isdigit():
            amount = int(amount)
            #if amount is greater than 0, break the loop
            if amount > 0:
                break
            #if amount is less than or equal to 0, print an error message
            else:
                print("Please enter a valid monetary amount greater than $0.")
        #if the amount is not a digit, print an error message
        else:
            print("Please enter a valid monetary amount.")
    return amount

#function to get the number of lines the user wants to bet on
def get_number_of_lines():
    # infinite loop that breaks until the user enters a valid number of lines
    while True:
        lines = input("Enter the number of lines you would like to bet on (1-" + str(MAX_LINES) + ")? ")
        #checking if the number of lines entered is a digit
        if lines.isdigit():
            lines = int(lines)
            #if the number of lines is between 1 and the maximum number of lines, break the loop
            if 1 <= lines <= MAX_LINES:
                break
                #if the number of lines is not between 1 and the maximum number of lines, print an error message
            else:
                print("Please enter a valid number of lines.")
                #if the number of lines is not a digit, print an error message
        else:
            print("Please enter a number.")
    return lines

#function to get the amount the user wants to bet
def get_bet():
    # infinite loop that breaks until the user enters a valid amount
    while True:
        amount = input("What would you like to bet on each line? $")
        #checking if the amount entered is a digit
        if amount.isdigit():
            amount = int(amount)
            #if the amount is between the minimum and maximum bet, break the loop
            if MIN_BET <= amount <= MAX_BET:
                break
                #if the amount is not between the minimum and maximum bet, print an error message
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
                #if the amount is not a digit, print an error message
        else:
            print("Please enter a valid monetary amount.")
    return amount

def spin(balance):
    #initializing get_number_of_line function
    lines = get_number_of_lines()
    #infinite loop that breaks when the total bet is less than or equal to the balance
    while True:
        #initializing get_bet function
        bet = get_bet()
        #calculating the total bet
        total_bet = lines * bet

        #if the total bet is greater than the balance, print an error message
        if total_bet > balance:
            print(f"You do not have enough funds to make this bet, your current balance is: ${balance}")
        #if the total bet is less than or equal to the balance, break the loop
        else:
            break
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

    #initializing get_slot_machine_spin function
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

#main function of program
def main():
    #initializing deposit function
    balance = deposit()
    while True:
        print(f"Your current balance is: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


#initializing the main function of the program
main()