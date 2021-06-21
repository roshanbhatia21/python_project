#General Knowledge Quiz for students
print("**********GENERAL KNOWLEDGE QUIZ**********")
def start_game():

    std_answers=[]
    correct_answers=0
    ques_num=1
    for key in questions:
        print("******************************************")
        print(key)
        for i in options[ques_num-1]:
            print(i)
        guess=input("ENTER(A,B,C or D)n: ")  
        guess=guess.upper()
        std_answers.append(guess)  

        correct_answers += check_answer(questions.get(key), guess)
        ques_num +=1

    display_result(correct_answers, std_answers)
#creating function for checking answers
def check_answer(answer, guess):

    if answer==guess:
        print("YOUR ANSWER IS CORRECT!!")
        return 1
    else:
        print("WRONG ANSWER")
        return 0
#creating function for displaying results
def display_result(correct_answers, std_answers):
    print("*************************")
    print("RESULTS")
    print("*************************")

    print("ANSWERS:",end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("YOUR ANSWERS:",end=" ")

    for i in std_answers:
        print(i, end=" ")
    print()
    score = float((correct_answers/len(questions))*100)
    print("YOUR SCORE "+ str(score)+ "%")
    
         
#creating function for play again 
def play_again():

    response = input("DO YOU WANT TO PLAY AGAIN? (YES OR NO): ")
    response=response.upper()

    if response == "YES":
        return True
    else:
        return False

questions = { "1.What is capital of india?": "A",
"2.National Bird of India is?": "B",
"3.How many days are there in a week?": "C"}
options=[["A. DELHI", "B. JAIPUR", "C. MUMBAI", "D. CHENNAI"],
["A. Sparrow", "B. Peacock", "C. penguin", "D. OSTRICH"],
["A. 5","B. 6", "C. 7", "D. 9"]
]
   
start_game()

while play_again():
    start_game()

print("THANK YOU!!")

        





