def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If discount is 20% or higher, apply it; otherwise, return original price.
    """
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price


# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Print the result
    if discount_percentage >= 20:
        print(f"Discount applied! Final price: ${final_price:.2f}")
    else:
        print(f"Discount not eligible (must be 20% or higher). Original price: ${final_price:.2f}")

except ValueError:
    print("Error: Please enter valid numbers for price and discount percentage.")
