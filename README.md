# VIT Bhopal Campus Food Court Ordering System

## 1. Project Overview

A Python-based console application that allows students to select food items, add them to a cart, calculate the total bill, and place an order. The program also generates a random order token. 

## 2. Features

* Food menu with prices
* Add items to cart
* View cart and total bill
* Place an order
* Generate random order token
* Display order status
* Handle empty-cart orders
* Handle invalid choices
* Exit option 

## 3. Technologies/Tools Used

* **Language:** Python
* **Module:** `random`
* **Interface:** Command-Line Interface (CLI)
* **Tools:** VS Code / IDLE / PyCharm / Command Prompt

## 4. Installation & Running

1. Install Python.
2. Save the program as `vit_food_court.py`.
3. Open Command Prompt/Terminal.
4. Navigate to the project folder.
5. Run:

```bash
python vit_food_court.py
```

The program will display the food menu and options.

## 5. Testing Instructions

Test the following:

| Input          | Expected Result              |
| -------------- | ---------------------------- |
| `1`            | Add Pizza                    |
| `2`            | Add Garlic Bread             |
| `3`            | Add Veg Burger               |
| `4`            | Add Cold Coffee              |
| `5`            | Display Cart & Bill          |
| `6`            | Place Order & Generate Token |
| `7`            | Exit                         |
| Invalid number | Display error message        |

The program checks for an empty cart before placing an order and generates a four-digit token for successful orders. 

## 6. Flowchart

```text
START
  ↓
Display Menu
  ↓
Get User Choice
  ↓
Add Food / View Cart / Place Order
  ↓
Calculate Bill
  ↓
Generate Token
  ↓
Clear Cart
  ↓
Return to Menu
  ↓
Exit?
 ├─ No → Menu
 └─ Yes → END
```

## 7. Screenshots

Recommended screenshots:

1. Main menu
2. Food item added to cart
3. Cart with total bill
4. Successful order with token
5. Invalid-choice message

## 8. Conclusion

The **VIT Bhopal Campus Food Court Ordering System** is a simple Python project demonstrating lists, loops, conditional statements, user input, bill calculation, and random token generation. It provides a basic model of a digital campus food-ordering system.
