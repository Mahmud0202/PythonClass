print("золото")
print("серебро")
print("обычный")

membership = str(input("Введите  членства:"))
amount = float(input("Выберите сумму покупки:"))
discount =0

if membership =="золото":

    if amount > 100:
        print("ваша скидка 20%")
        discount = 0.2 
    else:
        print("ваша скидка 10%") 
        discount=0.1
        
elif membership =="серебро":
    
    if amount > 100: 
       print("ваша скидка 15%")
       discount = 0.15 
    else: 
        print("ваша скидка 5%")
        discount = 0.05
        
        
elif membership =="обычный":    
     if amount > 100:          
        discount=0.05 
elif amount <100:
         print("у вас нет скидки")
         discount=0
         
       
price =  amount *(1-discount)  

print(f"Сумма после скидки:{price:.2f}")  