def calculator():
    print('Выберите опеацию')
    print('1,+')
    print("2,-")
    print("3,*")
    print("4,/")
    print("5,%")
    print("6,pow")
    print("7,pow3")
    print("8,sqrt")
  

    oper =input("Введите номер операции (1/2/3/4/5/6/7/8):")

    num1 =float(input(" Введите первое число:"))
    num2 =float(input( " Введите второе число:")) 
    
    if oper == '1':
        print(num1 + num2)
    elif oper == '2':
        print(num1 - num2)
    elif oper == '3':
        print( num1 * num2)
    elif oper == '4':
        print( num1 / num2)
    elif oper == '5':
        print( num1 * num2) /100
    elif oper == '6':
        print(num1 **num2)
    elif oper == '7':
        print(num1 ** 3)
    # elif oper =='8':
    #     print(math.sqrt(num1))
    calculator()
   







    