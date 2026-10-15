import io
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:g} = ${total_cost:g}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2025"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return

        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                item.item_quantity = modified_item.item_quantity
                return

        print("Item not found in cart. Nothing modified.")
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        else:
            for item in self.cart_items:
                item.print_item_cost()

            total_quantity = 0
            for item in self.cart_items:
                total_quantity += item.item_quantity

            print(f"Number of Items: {total_quantity}")

        print()
        print(f"Total: ${self.get_cost_of_cart():g}")
def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("o - Output shopping cart")
    print("q - Quit")
    print()
#TODO: implement menus in execute_menu()

def execute_menu(menuOp, theCart):
    if menuOp == 'a':
        print("ADD ITEM TO CART")

        item = ItemToPurchase()

        print("Enter the item name:")
        item.item_name = input()

        print("Enter the item price:")
        item.item_price = float(input())

        print("Enter the item quantity:")
        item.item_quantity = int(input())

        theCart.add_item(item)
        
        


    elif menuOp == 'r':
        print("REMOVE ITEM FROM CART")

        print("Enter name of item to remove:")
        item_name = input()

        theCart.remove_item(item_name)


    elif menuOp == 'c':
        print("CHANGE ITEM QUANTITY")

        item = ItemToPurchase()

        print("Enter the item name:")
        item.item_name = input()

        print("Enter the new quantity:")
        item.item_quantity = int(input())

        theCart.modify_item(item)


    elif menuOp == 'o':
        print("OUTPUT SHOPPING CART")
        theCart.print_total()

                
if __name__ == "__main__":
    menu_choice = ' '
        
    cust_name = input("Enter customer's name:\n")
    day_date = input("Enter today's date:\n")

    print()
    print(f"Customer name: {cust_name}")
    print(f"Today's date: {day_date}")
    print()


    my_cart = ShoppingCart(cust_name, day_date)

    print_menu()

    while menu_choice != 'q':
        menu_choice = input('Choose an option:\n')
        
        if menu_choice in ['a', 'r', 'c', 'o']:
            execute_menu(menu_choice, my_cart)
            print_menu()

