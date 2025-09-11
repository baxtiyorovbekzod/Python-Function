def is_palindrome(text):
    reversed_text = text [:: -1]
    result = text == reversed_text
    return result
def main():
    while True:
        text =input("Matn:")  
        if is_palindrome (text):
            print ("matn palindrom")
            break
        else:
            print ("matn palindrom emas")
main()            