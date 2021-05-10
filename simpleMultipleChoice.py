from Question import Question


question_prompts = [
    "What color are Apples?\n(a) Red/Green\n(b) Purple \n(c) Orange\n\n",
    "\nWhat color are Banana?\n(a) Teal\n(b) Magenta \n(c) Yellow\n\n",
    "\nWhat color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt + 'answer: ')
        if answer.lower() == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)

restart = input("Try again?(yes): ")

if restart == 'yes':
    run_test(questions)
else:
    exit()



