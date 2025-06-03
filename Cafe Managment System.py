class Menu:
    def __init__(self):
        self.items = {
            "Burger": 200,
            "Pasta": 150,
            "Fries": 100,
            "Coffe": 100,
            "Cold Drink": 250
        }

    def display_menu(self):
        print("List of orders:")
        for name, price in self.items.items():
            print(f"{name} : {price} Rs")

    def is_available(self, item):
        return item in self.items

    def get_price(self, item):
        return self.items[item]


class Order:
    def __init__(self, menu):
        self.menu = menu
        self.total_bill = 0
        self.items_ordered = []

    def take_order(self):
        try:
            total_items = int(input("How many items you want to order: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        for _ in range(total_items):
            item = input("Order item: ")
            if self.menu.is_available(item):
                self.total_bill += self.menu.get_price(item)
                self.items_ordered.append(item)
            else:
                print("Sorry, that's not a valid order.")

    def show_bill(self):
        if not self.items_ordered:
            print("Sorry, you have no order.")
        else:
            print("Your total bill is:", self.total_bill)


class Cafe:
    def __init__(self):
        self.menu = Menu()
        self.order = Order(self.menu)

    def run(self):
        print("Welcome to my mini restaurant Lahore :")
        self.menu.display_menu()
        self.order.take_order()
        self.order.show_bill()

        query = input("If you have any problem or queries, type Yes/No: ")
        if query.lower() == "yes":
            message = input("Type your message: ")
            if message:
                print("Thank you for your valuable feedback!")
        else:
            print("Thank you for giving us a chance to serve you!")



# Start the program
if __name__ == "__main__":
    cafe = Cafe()
    cafe.run()