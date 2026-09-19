# 1.  Interactive Terminal E-Commerce Cart & Inventory Tracker 
# Available inventory: Item Name -> Unit Price 
catalog = { 
    "laptop": 800, 
    "mouse": 20, 
    "keyboard": 50, 
    "monitor": 150 } 

grand_total = 0

while True:
    command = input("Enter item to buy(or 'Checkout'/'Exit'):  ").lower()

    if command == "exit":
        print("Exiting the program.")
        break
    elif command == "checkout":
        break

    elif command in catalog:
        price = catalog[command]
        grand_total += price
        print(f"Added {command.title()} (${price}) to order.")

    else:
        print("--> [ERROR] Item not found in catalog. Try again.")

if command == "checkout":
    subtotal = grand_total

    if subtotal>=500:
        discount_rate = 0.10
    elif 200<= subtotal<500:
        discount_rate = 0.05
    else:
        discount_rate = 0.0

    discount = subtotal * discount_rate
    final_total = subtotal - discount

    print("\nCHECKOUT RECEIPT")
    print("=" *40)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: ${discount:.2f}")
    print(f"Final Total: ${final_total:.2f}")
    print("=" *40)

# 2. Student Grade Evaluator & Class Performance Tracker Scenario 

count = int(input("How many student entries do you want to create?: ")) 
student_records = {}

for i in range(count):
    print(f"---Entry {i + 1}---")
    name = input(f"Enter student name: ")
    score = float(input(f"Enter score (0-100): "))
    student_records[name] = score

# Evaluate all students
print("=" * 40)
print("EVALUATION RESULTS") 
print("=" * 40)

for name, score in student_records.items():
    if score >=70:
        Grade = "A"
        Status = "Passes with Distinction"
    elif score >=50:
        Grade = "B"
        Status = "Passed"
    elif score <50:
        Grade = "F"
        Status = "Needs Improvement"
   
    print(f"{name}: Score {score} | Grade {Grade} | {Status}")

# Calculate class performance

average_score = sum(student_records.values()) / len(student_records)
total_passed = sum(1 for score in student_records.values() if score >= 50)
total_failed = sum(1 for score in student_records.values() if score < 50)

# Display class performance
print("=" * 40)
print("CLASS PERFORMANCE")
print("=" * 40)
print(f"Average Score: {average_score:.2f}")
print(f"Total Passed: {total_passed}")
print(f"Total Failed: {total_failed}")

# 3. Backend Data Processing & User Audit Tool Scenario 

# Raw user records: (User ID, Name, Role, Is_Active, Login_Attempts) 

users = [(101, "Alice", "admin", True, 1),  
         (102, "Bob", "member", True, 4),  
         (103, "Charlie", "editor", False, 0),  
         (104, "Diana", "admin", False, 6), 
         (105, "Evan", "member", True, 2),  
         (106, "Fiona", "guest", True, 0), ] 

active_users = 0
inactive_users = 0
flagged_users = 0

for user in users:
    if user[3] == True:
        active_users += 1

    if user[3] == True and user[2] == "admin":
        print(f"[GRANT] Full system access granted to {user[1]} (ID: {user[0]})")
    elif user[3] and user[2] in ["member", "editor"]:
        print(f"[GRANT] Standard access granted to {user[1]} (ID: {user[0]})")
    elif user[3] == False:
        inactive_users += 1
        print(f"[DENIED] Account {user[1]} is inactive.")

    if user[4] >= 5:
        flagged_users += 1
        print(f"[ALERT] Account {user[1]} is LOCKED due to excessive failed logins {user[4]} attempts.")


print("AUDIT SUMMARY REPORT")
print("=" * 40)
print(f"Total Active Users: {active_users}")
print(f"Total Inactive Users: {inactive_users}")
print(f"Total Security Alerts: {flagged_users}")