import random

# track the items the student or any college members  adds to their cart.
cart_items = []
cart_prices = []
running = True

print("=========================================")
print("  welcome to the vit - bhopal resturant , in campus ")
print("=======================================")

while running == True:
    print("\n--- list of foods with price  ---")
    print("1. [Domino's] Margherita Pizza - ₹199 -only" )
    print("2. [Domino's] Garlic Bread     - ₹99-only(after applying the discount of 12%)" )
    print("3. [Nescafe]   veg burger    - ₹120-only" )
    print("4. [Nescafe]  cold Coffee  - ₹90(after applying the discount of 10 %)")
    print("5.  View My Cart & Total bill")
    print("6.  Place Order (Generate Token)")
    print("7.  Exit App")
    print("you can see your details in above paragraph")
    
    # giving option to customer to choose from the previous mention options.
    choice = input("\nSelect an option number (1-7): ")
    
    # making menu condition using if,elif condition :
    if choice == "1":
        cart_items.append("Margherita Pizza")
        cart_prices.append(199)
        print(" Added Margherita Pizza to your cart")
        
    elif choice == "2":
        cart_items.append("Garlic Bread")
        cart_prices.append(99)
        print(" Added Garlic Bread to your cart")
        
    elif choice == "3":
           cart_items.append("veg burger")
           cart_prices.append(120)
           print(" Added veg burger to your cart")
           
    elif choice == "4":
           cart_items.append("cold Coffee")
           cart_prices.append(90)
           print(" Added cold Coffee to your cart!")
        
    elif choice == "5":
        print("\n--- YOUR ORDER CART ---")
    
        if len(cart_items) == 0:
            print("Your cart is empty.")
        else:
    
        
            total_price = 0

            for i in range(len(cart_items)):

                print(f"- {cart_items[i]}: ₹{cart_prices[i]}")
                total_price = total_price + cart_prices[i]

            print(f"Total Bill Amount: ₹{total_price}")
            
    elif choice == "6":
        
        if len(cart_items) == 0:
            print("\n Error: Cannot place an order with an empty cart!")
        else:
            
            total_price = 0
            for price in cart_prices:
                total_price =  total_price + price
                
            print("\n=======================================")
            print(" ORDER PLACED SUCCESSFULLY ")
            print("=========================================")
            
            
            random_token = random.randint(1000, 9999)

            print(f"Your Unique Token ID: TK-{random_token}" )

            print(f"Total Amount to Pay at Stall: ₹{total_price}" )

            print("Current Order Status: Preparing in Kitchen")


            print("=========================================" )
            
            
            cart_items = []
            cart_prices = []
            
    elif choice == "7":
        print("\n Thank you for visiting VIT Food Court , please come again , good byy")
        running = False

        
    else:
        print("\n you have choosen wrong choice , please choose it from 1-7 mention  in options ")
