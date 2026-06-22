import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]          # results = []
                                                               # for symbol in range(3):
                                                               #     results.append(random.choice(symbols))
                                                               # return results

def print_row(row):
    print("-------------")
    print(" | ".join(row))
    print("-------------")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100

    print("-------------------------")
    print("welcome to python slots- ")
    print("symbols: 🍒 🍉 🍋 🔔 ⭐ ")
    print("-------------------------")

    while balance > 0:
        print(f"current balance: {balance}")

        bet = input("enter your bet: $")

        if not bet.isdigit():
            print("please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("insufficient funds")
            continue

        if bet <= 0:
            print("bet must be greater than 0")
            continue

        balance = balance - bet

        row = spin_row()
        print("-------------")
        print("spinning...")
        print_row(row)
        payout = get_payout(row, bet)

        if payout > 0:
            print(f"you won ${payout}")
        else:
            print("you lost")

        balance += payout

        play_again = input("do you want to play again? (y/n): ").upper()

        if play_again != "Y":
            break

    print(f"game over! your final balance is ${balance}")


if __name__ == "__main__":
    main()