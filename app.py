from data import menu
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

keys = menu.keys()


def get_menu(word):
    word = word.title()
    # print("get_close_matches(word, keys)",get_close_matches(word, keys))
    if word in menu or len(get_close_matches(word, keys)) > 0:
        if len(get_close_matches(word, keys)) > 0:
            user_input = input("Did you mean %s ? Enter Y for Yes, or N for No: " % get_close_matches(word, menu.keys())[0])
            user_input = user_input.upper()
            if user_input == "Y":
                search_result = menu[get_close_matches(word, menu.keys())[0]]
                print("Ingredient for ",word," are ...")
                print (search_result['ingredient'])
                print("Bon Appétit !!!")
    else:
        print('unknown menu item, please try again.')
        init_get_menu()


def init_get_menu():
    menu_item = input('what menu item do you want to check ingredients?:')
    # print (get_menu(menu_item))
    get_menu (menu_item)

#user_main_category = input("input main_category : ")

#for menu_type in menu:
    #print("this is menu[menu_type]",menu[menu_type])
    #for key in menu[menu_type]:
       # print("THIS IS KEY ",key)
        #if user_main_category.lower() == menu[menu_type][key].lower():
            #print(menu[menu_type])
            #print(menu[menu_type][key].lower())
            #print("\nWould you like to have :", menu_type)
#menu = recipes.load(open('data.py'))
#sub_category_answer = input("what would you like to eat?: ")
#print('ans is: ',sub_category_answer)

#if sub_category_answer.lower() == "thai":
    #print("It is thai")
    #for index in recipes:
     #   for nestedindex in recipes[index]: 
      #      if nestedindex.lower() == "sub_category":
       #         if recipes[index][nestedindex].lower() == "thai":
        #            print(recipes[index]['name'])
                    #print(nestedindex, ":",recipes[index][nestedindex])6
#else:
 #   print(" not thai")

 #def get_meal(word):
    #return menu[word]


