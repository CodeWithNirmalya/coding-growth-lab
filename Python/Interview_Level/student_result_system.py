'''
5. Student Result System (Functions + Dictionary)

Store 5 students and marks in a dictionary. Print:

Highest scorer

Lowest scorer

Average marks

Passed students (≥40)'''


students = {
    "Nirmalya": 85,
    "Rahul": 38,
    "Ananya": 92,
    "Priya": 67,
    "Sourav": 45
}
#Highest scorer
def highest_scorer(data):
    topper = max(data,key = data.get)
    print(f'The highest scorer of this class is {topper} with the marks of  {data[topper]}')

#Lowest scorer

def lowest_scorer(data):
    lowest = min(data,key = data.get)
    print(f"The lowest scorer in this class is {lowest}  with the marks of {data[lowest]}")

# Average marks
def average_score(data):
    avg = sum(data.values()) /len(data)
    print("Average Marks:", round(avg, 2))


# Passed Students
def passed_students(data):
    print("Passed Students:")
    for name, mark in data.items():
        if mark >= 40:
            print(name, "-", mark)




highest_scorer(students)
lowest_scorer(students)
average_score(students)
passed_students(students)
