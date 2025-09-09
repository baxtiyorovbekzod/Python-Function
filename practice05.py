def taxminni_tekshirish(sirli_son, taxmin):
    return sirli_son == taxmin   

def natija_chiqarish(togri):
    if togri:
        print(" To‘g‘ri topildi")
    else:
        print("Xato topildi.")

def main():
    sirli_son = 7   
    taxmin = int(input("Son kiriting: "))
    
    togri = taxminni_tekshirish(sirli_son, taxmin) 
    natija_chiqarish(togri)                         
main()