
def c_to_f(celsius):

    
    F = 9 / 5 * celsius +32
    return F


def f_to_c(fahrenheit):
    
    C = 5 / 9 * (fahrenheit - 32)
    return C

def main():
        check = input("> ")
        if check == "1":
            celsius = float(input("Selsiyning qiymatini kiriting: "))
            farangeyt = c_to_f(celsius)
            print (f"{celsius}==> {farangeyt} (Farangeyt)ga teng ")

        elif check == "2":
            fahrenheit = float(input("Farangeytning qiymatini kiriting: "))
            celsius = f_to_c(fahrenheit)
            print (f"{fahrenheit}==> {celsius} (Selsiy)ga teng ")
        else:
             print("Faqat celsius va fahrenheit uchun qiymat kiritish mumkin!")    
main()