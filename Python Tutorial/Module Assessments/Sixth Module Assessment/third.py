def main():
    
    class Products:
        product_list = []
        
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = float(price)
            self.quantity = int(quantity)
        
        def display_info(self):
            print(f"Name: {self.name} | Price: {self.price} | Quantity: {self.quantity}")
        
        @classmethod
        def display_all_products(cls):
            for product in cls.product_list:
                product.display_info()
                
             
    
        @classmethod
        def add_item(cls):
            name = input('Enter the name of the new item: ')
            price = input('Enter the price of the new item: ')
            quantity = input('Enter the quantity of the new item: ')
            new_item = cls(name, price, quantity)
            cls.product_list.append(new_item)
            print(f"{name} has been added to the inventory.")

        def update_qty(self, quantity):
            self.quantity = quantity
            print(f"Quantity for {self.name} updated to {self.quantity}.")
            
        @classmethod
        def find_product(cls,name):
            for product in cls.product_list:
                if product.name.lower() == product_name.lower():
                    return product
            return None
            
        @classmethod
        def total_value(cls):
            value = 0
            for product in cls.product_list:
                value += product.price * product.quantity
                
            print(f"The total inventory value is: {value}")    
            return value
    while True:
        new_product = input('Would you like to add a product to the inventory? yes/no')
        if new_product.lower() == 'yes':
            Products.add_item()

        else:
            new_quantity = input('Would you like to update the quantity of an item? yes/no')
            if new_quantity.lower() == 'yes':
                product_name = input('Which product would you like to update? ').lower()
            
                product = Products.find_product(product_name)  # Find the product by name
                if product:
                    new_qty = int(input(f"Enter the new quantity for {product_name}: "))
                    product.update_qty(new_qty)  # Call the instance method
                else:
                    print(f"Product '{product_name}' not found in inventory.")
            else:
                print("This concludes the inventory session.")
                break
                
    Products.display_all_products()
    Products.total_value()
    
    
main()