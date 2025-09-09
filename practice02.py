from datetime import date

def calculate_age(birth_year):
    current_date = date. today ()

    age = current_date.year - birth_year
    return age

name = input ("Name: ")
birth_year = int(input("Birth Year: "))

age = calculate_age(birth_year)
print(f"{name}, sizning yoshingiz: {age}")