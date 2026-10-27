#You're building a feature that calculates discounted prices for an online store. You want to be able to set different
#  discount amounts and control whether prices are
#  rounded to look cleaner in the app.

#In this exercise, you will create a custom function
#  that handles these requirements using default
#  and keyword arguments.

original_price = 899.99

# Define the function with default arguments
def calculate_discount(price, discount_percent=15, round_result=True):
    discounted_price = price - (price * (discount_percent / 100))
    
    if round_result == True:
        # Round the result to two decimal places
        return round(discounted_price, 2)
    else:
        return discounted_price

# Call the function with keyword arguments
final_price = calculate_discount(price=original_price, discount_percent=25, round_result=False)
print(final_price)