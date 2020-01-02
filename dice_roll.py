import random
import time

start_roll = input("Do you want to roll the dice? ").lower()

while start_roll in ('y', 'ye', 'yes'):
    if start_roll in ('y', 'ye', 'yes'):
        roll_result = random.randint(0,6)
        print("Throwing the dice...")
        print("rolling...")
        time.sleep(0.5)
        print("rolling..")
        time.sleep(0.5)
        print("rolling.")
        time.sleep(.5)
        print(f'Congratulations, you rolled {roll_result}!')

        repeat = input("You want to play again? ")
        if repeat in ('n', 'no', 'nop', 'nope'):
            print("Nice playing with you")
            break

        elif repeat in ('y', 'ye', 'yes'):
            continue

        else:
            print("Invalid response. Answer Yes or No only.")
            break

else:
    print("Bye!")