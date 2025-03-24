from abc import ABC, abstractmethod

# Абстрактный класс Employee
class Employee(ABC):
    def _init_(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @abstractmethod
    def work(self):
        pass

    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Зарплата: {self.salary}")

# Подкласс Developer
class Developer(Employee):
    def _init_(self, name, age, salary, programming_language):
        super()._init_(name, age, salary)
        self.programming_language = programming_language

    def work(self):
        print(f"{self.name} пишет код на {self.programming_language}")

# Подкласс Manager
class Manager(Employee):
    def _init_(self, name, age, salary, team_size):
        super()._init_(name, age, salary)
        self.team_size = team_size

    def work(self):
        print(f"{self.name} управляет командой из {self.team_size} сотрудников")

# Создание объектов
dev = Developer("Алекс", 30, 70000, "Python")
mgr = Manager("Екатерина", 40, 120000, 10)

# Вызов методов
dev.display_info()
dev.work()

mgr.display_info()
mgr.work()