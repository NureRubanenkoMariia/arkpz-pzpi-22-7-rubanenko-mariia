# Поганий приклад, невідомо, що означає 'tp'
tp = 100.0  

# Гарний приклад, зрозуміло, що це загальна ціна
total_price = 100.0  


# Поганий приклад
def gUI():
    pass

# Гарний приклад
def get_user_info():
    pass

# Гарний приклад
class UserProfile:
    pass

# Поганий приклад
# Calculate the total price including applicable taxes and discounts
def calculate_final_price(base_price, tax_rate=0.15, discount=0.0):
    """
    Calculate the final price after applying tax and discount.
    
    Parameters:
        base_price (float): The original price before tax or discount.
        tax_rate (float, optional): Tax rate to apply to the base price. Default is 15%.
        discount (float, optional): Discount amount to subtract from the total price.
    
    Returns:
        float: The final price including tax, minus any discounts.
    """
    # Apply tax to base price
    taxed_price = base_price * (1 + tax_rate)

    # Subtract discount to get final price
    final_price = taxed_price - discount
    return round(final_price, 2)

# Гарний приклад
def calculate_final_price(base_price, tax_rate=0.15, discount=0.0):
    """
    This function calculates something.
    
    Parameters:
        base_price (float): base price of the item.
        tax_rate (float): tax rate.
        discount (float): discount to subtract.
    
    Returns:
        float: Returns the calculated price.
    """
    # Calculate tax by multiplying base_price with tax_rate
    taxed_price = base_price * (1 + tax_rate)  # This is where tax is applied
    
    # Subtract discount
    final_price = taxed_price - discount  # Apply discount here
    
    return round(final_price, 2)  # Round final price

# Гарний приклад
class ShoppingCart:
    """
    A class to represent a shopping cart in an e-commerce application.
    
    Attributes:
        items (dict): A dictionary where keys are item names and values are tuples of (price, quantity).
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}
    
    def add_item(self, item_name, price, quantity=1):
        """
        Add an item to the shopping cart.
        
        Parameters:
            item_name (str): Name of the item.
            price (float): Price of a single unit of the item.
            quantity (int, optional): Quantity to add. Defaults to 1.
        """
        # Check if item already in cart; update quantity if so
        if item_name in self.items:
            existing_quantity = self.items[item_name][1]
            self.items[item_name] = (price, existing_quantity + quantity)
        else:
            self.items[item_name] = (price, quantity)

# Гарний приклад
def calculate_total_price(user_data):
    """
    Calculates the total price of a user's orders, including any applicable discount.

    Parameters:
        user_data (dict): A dictionary containing user information, 
                          including a list of orders and an optional discount.

    Returns:
        float: The total order amount after applying the discount, rounded to two decimal places.
    """
    total_price = sum(order["price"] for order in user_data.get("orders", []))
    
    # Apply discount if available
    discount = user_data.get("discount", 0)
    if discount:
        total_price -= total_price * discount

    return round(total_price, 2)

# Поганий приклад
def calculate_total(amount, tax, discount):
 if amount > 0:
     total = amount + amount * tax - discount
 if(total < 0):
   total = 0
 return total

# Гарний приклад
def calculate_total(amount, tax, discount):
    """Calculate total amount after applying tax and discount."""
    
    if amount > 0:
        total = amount + (amount * tax) - discount
        
        if total < 0:
            total = 0
    else:
        total = 0
    
    return total

# Поганий приклад
# function t find m and sort
def srt( lst) :
    for i in range(0,len ( lst )) :
        mn = i
        for j in range(i+ 1 , len(lst)):
            if ( lst [ j ] < lst[mn]):
                mn =j 
    temp= lst [ i] ;
    lst [i ] = lst [ mn ]
    lst[mn ] = temp # now swap
                            # we no need return ?
    return lst 


# Гарний приклад
# Function to perform selection sort on a list
def selection_sort(numbers):
    """
    Sorts a list of numbers in ascending order using the selection sort algorithm.
    :param numbers: list - List of numbers to be sorted
    :return: list - Sorted list
    """
    for i in range(len(numbers)):
        # Assume the minimum element is the current index
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        # Swap the found minimum element with the current element
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers
