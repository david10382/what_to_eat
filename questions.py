import inquirer
from data import menu
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

def question_0(answerList):
    questions = [
      inquirer.List('geo_question',
                    message="Okay let's choose an origin",
                    choices=['south asian', 'europe', 'south america', 'east asian', 'eastern europe', 'north america'],
                ),
    ]
    questions0_answers = inquirer.prompt(questions)
    answerList.update(questions0_answers)
    # print(questions0_answers)
    # print(answerList)
    return answerList

def question_1(answerList):
    questions = [
      inquirer.List('first_question',
                    message="Okay let's choose a base",
                    choices=['rice', 'soup', 'noodle', 'bread','none'],
                ),
    ]
    questions1_answers = inquirer.prompt(questions)
    answerList.update(questions1_answers)
    # print(questions1_answers)
    # print(answerList)
    return answerList

def question_2(answerList):
    questions = [
      inquirer.List('second_question',
                    message="Okay let's choose a protein",
                    choices=['chicken','seafood','beef', 'pork', 'vegetarian'],
                ),
    ]
    questions2_answers = inquirer.prompt(questions)
    answerList.update(questions2_answers)
    # print(questions1_answers)
    # print(answerList)
    return answerList
  
def question_3(answerList):
    questions = [
      inquirer.List('third_question',
                    message="Now, do you have any allergies?",
                    choices=['nut', 'dairy', 'gluten', 'meat', 'seafood', 'none'],
                ),
    ]
    questions3_answers = inquirer.prompt(questions)
    answerList.update(questions3_answers)
    # print(questions1_answers)
    # print(answerList)
    return answerList


def resultDisplay(result):
  if len(result) > 0:
    print("You can go and grab...")
    for final_ans in result:

      print("=>", final_ans)
  else:
    print("Sorry, we can't find your match")


def question_list():
  answerList = {}
  question_0(answerList)
  question_1(answerList)
  question_2(answerList)
  question_3(answerList)


