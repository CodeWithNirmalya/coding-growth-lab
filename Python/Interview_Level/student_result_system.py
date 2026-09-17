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

def highest_scorer(data):
    topper = max(data,key = data.get)
    print(f'The highest scorer of this class is {topper} with the marks of - {data[topper]}')

highest_scorer(students)
