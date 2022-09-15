import final

class final_percentage(final):
    
    def __init__(self, class_name, current_grade, final_worth, goal):
        self._class_name = class_name
        self._current_grade = current_grade
        self._final_worth = final_worth
        self._goal = goal
    
    def calculate_need_grd(self):
        self._need_grade = (self.goal - (((100 - self.final_worth) / 100) * self.current_grade)) / (self.final_worth / 100)



class final_percentage_lowest_drop(final_percentage):

    def __init__(self, class_name, current_grade, final_worth, goal, num_tests, test_worth, test_avg, low_test):
        super().__init__(class_name, current_grade, final_worth, goal)
        self.num_tests = num_tests
        self.test_worth = test_worth
        self.test_avg = test_avg
        self.low_test = low_test
    
    def calculate_need_grd(self):
        self._need_grade = float((((self.goal/100)-((self.num_test * (self.test_avg/100) - (self.low_test/100))*((self.test_worth/100) / self.num_test))-((self.current_grade/100)*(1-(self.final_worth/100))-(self.test_avg/100)*(self.test_worth/100)))/(((self.final_worth/100)+(self.test_worth/self.num_test)/100)))) * 100
        


