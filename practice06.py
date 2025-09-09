phone = input("Telefon raqamingiz: ")

def is_valid_phone_number(phone):
   
    return phone.isdigit() and len(phone) == 9

if is_valid_phone_number(phone):
    print(True)
else:
    print(False)