from datetime import date


class Pet:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def display_info(self):
        print(f'{self.name}: ${self.price:.2f}')


class Dog(Pet):
    def __init__(self, name, category, price, age_category='Dog'):
        super().__init__(name, category, price)
        self.age_category = age_category


class Cat(Pet):
    def __init__(self, name, category, price, age_category='Cat'):
        super().__init__(name, category, price)
        self.age_category = age_category


pets = [
    Pet("Dog", "Mammals", 199.00),
    Pet("Cat", "Mammals", 99.00),
    Pet("Rabbit", "Mammals", 30.00),
    Pet("Guinea Pig", "Mammals", 15.00),
    Pet("Cockatiel", "Birds", 175.00),
    Pet("Mouse", "Mammals", 2.00),
    Pet("Ferret", "Mammals", 100.00),
    Pet("Snake", "Reptiles", 60.00),
    Pet("Betta Fish", "Fish", 5.00),
    Pet("Bearded Dragon", "Reptiles", 50.00),
    Pet("Hamster", "Mammals", 15.00),
    Pet("Turtle", "Reptiles", 45.00),
]


def display_menu(pet_list):
    print("Welcome to the GC Pet Store! Here is what we have to offer: ")
    for i, pet in enumerate(pet_list, 1):
        print(f'{i}. {pet.name}: ${pet.price:.2f}')


def sales_tax(total, tax):
    return total * (tax / 100)


order = []
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
        option = get_user_input("What pet would you like to adopt? Enter the corresponding number. Type '0' if you are ready to finalize your purchase: ")

        if 1 <= option <= len(products):
            howmany = get_user_input(f"How many {products[option - 1].name} would you like? Enter a valid value: ")
            selection = products[option - 1]
            print(f"You have selected {howmany} {selection.name} for ${selection.price:.2f} each!")
            total = selection.price * howmany
            print(f'The cost for this is: ${total:.2f}')
            order.append((selection.name, selection.price, howmany, total))
        elif option == 0:
            break

    subtotal = sum(item[3] for item in order)
    salestax = sales_tax(subtotal, tax)
    grandtotal = subtotal + salestax


    while True:
        payment_type = input("Would you like to pay with cash, check, or credit? ")
        if payment_type == "cash":
            cash_tender = int(input("Amount tendered: "))
            change = cash_tender - grandtotal
            print(f"Change: ${change}")
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
        print("Here is your receipt:")
        print(f'Date: {date.today()}')
        for item in order:
            print(f'{item[2]} {item[0]} at ${item[1]:.2f} each: ${item[3]:.2f}')
        print(f'Subtotal: ${subtotal:.2f}')
        print(f'Sales Tax: ${salestax:.2f}')
        print(f'Total: ${grandtotal:.2f}')
        print(f'Payment Method: {payment_type}')


    display_receipt(order, subtotal, salestax, grandtotal, payment_type.upper())

order = process_order(pets)
print("Thank you for shopping at the GC Pet Store!")
