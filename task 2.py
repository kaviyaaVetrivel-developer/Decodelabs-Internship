cost=[]
total =0

print("Welcome to Expense Tracker")
print("\nEnter 0 to exit")
while True:
    expense = float(input("Enter Expense:"))

    if expense == 0:
        break
    cost.append(expense)
    total += expense

print("\n============RECIPT=============")
for i , expense in enumerate(cost, start=1):
    print(f"Expense {i} : ₹{expense}")
print("-------------------------------")
print(f"Total expense is : ₹{total}")
print("===============================")