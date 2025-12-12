import json, os
file="tasks.json"
tasks = []

if os.path.exists(file):
    with open(file) as f: tasks=json.load(f)

while True:
    print("\n1. Add  2. Remove  3. Complete  4. Show  5. Exit")
    choice = input("Choice: ")
    if choice=='1':
        task=input("Enter task: ")
        tasks.append({"task":task,"done":False})
    elif choice=='2':
        idx=int(input("Task index to remove: "))
        if 0<=idx<len(tasks): tasks.pop(idx)
    elif choice=='3':
        idx=int(input("Task index to complete: "))
        if 0<=idx<len(tasks): tasks[idx]["done"]=True
    elif choice=='4':
        for i,t in enumerate(tasks): print(f"{i}: {t['task']} [{'Done' if t['done'] else 'Pending'}]")
    elif choice=='5': break

with open(file,"w") as f: json.dump(tasks,f)
print("Tasks saved!")
