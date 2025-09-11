def calculate_bmi(weight, height):
    bmi=weight/(height**2)
    return bmi

def bmi_status(bmi):
    if bmi < 18.5:
       return "Underweight (ozg'in)"
    elif 18.5<= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight (semiz)"
    elif bmi >= 30:
        return "Obesity (semirib ketgan)"

height=float(input("Bo'y:"))
weight=float(input("Vazn:"))

bmi = calculate_bmi(weight, height)
status = bmi_status (bmi)
print(status)    