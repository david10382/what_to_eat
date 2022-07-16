import inquirer
from welcome import init_welcome


home_questions = [
  inquirer.List('home_page',
                message="Welcome! Let's find you something to eat",
                choices=['Selections', 'Quick Search', 'Exit'],
            ),
]
answers_home = inquirer.prompt(home_questions)

def search_user_answer(user_ans):
  user_ans = answers_home['home_page'].lower()
  if user_ans == 'selections':
    init_welcome()

search_user_answer(answers_home)
