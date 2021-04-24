
if __name__ == "__main__":
    import random

    min_val = 1
    max_val = 6

    total = 0
    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        print("Rolling the dices...")
        print("The values are: ")

        first = random.randint(min_val, max_val)
        second = random.randint(min_val, max_val)

        total = int(first) + int(second) + total

        print(f"{first}  {second}")

        roll_again = input("Roll the dices again?\n")

    print("Total earned points: ", total)
    print("The game has ended!")
