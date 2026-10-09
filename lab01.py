'''
Lab01: Fiesta San ANtonio Food Ordering app
Chackpoint 1: Program Strcuture
Author: Uday Singh
abc123: fgr931
IS 2053 ON2

we need to create a file program that sets up the scaffold for Lab 1
-Define main() functions
-Print welcome message
-uses the if __name__ == "__main__": main() "gaurd" at bottome of calls
Include test harness to confirm setup
'''

# Checkpoint 2 Named constants and display menu

PRICE_TURKEY_LEG = 12.00
PRICE_CHICKEN_STICK = 8.00
PRICE_FUNNEL_CAKE = 6.50
PRICE_GORDITA = 5.50
PRICE_AGUA_FRESCA = 4.00
TAX_RATE = 0.0875

# Checkpoint 1 Set Up Your Program Structure


def main():
    # welcome message
    print("Welcome to the Fiesta Food Order App!")

    #  Display menu

    print(f"{'1. Turkey Leg':<25} ${PRICE_TURKEY_LEG:>6.2f}")
    print(f"{'2. Chicken-on-a-Stick':<25} ${PRICE_CHICKEN_STICK:>6.2f}")
    print(f"{'3. Funnel Cake':<25} ${PRICE_FUNNEL_CAKE:>6.2f}")
    print(f"{'4. Gordita':<25} ${PRICE_GORDITA:>6.2f}")
    print(f"{'5. Agua Fresca':<25} ${PRICE_AGUA_FRESCA:>6.2f}")
    print(f"Sales Tax Rate: {TAX_RATE * 100:.2f}%")
    # Checkpoint 3: Assumes constants defined in
    # checkpoint 2 menu choic eand quantity

    item_number = int(input("Enter the number of item you'd"
                            + " like to order?: "))
    quantity = int(input("How many would you like to order? "))

    # Map selection to price with if/elif statements
    if item_number == 1:
        item_price = PRICE_TURKEY_LEG
        item_name = "Turkey Leg"
    elif item_number == 2:
        item_price = PRICE_CHICKEN_STICK
        item_name = "Chicken-on-a-Stick"
    elif item_number == 3:
        item_price = PRICE_FUNNEL_CAKE
        item_name = "Funnel Cake"
    elif item_number == 4:
        item_price = PRICE_GORDITA
        item_name = "Gordita"
    elif item_number == 5:
        item_price = PRICE_AGUA_FRESCA
        item_name = "Agua Fresca"
    else:
        print("Invalid choice. Defaulting to Agua Fresca.")
        item_price = PRICE_AGUA_FRESCA
        item_name = "Agua Fresca"

    # CHeckpoint 5: Calculations
    subtotal = item_price * quantity
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    # Checkpoint 6: Receipt output
    print("\n----- Receipt -----")
    print(f"Item:       {item_name}")
    print(f"Quantity:   {quantity}")
    print(f"Subtotal:   ${subtotal:6.2f}")
    print(f"Tax:        ${tax:6.2f}")
    print("---------------------")
    print(f"Total:      ${total:6.2f}")

    # Fun message
    if item_number == 2 and quantity > 3:
        print("You must really love chicken-on-a-stick!")

    # Checkpoint 1: Called main gaurd


if __name__ == "__main__":
    main()
