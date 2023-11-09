from datetime import date


class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


products = [
    Product("Dog", "Mammals", 199.00),
    Product("Cat", "Mammals", 99.00),
    Product("Rabbit", "Mammals", 30.00),
    Product("Guinea Pig", "Mammals", 15.00),
    Product("Cockatiel", "Birds", 175.00),
    Product("Mouse", "Mammals", 2.00),
    Product("Ferret", "Mammals", 100.00),
    Product("Snake", "Reptiles", 60.00),
    Product("Betta Fish", "Fish", 5.00),
    Product("Bearded Dragon", "Reptiles", 50.00),
    Product("Hamster", "Mammals", 15.00),
    Product("Turtle", "Reptiles", 45.00),
]


def display_menu():
    print("Welcome to the GC Pet Store! Here is what we have to offer: ")
    for i, pet in enumerate(products):
        print(f'{i + 1}. {pet.name}: ${pet.price:.2f}')


def sales_tax(total, tax):
    return total * (tax / 100)


order = []
tax = 6.00

while True:
    display_menu()
    option = int(input("What pet would you like to adopt? Enter the corresponding number. Type '0' if you are ready to finalize your purchase: "))
    if 1 <= option and option <= len(products):
        howmany = int(input(f"How many {products[option - 1].name} would you like? Enter a valid value: "))
        selection = products[option - 1]
        print(f"You have selected {howmany} {selection.name} for ${selection.price:.2f} each!")
        total = selection.price * howmany
        print(f'The cost for this is: ${total:.2f}')
        order.append((selection.name, selection.price, howmany, total))
    elif option == 0:
        break

print("Here is your total:")
subtotal = sum(item[3] for item in order)
salestax = sales_tax(subtotal, tax)
grandtotal = subtotal + salestax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${salestax:.2f}")
print(f"Grand Total: ${grandtotal:.2f}")

while True:
    payment_type = input("Would you like to pay with cash, check, or credit? ")
    if payment_type == "cash":
        cash_tender = int(input("Amount tendered: "))
        change = cash_tender - grandtotal
        print(f"Change:  ${change}")
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
        print("Invalid payment type. Please enter cash, check or credit.")

print("Thank you for shopping at the GC Pet Store!")
print("Here is you receipt: ")
print(f'Date: {date.today()}')
#for item in order:
    #print items
print(f'Subtotal: {subtotal}')
print(f'Sales Tax: {salestax}')
print(f'Total: {grandtotal}')
print(f'Payment Method: {payment_type}')
