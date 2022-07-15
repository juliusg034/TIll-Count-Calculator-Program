coins = float(input("Enter amount in coins: "))
ones = float(input("Enter amount in ones: "))
fives = float(input("Enter amount in fives: "))
tens = float(input("Enter amount in tens: "))
twenties = float(input("Enter amount in twenties: "))
fifties = float(input("Enter amount in fifties: "))
hundreds = float(input("Enter amount in hundreds: "))

# Calculate the amount of bills
amount_of_fives = fives / 5
amount_of_tens = tens / 10
amount_of_twenties = twenties / 20
amount_of_fifties = fifties / 50
amount_of_hundreds = hundreds / 100
amount_of_ones = ones / 1

# Calculate total amount in till
total = coins + ones + fives + tens + twenties + fifties + hundreds

print(f'\nYou have a total of ${total}')

# If there is less than 300, there is no deposit
if total > 300:
    # Calculate the deposit
    deposit = total - 300
    ending_deposit = deposit
    print(f'\nYou have to deposit ${deposit}')

    # My logic: I have already calculated the amount of hundreds I have. If I don't have
    # any hundreds in the till. Then, no further computation is needed
    if amount_of_hundreds > 0:
        
        # Calculate the max number of hundred dollar bills possible with the deposit using modulo operator
        max_hundreds = ending_deposit // 100
        
        # I can't deposit more bills than I have so if the max number of hundred dollar bills is larger than 
        # actual amount of hundred dollar bills then use that to subtract that from the remaining deposit
        if max_hundreds > amount_of_hundreds:
            print(f'Deposit {amount_of_hundreds} hundreds')
            ending_deposit = ending_deposit - (100 * amount_of_hundreds)
        # However, if the max is less than the actualy amount then use that to subtract from the remaining amount    
        else:
            ending_deposit = ending_deposit - (100 * max_hundreds)
            
            # Let the user know how many hundred dollar bills to deposit
            print(f'Deposit {max_hundreds} hundreds')
    
    # Repeat the same logic for fifties
    if amount_of_fifties > 0:
        max_fifties = ending_deposit // 50
        if max_fifties > amount_of_fifties:
            print(f'Deposit {amount_of_fifties} fifties')
            ending_deposit = ending_deposit - (50 * amount_of_fifties)
        else:
            ending_deposit = ending_deposit - (50 * max_fifties)
            print(f'Deposit {max_fifties} fifties')
    
    # Repeat the same logic for twenties
    if amount_of_twenties > 0:
        max_twenties = ending_deposit // 20
        if max_twenties > amount_of_twenties:
            print(f'Deposit {amount_of_twenties} twenties')
            ending_deposit = ending_deposit - (20 * amount_of_twenties)
        else:
            ending_deposit = ending_deposit - (20 * max_twenties)
            print(f'Deposit {max_twenties} twenties')
    
    # # Repeat the same logic for tens
    if amount_of_tens > 0:
        max_tens = ending_deposit // 10
        if max_tens > amount_of_tens:
            print(f'Deposit {amount_of_tens} tens')
            ending_deposit = ending_deposit - (10 * amount_of_tens)
        else:
            ending_deposit = ending_deposit - (10 * max_tens)
            print(f'Deposit {max_tens} tens')
            
    # # Repeat the same logic for fives
    if amount_of_fives > 0:
        max_fives = ending_deposit // 5
        if max_fives > amount_of_fives:
            print(f'Deposit {amount_of_fives} fives')
            ending_deposit = ending_deposit - (5 * amount_of_fives)
        else:
            ending_deposit = ending_deposit - (5 * max_fives)
            print(f'Deposit {max_fives} fives')
    
    # # Repeat the same logic for ones
    if amount_of_ones > 0:
        max_ones = ending_deposit // 1
        if max_ones > amount_of_ones:
            print(f'Deposit {amount_of_ones} ones')
            ending_deposit = ending_deposit - (1 * amount_of_ones)
        else:
            ending_deposit = ending_deposit - (1 * max_ones)
            print(f'Deposit {max_ones} ones')
else:
    print("\nThere is no deposit")

