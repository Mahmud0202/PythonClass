scores=list(map(int,input("Введите список оценок через пробел").split()))
even_numbers = 0
odd_numbers = 0
result=[]
for score in scores:
    if score >=95:
        grade="A"
        result.append((score,"Сдал"))
    elif score >=90:
        grade="А"
        result.append((score,"Сдал"))
    elif score >=89:
        grade="B"
        result.append((score,"Сдал"))
    elif score >=85:
        grade="B"
        result.append((score,"Сдал"))
    elif score >=80:
        grade="B"
        result.append((score,"Сдал"))
    elif score >=77:
        grade="С"
        result.append((score,"Сдал"))
    elif score >=72:
        grade="С"
        result.append((score,"Сдал"))
    elif score >=68:
        grade="D"
        result.append((score,"Сдал"))
    elif score >=55:
        grade="F"
        result.append((score," Не сдал"))
    elif score >=47:
        grade="F"
        result.append((score,"Не сдал"))
    else:
        grade="F"
        result.append((score,"Не удача")) 

    print(f"балл:  {score} оценка: {grade}  Результат {result}")
    
    even_numbers += score % 2 == 0
    odd_numbers += score % 2 != 0
    print(f"Четных оценок:  {even_numbers}")
    print(f"Нечетных оценок:  {odd_numbers}")