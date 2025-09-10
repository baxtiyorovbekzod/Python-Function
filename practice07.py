questions = "Messi nechanchi yil?"

correct_answer = "1987"

user_answer = input("> ")

def check_answer(user_answer, correct_answer):

    
    if user_answer == correct_answer:
        print("True")
    
    else:
        print("False")

check_answer(user_answer,correct_answer)
   