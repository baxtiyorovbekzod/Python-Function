def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def mutiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def main():
    while True:
        son=int(input("Son:"))
        son2=int(input("Son2:"))
        amal=input("Amal:")

        if amal=="+":
            result=add(son,son2)
        elif amal=="-":
            result=subtract(son,son2) 
        elif amal=="*":
            result=mutiply(son,son2)
        elif amal=="/":
            result=divide(son,son2)   
        else:
            print("Amalda faqat +,-,*,/ lar ishlatiladi")
            break

        print(result)
main()                     