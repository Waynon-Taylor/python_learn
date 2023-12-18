print("Quiz Game")

questions_awnsers = {
    "who created Python?: ":
    {
        "awnser": "A",
        "options": ["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"]
    },

    "what year was python created?: ":
    {
        "awnser": "B",
        "options": ["A. 1989", "B. 1991", "C. 2000", "D. 2016"]
    },
    "Python is tributed to which comedy group?: ":
    {
        "awnser": "C",
        "options": ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"]
    },
    "Is the earth round?: ":
    {
        "awnser": "A",
        "options": ["A. True", "B. False", "C. sometimes", "D. what's Earth?"]
    }
}

def question(questions_awnsers):
    current_score = 0
    for question, awnsers in questions_awnsers.items():
        print(question)
        for awnser in awnsers['options']:
            print(awnser)
        user_input = input('?').lower()
        if user_input == awnsers['awnser'].lower():
            current_score += 1
    return current_score

print("total score:"+ str(question(questions_awnsers)))
