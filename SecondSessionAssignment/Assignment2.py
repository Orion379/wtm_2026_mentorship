# Available inventory: Item Name -> Unit Price
catalog = {
    "laptop": 800,
    "mouse": 20,
    "keyboard": 50,
    "monitor": 150
}

grand_total = 0

while True:
    command = input("Enter item to buy (or 'checkout' / 'exit'): ").lower()

    if command == "exit":
        # Cancel the order entirely, no receipt printed
        print("--> Order cancelled. Goodbye!")
        break

    elif command == "checkout":
        # Leave the loop and move on to discount logic below
        break

    elif command in catalog:
        price = catalog[command]
        grand_total += price
        print(f"--> Added {command.title()} (${price}) to order.")

    else:
        print("--> [ERROR] Item not found in catalog. Try again.")

# Only print a receipt if the user actually checked out (grand_total could
# legitimately be 0, so we check the command instead of the total).
if command == "checkout":
    subtotal = grand_total

    if subtotal >= 500:
        discount_rate = 0.10
    elif 200 <= subtotal < 500:
        discount_rate = 0.05
    else:
        discount_rate = 0.0

    discount = subtotal * discount_rate
    final_total = subtotal - discount

    print("\nCHECKOUT RECEIPT")
    print("=" * 40)
    print(f"Subtotal:      ${subtotal:.2f}")
    print(f"Discount:      ${discount:.2f}")
    print(f"Final Total:   ${final_total:.2f}")
    print("=" * 40)