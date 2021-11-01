""" Restaurant stories"""
from models import RestaurantHall, Waiter, Customer, FoodStorage, Chef, \
    Kitchen, Cook, AccessibleMenu, Order, Delivery

SCORE = 0


def ex():
    """Exit function"""
    exit(0)

if __name__ == "__main__":
    while True:
        rest = RestaurantHall()
        jarvis = Waiter("Jarvis", 3500)
        print(f"Welcome to the {rest.restaurant_name}! Myname is {jarvis.name}, I`m you waiter.")
        print(f"{jarvis.name}:How can I contact you?")
        name = input("My name is    ")
        SCORE += 1
        customer = Customer(name)
        print(f"{jarvis.name}: Hello {customer.name}, how many guests will there be?")
        SCORE += 1
        while True:
            customer_amount = input(f"{customer.name}: Only   ")
            if not customer_amount.isdigit():
                continue
            FREE_TABLE = rest.add_visitors(int(customer_amount))
            if FREE_TABLE == 5:
                print(f"You score: {SCORE}")
                ex()
            elif FREE_TABLE == 2:
                continue
            elif FREE_TABLE == 1:
                SCORE += 1
                break

        print(f"{jarvis.name}: Do you want to see menu, Y or N?")

        while True:
            res = input(f"{customer.name}: ")
            if res in ("Y", "y", "д", 'Д', "YES", "yes", "Yes"):
                SCORE += 1
                break

            if res in ("N", "NO", "n", "No", "no", "Н", "н"):
                print(f'{jarvis.name}: Sorry, I hope to see you next time!')
                print(f"You score: {SCORE}")
                ex()
            else:
                print(f"{jarvis.name}: You are drunk, get out of here!")
                print(f"You score: {SCORE}")
                ex()

        chef = Chef("Grzegorz Bzhenchishchikiewicz", 1500)

        print(f"{jarvis.name}: Great, our chef mr. {chef.name} has prepared a wonderful menu!")
        storage = FoodStorage()
        chef.make_menu(storage.food_list)

        ac_menu = AccessibleMenu(chef.menu)
        menu = ac_menu.get_menu()
        order = Order(customer.name)
        print(f"{jarvis.name}: Please enter your order!")
        while True:
            dish = input(f"{customer.name}: ")
            if not dish.isdigit():
                continue
            chose = menu[int(dish)]
            SCORE += 1
            if chose not in order.order:
                order.order.append(chose)
                print(f"{jarvis.name}: You chosed {chose}")
                print(f"{jarvis.name}: Do you want to add something else? Y or N")
                ch = input(f"{customer.name}: ")

                if ch in ("Y", "y"):
                    ac_menu.get_menu()
                    SCORE += 1
                    continue
                if ch not in ("N", "n"):
                    print(f"{jarvis.name}: I do not understand...")
                else:
                    jarvis.take_order(order.order)
                    break

            else:
                print(f"{jarvis.name}: {chose} already ordered!")
        print(f"{jarvis.name}: Thanks for your order {customer.name}, \
our chef will make it as fast as possible.")
        SCORE += 1

        kitchen = Kitchen()
        kitchen.take_order(jarvis.order_list)
        cook = Cook("Кейси Райбек", 1500)
        for cur_dish in kitchen.current_dish:
            cook.cook_food(cur_dish)
        kitchen.make_food(rest.amount_visitors)
        delivery = Delivery(kitchen.current_dish)
        jarvis.delivery_order(delivery.send_order())

        print(f"{jarvis.name}: Here's your order, bon appetit!")

        print("### Don't you think the food smells somehow unpleasant? Y or N ###")

        ch = input("...:")

        if ch in ("Y", "y"):
            print(f"{customer.name}: {jarvis.name}, come here please.")
            SCORE += 1
        elif ch in ("N", "N"):
            print(f"{customer.name}: Thank you, it was delicious!")
            print("You died two days later due to poisoning.!")
            print(f"Score {SCORE}")
            ex()

        print(f"{jarvis.name}: Yes, I'm listening, would you like to order more?")
        print(f"{customer.name}: Uh, no, it seems to me that something is wrong with this dish.")

        print(f"{jarvis.name}: I'm sorry?")
        print(f"{customer.name}: Smell it, it smells bad!")

        print(f"{jarvis.name}: What are you, no, it was cooked by the chef himself!")
        print(f"{customer.name}: No, I'm pretty sure it's gone bad, mold is here!")

        print(f"{jarvis.name}: You deceiver! Have you decided to eat for free? We have the best!")
        print("### The waiter looks very angry ###")

        print("\n### What will you answer? ###")
        print("1. No, it's okay.\n2. I'll call the police now!")

        ch = input("...: ")
        if ch.isdigit():
            if int(ch) == 1:
                print(f"{customer.name}: No, it's okay, I'm sorry, I made a mistake.")
                print(f"{jarvis.name}: Fine, now get out of here!")
                print("...")
                print("### Died 2 days later due to poisoning. ###")
                print(f"score: {SCORE}")
                ex()
            elif int(ch) == 2:
                print(f"{customer.name}: Get your superiors here immediately, \
                or I'll call the police!")
                print()
                print("### Open Achievement: Don't be a pussy! ###")
                SCORE += 10
            else:
                print("### You vomited right on top of a visitor sitting next to you. ###")
                print("### Panic began, and a noise rose around. \
Soon an ambulance arrived and you were taken to the hospital. You survived! ###")
                print(f"score: {SCORE}")
                ex()
        print(f"{jarvis.name}: I'm not calling anyone! You are in the {rest.restaurant_name}, \
it's the most exclusive restaurant in town!")
        print(f"{jarvis.name}: Get out, you miserable pauper!")

        print("\n### What will you answer? ###")
        print("1. I'm sorry.\n2. An upscale restaurant? It's a dump.")

        ch = input("...: ")
        if int(ch) in (1, 2):
            if int(ch) == 1:
                print(f"{customer.name}: No, it's okay, I'm sorry, I made a mistake.")
                print(f"{jarvis.name}: Fine, now get out of here!")
                print("...")
                print("### Died 2 days later due to poisoning. ###")
                print(f"score: {SCORE}")
                ex()
            elif int(ch) == 2:
                print(f"{customer.name: An upscale restaurant? \
\nIt's a dump! The interior is like a cheap joint, that's one. \
\nIt stinks in here, that's two. And you stink, that's three!}")
                print()
                SCORE += 15
        else:
            print("### You vomited right on top of a visitor sitting next to you. ###")
            print("### Panic began, and a noise rose around. \
Soon an ambulance arrived and you were taken to the hospital. \
You survived! ###")
            print(f"score: {SCORE}")
            ex()
        print("### From such an unexpected answer, \
you see the waiter blush and lose the joy of speech. ###")
        print("### Would you like to strike first? Y or N ###")

        ch = input("...: ")
        if ch in ("Y", 'y'):
            print(f"{customer.name}: Get in your face!")
            print("### You do a straight hook! \
Your opponent falls to the floor, blood streaming down his face. \
You win! ####")
            SCORE += 45
            print(f"score: {SCORE}")
            ex()
        elif ch in ("N", "n"):
            print(f"{jarvis.name}: Take that commoner!")
            print("### From the impact, you fall to the floor. \
Blood runs down your face. It's not blood running down your pants. \
You have been filmed on your phone and are already being posted on YouTube.  ###")
            print("### Achievement open: Wet Pants! ###")
            print("### You lost. ###")
            SCORE -= 25
            print(f"score: {SCORE}")
            ex()

        else:
            print("### You vomited right on top of a visitor sitting next to you. ###")
            print("### Panic began, and a noise rose around. \
Soon an ambulance arrived and you were taken to the hospital. You survived! ###")
            print(f"score: {SCORE}")
            ex()
