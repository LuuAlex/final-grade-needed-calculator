import sys, final_percentage

print("Final Grade Calculator")
print('')

# TODO: make sqlite3 database, run object when called on with "View Prevous Calculations"

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
        class_name = input("Enter the name of the class: ")
        current_grade = input("Enter your Current Grade (%): ")
        final_worth = input("Enter Final Worth (%): ")
        goal = input("Enter your Goal (%): ")

        # TODO: store entries in sqlite3 database with class_name, and unique number

        entry = final_percentage(class_name, current_grade, final_worth, goal)
    
    else:
        sys.exit()