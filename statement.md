VIT Bhopal Campus Food Court Ordering System
1. Problem Statement

In a college campus food court, students and other college members need to select food items, calculate their bill, and place orders efficiently. A simple manual process can make order management less convenient.

The purpose of this project is to develop a Python-based food ordering system that provides a simple digital method for selecting food items, maintaining a cart, calculating the total bill, and placing an order.

The system also generates a unique token after a successful order, which can be used to identify the order.

2. Scope of the Project

The scope of this project is to provide a basic console-based food ordering system for the VIT Bhopal campus.

The system currently supports:

Displaying available food items and prices.
Adding food items to a cart.
Viewing selected items.
Calculating the total bill.
Checking whether the cart is empty.
Placing an order.
Generating a random four-digit order token.
Displaying the order status.
Clearing the cart after successful ordering.
Handling invalid menu choices.

The current project is limited to a command-line interface and does not include a database, online payment system, or graphical interface.

3. Target Users

The primary target users of this project are:

Students

VIT Bhopal students can use the system to select food items and calculate their order amount.

College Members

Other college members can use the application to select food from the available campus menu.

Food Court Staff

The system can provide a basic model for managing customer orders and generating order tokens.

The code specifically describes the cart as tracking items added by students or college members.

4. High-Level Features
1. Food Menu

Displays available food items such as Margherita Pizza, Garlic Bread, Veg Burger, and Cold Coffee with their prices.

2. Cart Management

Users can add selected food items and their prices to the cart.

3. Bill Calculation

The system calculates the total price of all selected food items.

4. Order Placement

Users can place an order after adding items to their cart.

5. Order Token

A random four-digit token is generated after successful order placement.

6. Order Status

The system displays the order status as "Preparing in Kitchen."

7. Empty Cart Validation

The system prevents users from placing an order when the cart is empty.

8. Invalid Input Handling

If the user enters an option other than 1–7, the program displays an appropriate message.

9. Exit Function

The user can select option 7 to exit the application.
