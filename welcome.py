import inquirer

def user_selections(welcome_answerList):
    questions = [
    inquirer.List('first_question',
                    message="Welcome! Let's find you something to eat",
                    choices=['Yes', 'No', 'Surprise me!'],
                ),
    ]
    answers = inquirer.prompt(questions)
    welcome_answerList.update(answers)
    return welcome_answerList


def init_welcome():
    welcome_answerList = {}
    user_selections(welcome_answerList)

    



