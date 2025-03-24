class Student:
    def __init__(self,name,student_id,grades):
        self.name=name
        self.student_id=student_id
        self.grades=[]
        
    def add_grade(self,grades):
        self.grades.append(grades)
    
    def calculate_average(self):
        return sum (self.grades)/ len (self.grades)
    def get_best_grade(self): 
        return max(self.grades) if self.grades else None
    def get_worst_grade(self): 
        return min(self.grades) if self.grades else None
    def display_info(self):
        average = self.calculate_average()
        best_grade =self.get_best_grade()
        worst_grade =self.get_worst_grade()
        print(f"Имя студента: {self.name}")
        print(f"ID Студента: {self.student_id}")
        print(f"Средний балл : {average}")
        print(f"Лучшая оценка:{best_grade}")
        print(f"Худая оценка:{worst_grade}")

class StudentManager:
    def __init__(self):
        self.students=[]

    def add_student(self,student):
        self.students.append(student)        
    def get_top_students(self):
        return max(self.students,key=lambda student: student.calculate_average())   
    def get_lowest_student(self): 
        return min(self.students,key=lambda student: student.calculate_average())
    
    def display_all_students(self):
        if not self.students:
            print("Список стдуентов пуст")
        for student in self.students:
            student.display_info()
            print(f"Лучший студент:{self.get_top_students()}")
            print(f"Студент с худшими оценками:{self.get_lowest_student()}")
student1=Student("Alice Johnson", 101, 97)  
student2=Student("Bob Smith",102, 88) 

student1.add_grade(97)
student2.add_grade(76)
student2.add_grade(73)
student1.add_grade(95)
student2.add_grade(98)
student1.add_grade(96)

student1.display_info()
student2.display_info()

manager =StudentManager()
manager.add_student(student1)
manager.add_student(student2)
manager.display_all_students()
    