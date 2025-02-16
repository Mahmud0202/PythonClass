def mask_card_number(card_number):
    if len(card_number) != 16 or not card_number.isdigit():  
        return "Invalid card number"
    return '*' * 12 + card_number[-4:] 

card_number = input("Введите номер карты: ")
print(mask_card_number(card_number))

