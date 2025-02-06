score=int(input("Введите оценку за тест:"))

if score > 90:
    homework=input("Сдали ли студент все домашние задания?(да/нет):")
    if homework=="да":
      print ("Отлично!Оценка A+")
    elif homework=="нет":
        print ("Хорошая работа,но сдайте все задания!Оценка:А")
elif score >80:
    homework= input("посещал ли он более 75% занятий (да/нет):")
    if homework=="да":
        print ("Хорошо! Оценка: B")
    elif homework=="нет":
        print ( "Нужно посещать занятия! Оценка: C")
elif score <80:
    print("Старайиесь лучше!")