import inquirer
from welcome import init_welcome
from app import init_get_menu
from goodbye import goodbye

home_questions = [
  inquirer.List('home_page',
                message="Welcome! Let's find you something to eat",
                choices=['Selections', 'Menu Item Ingredients', 'Exit'],
            ),
]
answers_home = inquirer.prompt(home_questions)

def search_user_answer(user_ans):
  user_ans = answers_home['home_page'].lower()
  if user_ans == 'selections':
    init_welcome()
  elif user_ans == 'quick search':
    init_get_menu()
  elif user_ans == 'exit':
    goodbye()

search_user_answer(answers_home)
