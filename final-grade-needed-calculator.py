import sys
print('Final Grade Calculator')
print('')

def calc():
    print("Choose one Option: ")
    print("A1- Final is Worth a Percentage of Grade")
    print("A2- Final is Worth a Percentage of Grade w/ Lowest Test/Quiz/Midterm Drop")
    print("A3- Final is Worth a Percentage of Grade w/ Lowest Test/Quiz/Midterm Full Score Replacement")
    print("A4- Final is Worth a Percentage of Grade w/ Lowest Test/Quiz/Midterm Parital Score Replacement (using final percentile equivalent)")
    print("B1- Final is Worth Points of Grade")
    print("B2- Final is Worth Points of Grade w/ Lowest Test/Quiz/Midterm Drop")
    print("B3- Final is Worth Points of Grade w/ Lowest Test/Quiz/Midterm Full Score Replacement")
    print("B4- Final is Worth Points of Grade w/ Lowest Test/Quiz/Midterm Parital Score Replacement (using final percentile equivalent)")
    print("Any Other Input- Exit")
    print('')
    value = input("Enter Choice #: ")

    if value == 'A1':
        current_grade = input('Enter your Current Grade (%): ')
        final_worth = input("Enter Final Worth (%): ")
        goal = input("Enter your Goal (%): ")
        need_grade = (float(goal) - (((100 - float(final_worth)) / 100) * float(current_grade))) / (float(final_worth) / 100)
        print('You need a %s percent on the final to get a %s percent overall grade.' % (round(need_grade,3), goal))
        print('')
        input("Press enter to continue...")
        print ('')

    elif value == 'A2':
        current_grade = float(input("Enter Current Grade (%): "))
        final_worth = float(input("Enter Final Worth (%): "))
        goal = float(input("Enter Goal (%): "))
        num_test = float(input("Enter # of Test: "))
        test_worth = float(input("Enter Test Category Worth (%): "))
        test_avg = float(input("Enter Test Category Avarage (%): "))
        low_test = float(input("Enter Lowest Test (%): "))
        need_grade = float((((goal/100)-((num_test * (test_avg/100) - (low_test/100))*((test_worth/100) / num_test))-((current_grade/100)*(1-(final_worth/100))-(test_avg/100)*(test_worth/100)))/(((final_worth/100)+(test_worth/num_test)/100))))
        need_grade = float(100*need_grade)
        print("You need a %s percent on the final to get a %s percent overall grade. Good Luck!" % (round(need_grade,3), goal))
        print('')
        input("Press enter to continue...")
        print ('')
    else:
        sys.exit()

while True:
    calc()