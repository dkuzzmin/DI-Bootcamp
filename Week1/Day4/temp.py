#8
import random
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

def starwarquiz(*args):
    data = args
    wrong_answers = list()
    correct_answers = list()
    flag = True
    rand_x = random.randint(0,len(data)-1)
    while len(correct_answers)+len(wrong_answers) < len(data):
        while rand_x in wrong_answers or rand_x in correct_answers:
            rand_x = random.randint(0,len(data)-1)
        # print(rand_x)
        print(data[rand_x]["question"])
        answer = input()
        if answer == data[rand_x]["answer"]:
            print("Exactly!")
            correct_answers.append(rand_x)
        else:
            print("No!")
            wrong_answers.append(rand_x)
    return wrong_answers, correct_answers

def usersstat(wrong:list, correct:list):
    print(f"Your stats:{int(100*len(correct)/(len(correct)+len(wrong)))}%")
    print(f"Correct answers:{len(correct)}")
    print(f"Wrong answers:{len(wrong)}")
    

usersstat(*starwarquiz(*data))

