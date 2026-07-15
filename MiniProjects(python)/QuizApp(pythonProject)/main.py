def run_quiz():
    questions = [
        {
            "question": "Who is developer of Python?",
            "options": ["A) Guido van Rossum", "B) James Gosling", "C) Bjarne Stroustrup", "D) Dennis Ritchie"],
            "answer": "A) Guido van Rossum"            
        },
        {
            "question": "What type of programming language is Python?",
            "options": ["A) Compiled", "B) Interpreted", "C ) Assembly", "D) Machine Language"],
            "answer": "B) Interpreted"  
        },
        {
            "question": "What is the output of print(2 ** 3)?",
            "options": ["A) 6", "B) 8", "C) 9", "D) 5"],
            "answer": "B) 8"        
        },
        {
            "question": "Which of the following is a mutable data type in Python?", 
            "options": ["A) Tuple", "B) List", "C) String", "D) Integer"],
            "answer": "B) List"     
        },
        {
            "question": "What is the correct way to define a function in Python?",
            "options": ["A) function myFunction():", "B) def myFunction():", "C) func myFunction():", "D) define myFunction():"],
            "answer": "B) def myFunction():"
            
        }
    ]

    score = 0
 
    for index,q in enumerate(questions):   
        print(f"Q{index + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        user_answer = input("\n  Choose the correct option (A/B/C/D):------------------- ") 
        if user_answer.strip().upper() == q['answer'][0]:
            print("You guessed it right ! \n Your answer is correct\n")
            score += 1

    print(f" Are you ready to see the final score \n Your final score is {score}/{len(questions)}")
    print("Keep practicing and learning Python-------------")

run_quiz()