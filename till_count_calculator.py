coins = float(input("Enter amount in coins: "))
ones = float(input("Enter amount in ones: "))
fives = float(input("Enter amount in fives: "))
tens = float(input("Enter amount in tens: "))
twenties = float(input("Enter amount in twenties: "))
fifties = float(input("Enter amount in fifties: "))
hundreds = float(input("Enter amount in hundreds: "))

amount_of_fives = fives / 5
amount_of_tens = tens / 10
amount_of_twenties = twenties / 20
amount_of_fifties = fifties / 50
amount_of_hundreds = hundreds / 100
amount_of_ones = ones / 1

total = coins + ones + fives + tens + twenties + fifties + hundreds

print(f'\nYou have a total of ${total}')

if total > 300:
    deposit = total - 300
    ending_deposit = deposit
    print(f'\nYou have to deposit ${deposit}')

    if amount_of_hundreds > 0:
        max_hundreds = ending_deposit // 100
        if max_hundreds > amount_of_hundreds:
            print(f'Deposit {amount_of_hundreds} hundreds')
            ending_deposit = ending_deposit - (100 * amount_of_hundreds)
        else:
            ending_deposit = ending_deposit - (100 * max_hundreds)
            print(f'Deposit {max_hundreds} hundreds')

    if amount_of_fifties > 0:
        max_fifties = ending_deposit // 50
        if max_fifties > amount_of_fifties:
            print(f'Deposit {amount_of_fifties} fifties')
            ending_deposit = ending_deposit - (50 * amount_of_fifties)
        else:
            ending_deposit = ending_deposit - (50 * max_fifties)
            print(f'Deposit {max_fifties} fifties')

    if amount_of_twenties > 0:
        max_twenties = ending_deposit // 20
        if max_twenties > amount_of_twenties:
            print(f'Deposit {amount_of_twenties} twenties')
            ending_deposit = ending_deposit - (20 * amount_of_twenties)
        else:
            ending_deposit = ending_deposit - (20 * max_twenties)
            print(f'Deposit {max_twenties} twenties')

    if amount_of_tens > 0:
        max_tens = ending_deposit // 10
        if max_tens > amount_of_tens:
            print(f'Deposit {amount_of_tens} tens')
            ending_deposit = ending_deposit - (10 * amount_of_tens)
        else:
            ending_deposit = ending_deposit - (10 * max_tens)
            print(f'Deposit {max_tens} tens')

    if amount_of_fives > 0:
        max_fives = ending_deposit // 5
        if max_fives > amount_of_fives:
            print(f'Deposit {amount_of_fives} fives')
            ending_deposit = ending_deposit - (5 * amount_of_fives)
        else:
            ending_deposit = ending_deposit - (5 * max_fives)
            print(f'Deposit {max_fives} fives')

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

