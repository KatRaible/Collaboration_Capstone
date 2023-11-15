from datetime import date


class Pet:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


pets = [
    Pet("Dog(s)", "Dogs", 199.00),
    Pet("Cat(s)", "Cats", 99.00),
    Pet("Rabbit(s)", "Rabbits", 30.00),
    Pet("Guinea Pig(s)", "Guinea_Pigs", 15.00),
    Pet("Birds", "Birds", 175.00),
    Pet("Mice", "Mice", 2.00),
    Pet("Ferret(s)", "Ferrets", 100.00),
    Pet("Snake(s)", "Snakes", 60.00),
    Pet("Betta Fish", "Fish", 5.00),
    Pet("Bearded Dragon", "Dragon", 50.00),
    Pet("Hamster(s)", "Hamsters", 15.00),
    Pet("Turtle(s)", "Turtles", 45.00),
]


def display_menu(pet_list):
    print()
    print("Welcome to the Pawsitive Pets Pet Store! Here is what we have to offer: ")
    print()
    print("============================================================")
    print()
    for i, pet in enumerate(pet_list, 1):
        print(f'{i}. {pet.name}: ${pet.price:.2f}')


def sales_tax(total, tax):
    return total * (tax / 100)


tax = 6.00


def get_user_input(prompt, input_type=int):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid value.")


def process_order(products):
    order = []

    while True:
        display_menu(products)
        print()
        option = get_user_input(
            "What pet would you like to adopt? Enter the corresponding number. Type '0' if you are ready to finalize "
            "your purchase: ")

        if 1 <= option <= len(products):
            howmany = get_user_input(f"How many {products[option - 1].name} would you like? Enter a valid value: ")
            selection = products[option - 1]
            print(f"You have selected {howmany} {selection.name} for ${selection.price:.2f} each!")
            total = selection.price * howmany
            print(f'The cost for this is: ${total:.2f}')
            print()
            order.append((selection.name, selection.price, howmany, total))
        elif option == 0:
            break

    subtotal = sum(item[3] for item in order)
    salestax = sales_tax(subtotal, tax)
    grandtotal = float(subtotal + salestax)

    while True:
        print(f'Your grand total is going to be: ${grandtotal:.2f}')
        payment_type = input("Would you like to pay with cash, check, or credit? ")
        if payment_type == "cash":
            cash_tender = float(input("Amount tendered: "))
            while cash_tender < grandtotal:
                cash_tender = float(input("Insufficient funds... please enter enough cash: "))
                continue
            else:
                change = cash_tender - grandtotal
                print(f"Change: ${change:.2f}")
                break
        elif payment_type == "check":
            check_num = int(input("Check number: "))
            break
        elif payment_type == "credit":
            cc_num = int(input("Credit card number: "))
            exp = int(input("Expiration: "))
            cvv = int(input("CVV: "))
            break
        else:
            print("Invalid payment type. Please enter cash, check, or credit.")

    def display_receipt(order, subtotal, salestax, grandtotal, payment_type):
        print()
        print()
        print("Here is your receipt:")
        print()
        print("=====================")
        print()
        print(f'Date: {date.today()}')
        print()
        for item in order:
            print(f'{item[2]} {item[0]} at ${item[1]:.2f} each (${item[3]:.2f})')
        print()
        print(f'Subtotal: ${subtotal:.2f}')
        print(f'Sales Tax: ${salestax:.2f}')
        print(f'Total: ${grandtotal:.2f}')
        print(f'Payment Method: {payment_type}')
        print()
    display_receipt(order, subtotal, salestax, grandtotal, payment_type.upper())


order = process_order(pets)
print()
print("Thank you for shopping at the Pawsitive Pets Pet Store!")
print()
print()
print()

