marks = list(map(int, input("Enter marks: ").split()))
avg = sum(marks) / len(marks)

if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Average:", avg)
print("Grade:", grade)
