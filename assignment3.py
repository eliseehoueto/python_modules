def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


original_price = float(input("Please enter the base price: "))
        
discount_percentage = float(input("Please enter the discount percent : "))

final_price = calculate_discount(original_price, discount_percentage)

if final_price == original_price:
    print(f"No discount. The final price is : {final_price:.2f} €")
else:
    print(f"The final price after a discount of {discount_percentage:.2f}% is : {final_price:.2f} ")

