import sys
from final_percentage import *
from final_points import *

print("Final Grade Calculator")
print('')


# TODO: make sqlite3 database, run object when called on with "View Previous Calculations"
# TODO: make database file; make database class to update, store, retrieve info from database

# Default input for percentage
def default_input_percentage():
    class_name = input("Enter the name of the class: ")
    current_grade = float(input("Enter your Current Grade (%): "))
    final_worth = float(input("Enter Final Worth (%): "))
    goal = float(input("Enter your Goal (%): "))

    return class_name, current_grade, final_worth, goal


# Default input for points
def default_input_points():
    class_name = input("Enter the name of the class: ")
    current_grade = float(input("Enter your Current Amount of Points: "))
    total_points = float(input("Enter Total Amount of Points Possible: "))
    final_worth = float(input("Enter Final Point Worth: "))
    goal = float(input("Enter your Goal Amount of Points: "))

    return class_name, current_grade, total_points, final_worth, goal


# Creates pauses
def end_pause():
    print('')
    input("Press enter to continue...")
    print('')


while True:
    print("Choose one Option: ")
    print("A1- Final is Worth a Percentage of Grade")
    print("A2- Final is Worth a Percentage of Grade w/ Lowest Test/Quiz/Midterm Drop")
    print("A3- Final is Worth a Percentage of Grade w/ Lowest Test/Quiz/Midterm Full Score Replacement")
    print(
        "A4- Final is Worth a Percentage of Grade w/ Lowest Test/Quiz/Midterm Partial Score Replacement (using final percentile equivalent)")
    print("B1- Final is Worth Points of Grade")
    print("B3- Final is Worth Points of Grade w/ Lowest Test/Quiz/Midterm Drop Full Score Replacement")
    print(
        "B4- Final is Worth Points of Grade w/ Lowest Test/Quiz/Midterm Partial Score Replacement (using final percentile equivalent)")
    print("0 - View Previous Calculations")
    print("Any Other Input- Exit")
    print('')
    value = input("Enter Choice #: ")

    if value == "A1":
        class_name, current_grade, final_worth, goal = default_input_percentage()

        # TODO: store entries in sqlite3 database with class_name, and unique number

        entry = FinalPercentage(class_name, current_grade, final_worth, goal)
        entry.calculate_need_grd()

        entry.need_grd_print()
        end_pause()

    elif value == "A2":
        class_name, current_grade, final_worth, goal = default_input_percentage()

        num_test = float(input("Enter # of Test: "))
        test_worth = float(input("Enter Test Category Worth (%): "))
        test_avg = float(input("Enter Test Category Average (%): "))
        low_test = float(input("Enter Lowest Test (%): "))

        # TODO: store entries in sqlite3 database with class_name, and unique number

        entry = FinalPercentageLowestDrop(class_name, current_grade, final_worth, goal, num_test, test_worth,
                                             test_avg, low_test)
        entry.calculate_need_grd()

        entry.need_grd_print()
        end_pause()

    elif value == "B1":
        class_name, current_grade, total_points, final_worth, goal = default_input_points()

        entry = FinalPoints(class_name, current_grade, total_points, final_worth, goal)
        entry.calculate_need_grd()

        entry.need_grd_print()
        end_pause()

    elif value == "B3":
        class_name, current_grade, total_points, final_worth, goal = default_input_points()

        drop_test_worth = float(input("Enter Lowest Test/Quiz/Midterm Worth in Points: "))
        drop_test_score = float(input("Enter Lowest Test/Quiz/Midterm Score in Points: "))

        entry = FinalPointsLowestFullReplacement(class_name, current_grade, total_points, final_worth, goal,
                                                     drop_test_worth, drop_test_score)
        entry.calculate_need_grd()

        entry.need_grd_print()
        end_pause()

    else:
        sys.exit()
