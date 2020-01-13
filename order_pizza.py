answer_yes = ('y', 'ye', 'yes')
answer_no = ('n', 'no')
available_toppings = ['pepperoni', 'mushroom', 'onion', 'sausage', 'bacon',
'extra cheese', 'black olives', 'green pepper']
pizza_toppings = []

print("""
******************************
*        Hi!                 *
*Welcome to PapaJohn's Pizza *
******************************
""")

print("Would you like to place an order?")
customer = input("(Yes/No)\n -> ").lower()

if customer in answer_yes:
    print("We have 10/12/14 inches pizza. What is the pizza size you would like to order?")
    pizza_size = int(input("Size: "))
    if pizza_size == 10 or pizza_size == 12 or pizza_size == 14:
        print("""
What topping would you like to add to the pizza?
We have Pepperoni, Mushrooms, Onions, Sausage, Bacon, Extra cheese, Black olives, Green peppers.
(Enter 'Done' once you are finished)
        """)

        while True:
            pizza_topping = input("-> ").lower()
            if pizza_topping == 'done':
                break
            else:
                pizza_toppings.append(pizza_topping)
                continue
        
        if pizza_topping:
            print(f"\nOne {pizza_size} inch pizza coming right up!\n")
            for topping in pizza_toppings:
                if topping not in available_toppings:
                    print(f"Sorry, {topping.upper()} is NOT available.")
                else:
                    print(f"Adding {topping} to the pizza.")
            print("\nHere is your pizza. Thank you and enjoy your meal. Please come again soon.")
        else:
            print(f"One extra {pizza_size} inch plain pizza coming right up!\n")
            print("Here is your pizza. Thank you and enjoy your meal. Please come again soon.")

    else:
        print("Invalid value.")
        quit()

elif customer in answer_no:
    print("Thank you for coming. Please come again.")
else:
    print('Sorry, I did not understand that.')