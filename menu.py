import sys
from final_percentage import*

print("Final Grade Calculator")
print('')

# TODO: make sqlite3 database, run object when called on with "View Prevous Calculations"
# TODO: make database file; make database class to update, store, retrive info from database

def defualt_input_percentage():
    class_name = input("Enter the name of the class: ")
    current_grade = float(input("Enter your Current Grade (%): "))
    final_worth = float(input("Enter Final Worth (%): "))
    goal = float(input("Enter your Goal (%): "))

    return class_name, current_grade, final_worth, goal


while True:
    print("Choose one Option: ")
    print("A1- Final is Worth a Percentage of Grade")
    print("A2- Final is Worth a Percentage of Grade w/ Lowest Test/Quiz/Midterm Drop")
    print("A3- Final is Worth a Percentage of Grade w/ Lowest Test/Quiz/Midterm Full Score Replacement")
    print("A4- Final is Worth a Percentage of Grade w/ Lowest Test/Quiz/Midterm Parital Score Replacement (using final percentile equivalent)")
    print("B1- Final is Worth Points of Grade")
    print("B2- Final is Worth Points of Grade w/ Lowest Test/Quiz/Midterm Drop")
    print("B3- Final is Worth Points of Grade w/ Lowest Test/Quiz/Midterm Full Score Replacement")
    print("B4- Final is Worth Points of Grade w/ Lowest Test/Quiz/Midterm Parital Score Replacement (using final percentile equivalent)")
    print("0 - View Previous Calculations")
    print("Any Other Input- Exit")
    print('')
    value = input("Enter Choice #: ")

    if value == "A1":
        class_name, current_grade, final_worth, goal = defualt_input_percentage()

        # TODO: store entries in sqlite3 database with class_name, and unique number

        entry = final_percentage(class_name, current_grade, final_worth, goal)

    if value == "A2":
        class_name, current_grade, final_worth, goal = defualt_input_percentage()

        num_test = float(input("Enter # of Test: "))
        test_worth = float(input("Enter Test Category Worth (%): "))
        test_avg = float(input("Enter Test Category Avarage (%): "))
        low_test = float(input("Enter Lowest Test (%): "))

        # TODO: store entries in sqlite3 database with class_name, and unique number

        entry = final_percentage_lowest_drop(class_name, current_grade, final_worth, goal, num_test, test_worth, test_avg, low_test)
    
    else:
        sys.exit()