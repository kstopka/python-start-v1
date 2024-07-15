print()


def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game


tomek = parent_function("Tomek", 3)
ania = parent_function("Ania", 5)

tomek()
tomek()

ania()

tomek()
