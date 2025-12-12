import csv
expenses=[]
while True:
    amt = float(input("Enter amount (0 to stop): "))
    if amt==0: break
    cat = input("Category: ")
    desc = input("Description: ")
    expenses.append({"amount":amt,"category":cat,"desc":desc})

summary={}
for e in expenses:
    summary[e["category"]] = summary.get(e["category"],0)+e["amount"]

print("\nExpense Summary:")
for k,v in summary.items(): print(f"{k}: {v}")

save = input("Export to CSV? (y/n): ").lower()
if save=='y':
    with open("expenses.csv","w",newline="") as f:
        writer = csv.DictWriter(f,fieldnames=["amount","category","desc"])
        writer.writeheader()
        writer.writerows(expenses)
    print("Saved to expenses.csv")

