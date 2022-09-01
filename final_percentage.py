import final

class final_percentage(final):
    
    def __init__(self, class_name, current_grade, final_worth, goal, lowest=False, num_tests=0, test_worth=0, test_avg=0, low_test=0):
        self._class_name = class_name
        self._current_grade = current_grade
        self._final_worth = final_worth
        self._goal = goal
        self._need_grade = (float(goal) - (((100 - float(final_worth)) / 100) * float(current_grade))) / (float(final_worth) / 100)


