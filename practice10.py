def is_strong_password(password):
    
        return len(password)>8 and password.isalnum()
def main():
    while True:
         
        password=input("Pasword:") 
           
        if is_strong_password(password):
            print("Parol tastiqlandi.")
            break
        else:
             print("Parol kuchsiz qaytatdan parol kiriting!")
main()             

           
