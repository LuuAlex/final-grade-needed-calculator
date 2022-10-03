from final import final

class final_points(final):
    
    def __init__(self, class_name, current_grade, final_worth, goal):
        self._class_name = class_name
        self._current_grade = current_grade
        self._final_worth = final_worth
        self._goal = goal
    
    def calculate_need_grd(self):
        self._need_grade = (self._goal - self._current_grade) / self._final_worth



class final_points_lowest_full_replacement(final_points):

    def __init__(self, class_name, current_grade, final_worth, goal):
        super().__init__(class_name, current_grade, final_worth, goal)
        self._test_worth = test_worth
        self._test_avg = test_avg
        self._low_test = low_test
    
    def calculate_need_grd(self):
        self._need_grade = (self._goal - self._current_grade) / (self._final_worth + self._drop_test_worth)
        


