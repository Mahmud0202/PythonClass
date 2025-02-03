height = float(input("Введите ваш рост:"))
weight = float(input("Введите  ваш  вес:"))
bmi =weight/ (height/100)**2
print(f"ваш bmi:{weight/(height**2)}")
if bmi <18.5:
    print("Underweight")
elif bmi < 18.5 <= bmi <24.9:
    print("normal")
elif bmi < 25 <= bmi <29.9:
    print("Owerweight")
elif bmi <30 <= bmi <34.9:
    print("Obesity class 1")
elif bmi <35 <=bmi<39.9:
    print("Obesity class 2")
elif bmi >= 40:
    print("obesity class 3")
else:
    print("To much")
              
