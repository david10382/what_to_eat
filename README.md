# What_to_eat - What is it?

'What to eat' is a terminal application that helps the user to match with a menu item for their next meal application. This is achieved through a series of questions to determine what they should eat. The application takes in to account for factors such as origin of meal, choice of protiens, and allergies. 

The application also takes into account the possible user's state of mind. If the user is ready to explore menu items without inputting any preferences, they are able to utilise the random generator to return a menu item determined by the application. 

Furthermore, the user is able to confirm ingredients of the menu items which can assist in finding preferences. For example, if the application returned 'Thai Grilled Chicken' through the random generator but the user would like to view the ingredients, the application provides a list of ingredients in the 'Menu Item ingredients'. 


# Development process

The development process began with a Trello board to help with listing the desired fucntions and features of the appllication. It has also helped with tracking progress of the build of the application and prioritising the deliverables.  
 
 ![Trello board](./images/Trello%20board%20for%20T1A3.png)
 ![Trello board time line](./images/Trello%20board%20time%20line.png)
 ![Trello board prioritization](./images/Trello%20board%20time%20line%20-%20priortisation.png)

The development process began with mapping the application structure. It has aided in determining the functionality of the application, as well as in aiding the relationships between fucntions and the dictionary containing the menu items. 

1. Application structure 

Next step in the process was to map the application structure. Mapping the structure of the application helped determine the functionality of the application, as well as in aiding the relationships between fucntions and the dictionary containing the menu items.

![Application Structure](./images/Application%20Strucutre%20Overview.drawio.png)

2. Selection Process flow chart 

The Selection Process flow chart explains the steps in which the feature interacts with the dictionary of menu items and user inputs. The Selection process involves five questions, utilising the enquirer library, with set answers that return a menu item. As the user inputs their choices, the choices are stored in a temporary list which compares and filters the possible menu items. 

![Selection process flow chart](./images/Selection%20Process%20flow%20chart.drawio.png)

4. Testing methods 
Integrated Testing (big bang approach)

https://github.com/david10382/what_to_eat/blob/main/Testing%20/Integrated%20Testing%20for%20What%20to%20eat%20App.pdf

Random generator testing 

```
import random_gen


def test_randg():
    firstAns = str(random_gen.menu_random())
    secondAns = str(random_gen.menu_random())
    thirdAns = str(random_gen.menu_random())
    
    if firstAns == secondAns and secondAns == thirdAns:
        print("Error")
    else:
        print("Test passed")

test_randg()
```

# Features and Functionality 
'What to eat' employs the following libraries:
1. enquirer (external package)
2. difflib (buitl in package)
3. randdom (built in package)

'What to eat' uses the enquirer package to ask the user questions and validate the answers. This is utilised most in the 'Selections'(selection process) feature. 

'Surprise me' (random menu item generator) uses the random package to return a menu item determined by the application when chosen.

'Menu Item Ingredients' feature is that returns the ingredients in a Menu Item. It uses the difflib package and SequenceMatcher and get_close_matches to correct any spelling errors from the user input.



# Installation

Python3 is required to run the application.

https://www.python.org/downloads/

# Dependancies

The application requires the user have  inquirerer package installed on their computer. 

``` pip install inquirer or pip3 install inquirer ```



# Usage

1. Selection Process 
    Selection process is named 'Selections' in the application, and as explained above, is a feature that filters user choices and returns a menu item by comparing the dictionary of menu items. The user must go through and pick answers from five questions:

Let's find something to eat?:

    1. confirm that you wish to find menu item based on preferences by picking 'yes'.
    2. confirm that you do not wish to do so by picking 'no'
    3. pick 'Surpirse me!' if you would rather find menu item at random

Choose an Origin:
         
    pick a preference by geography i.e. south asian.

Choose a base:
         
    pick a preference by geography i.e. rice.

Choose Protein

         pick a preference by protien  i.e. chicken.

Any Allergies

        pick to remove any category of allergy  i.e. seafood.

2. Lookup feature for the ingredients in a menu 

        At the start of the application, pick 'Menu Item Ingredient'.
        Then type the desired Menu item to view list of ingredients.

3. Random generator 

        pick the 'Surprise me!' option in the beginning of the Selection stage.

# Link to github 

https://github.com/david10382/what_to_eat