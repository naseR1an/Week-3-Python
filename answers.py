# Question one
def calculate_discount(price, discount_percent):
    """Calculate final price after applying discount if it's 20% or higher."""
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))  # Apply discount
        return final_price
    else:
        return price  # Return original price 

# Question two
price = int(input("Enter the price of the item: "))
discount_percent = int(input("Enter the discount percentage: "))
print (f"The final price is: {calculate_discount(price, discount_percent)}")


