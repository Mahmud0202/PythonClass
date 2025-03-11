students = [
 {
     "name": "Alice",
 "subjects": ("Math", "Physics", "English"),
 "scores": {"Math": 85,"Physics": 78, "English": 92}},
 {
     "name": "Bob", 
"subjects": ("Math", "Biology", "English"), "scores": {"Math": 72,
"Biology": 88, "English": 80}},
 {
     "name": "Charlie",
"subjects": ("Math", "Physics", "Chemistry"), "scores":
{"Math": 90, "Physics": 95, "Chemistry": 85}},
]

# def display_studens(data):
#     for student in data:
#         name = student["name"]
#         subject = "," .join(student["subjects"])
#         print(f"{name} is enrolled in:{subject}")

# display_studens(students)


# def get_average_score(name, students):
#     for student in students:
#         if student["name"] == name:
#             scores = student["scores"].values()
#             return sum(scores) / len(scores)  
# print(get_average_score("Alice", students))

# get_average_score(students)


def find_top_student(students):
    for student in students:
        top_score = 0
        top_student =[]
        for studen in students:
            avg_score = sum(student["score"].values())/(len(student["score"]))
            if avg_score > top_score:
                top_score = avg_score
                top_student = student["name"]
        return top_student
print(find_top_student(students))

# find_top_student(students)


def failed_students(students, passing_score=50):
    failed_names = []
    for student in students:
        for subject, score in student["scores"]():
            if score < passing_score:
                failed_names.append(student["name"])
    return failed_names