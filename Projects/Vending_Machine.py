class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}"

class VendingMachine:
    def __init__(self):
        self.products = [
            Product("Chips", 1.50),
            Product("Soda", 2.00),
            Product("Candy", 1.00)
        ]
    
    def display_products(self):
        # Display available products and their prices
        print("Available products:")
        for product in self.products:
            print(product)
    
    def make_purchase(self, product_name, money_inserted):
        # Find the product based on the input name
        product = None
        for p in self.products:
            if p.name.lower() == product_name.lower():
                product = p
                break
        
        # If the product is found and the money is sufficient
        if product:
            if money_inserted >= product.price:
                change = round(money_inserted - product.price, 2)
                print(f"Purchase successful! You bought {product.name} for {product.price}. Your change is {change}.")
            else:
                print("Insufficient funds. Please insert more money.")
        else:
            print("Product not found.")

# Function to simulate the vending machine process
def vending_machine_simulation():
    machine = VendingMachine()
    
    # Display available products
    machine.display_products()
    
    # Get user input for product choice and money inserted
    product_name = input("\nChoose product: ")
    
    try:
        # Convert inserted money to float and process the purchase
        money_inserted = float(input("Money inserted: "))
        machine.make_purchase(product_name, money_inserted)
    except ValueError:
        print("Invalid input. Please insert a valid amount of money.")

# Run the vending machine simulation
if __name__ == "__main__":
    vending_machine_simulation()
