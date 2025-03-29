def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    :param price: float - Original price of the item
    :param discount_percent: float - Discount percentage to be applied
    :return: float - Final price after discount
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price  # Return original price if discount is less than 20%

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate and display the final price
    final_price = calculate_discount(original_price, discount_percentage)
    print(f"Final price after discount: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
