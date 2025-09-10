def calculate_tax(salary):
   
    if salary > 5_000_000:
        tax_rate = 20
    else:
        tax_rate = 13
    return salary * tax_rate / 100

def calculate_net_salary(salary):
    return salary - calculate_tax(salary)

def main():
    salary = float(input("Maoshni kiriting: "))
    
    net = calculate_net_salary(salary)
   
    print(f"Sof maosh: {net}")

main()